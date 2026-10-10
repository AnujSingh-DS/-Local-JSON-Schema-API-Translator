import json
import urllib.request
import urllib.error
import os
import gradio as gr
from pydantic import BaseModel, Field
from typing import List, Optional

# 1. DEFINE YOUR STRUCTURAL SCHEMA
class ApiPayloadBlueprint(BaseModel):
    endpoint_name: str = Field(description="The semantic slug name of the action, lowercase with underscores.")
    http_method: str = Field(description="Must be GET, POST, PUT, DELETE, or PATCH.")
    required_parameters: List[str] = Field(description="List of parameter keys parsed from the text description.")
    auth_required: bool = Field(description="True if the request mentions tokens, keys, passwords, or authentication.")
    inferred_data_types: dict = Field(description="Key-value mapping of parameters to their expected standard types.")

# 2. THE MODEL HARNESS RUNTIME
class ModelHarness:
    def __init__(self, model_name: str = "llama3.2:3b"):
        self.url = "http://localhost:11434/api/chat"
        self.model = model_name

    def translate_to_schema(self, user_prompt: str):
        target_schema = ApiPayloadBlueprint.model_json_schema()
        
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are a strict API translation harness. Convert requirements into structures matching the schema layout."},
                {"role": "user", "content": f"Parse the following API requirement specification:\n{user_prompt}"}
            ],
            "options": {"temperature": 0.0},
            "format": target_schema,
            "stream": False
        }

        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(self.url, data=data, headers={"Content-Type": "application/json"})

        try:
            with urllib.request.urlopen(req) as response:
                res_body = response.read().decode("utf-8")
            raw_content = json.loads(res_body).get("message", {}).get("content", "{}")
            validated_output = ApiPayloadBlueprint.model_validate_json(raw_content)
            
            # Return parsed dictionary directly to help our file utility handle it safely
            return validated_output.model_dump()
        except urllib.error.URLError:
            return {"error": "❌ Connection Error: Is Ollama running in the background?"}
        except Exception as e:
            return {"error": f"❌ Validation mismatch: {e}"}

# 3. CONTROLLER FUNCTIONS FOR INTERFACE
harness = ModelHarness("llama3.2:3b")

def process_and_display(text_input):
    """Parses text and formats it into pretty JSON text for the UI code box."""
    result = harness.translate_to_schema(text_input)
    return json.dumps(result, indent=4)

def export_json_file(json_text_content):
    """Saves the active text box content into a downloadeable physical file."""
    if not json_text_content or "❌" in json_text_content:
        return None # Prevent downloading connection errors
        
    try:
        # Load string to make sure it's valid data before printing out
        parsed_data = json.loads(json_text_content)
        filename = f"{parsed_data.get('endpoint_name', 'api_spec')}.json"
        
        # Write to a clean temporary script file path local to the user directory
        file_path = os.path.join(os.getcwd(), filename)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(parsed_data, f, indent=4)
            
        # Return path directly so Gradio File widget exposes it to the browser link
        return file_path
    except Exception:
        return None

# 4. INTERACTIVE WEB UI LAYOUT
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🚀 SchemaForge: Natural Language to Strict JSON API Specs")
    gr.Markdown("Translate unstructured requirements into type-safe, validated schemas instantly using local `llama3.2:3b`.")
    
    with gr.Row():
        with gr.Column():
            input_box = gr.Textbox(
                label="Enter Natural Language API Description", 
                placeholder="e.g., Make a POST endpoint to create accounts. It needs a username string, password string, and age integer...",
                lines=5
            )
            submit_btn = gr.Button("Enforce JSON Schema Constraints", variant="primary")
            
        with gr.Column():
            output_box = gr.Code(label="Type-Safe JSON Output", language="json")
            
            # The Export Components
            export_btn = gr.Button("💾 Prepare Export File", variant="secondary")
            file_download_widget = gr.File(label="Download Generated Schema File", visible=False)
            
    # Connect generation logic
    submit_btn.click(fn=process_and_display, inputs=input_box, outputs=output_box)
    
    # Connect download workflow (Reveals the file widget automatically when ready)
    export_btn.click(
        fn=export_json_file, 
        inputs=output_box, 
        outputs=file_download_widget
    ).then(
        fn=lambda: gr.update(visible=True), 
        outputs=file_download_widget
    )

if __name__ == "__main__":
    demo.launch()
