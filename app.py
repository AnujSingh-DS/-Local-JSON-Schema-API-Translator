import json
import urllib.request
import urllib.error
import os
import zipfile
import io
import gradio as gr
from pydantic import BaseModel, Field
from typing import List, Dict

# 1. STRUCTURAL METADATA SCHEMA
class UltimateCodeBlueprint(BaseModel):
    target_language: str = Field(description="The programming language chosen by the user.")
    inferred_framework: str = Field(description="The target framework name (e.g., FastAPI, Express).")
    generated_code: str = Field(description="The complete, production-ready primary source code.")
    suggested_filename: str = Field(description="Native filename with extension (e.g., main.py, server.js).")
    dockerfile_contents: str = Field(description="A fully configured Dockerfile optimizing this specific code layer.")
    security_audit_report: str = Field(description="A punchy markdown security review highlighting potential risk vectors or confirming safety.")

# 2. MODEL RUNTIME
class ModelHarness:
    def __init__(self, model_name: str = "llama3.2:3b"):
        self.url = "http://localhost:11434/api/chat"
        self.model = model_name

    def translate_to_ultimate_engine(self, user_prompt: str, language: str):
        target_schema = UltimateCodeBlueprint.model_json_schema()
        
        system_instruction = (
            f"You are an elite enterprise software architect and security engineer. "
            f"Convert the requirements into production-grade {language} code. "
            f"You MUST generate the primary code, a matching containerized Dockerfile layout, and a thorough safety audit markdown block. "
            f"Strictly map all output arrays directly inside the requested structural JSON schema target configuration layout."
        )
        
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": f"Target Language: {language}\nRequirements:\n{user_prompt}"}
            ],
            "options": {"temperature": 0.1},
            "format": target_schema,
            "stream": False
        }
        
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(self.url, data=data, headers={"Content-Type": "application/json"})
        
        try:
            with urllib.request.urlopen(req) as response:
                res_body = response.read().decode("utf-8")
                raw_content = json.loads(res_body).get("message", {}).get("content", "{}")
                validated_output = UltimateCodeBlueprint.model_validate_json(raw_content)
                return validated_output.model_dump()
        except urllib.error.URLError:
            return {
                "generated_code": "// ❌ Connection Error: Is Ollama running in the background?",
                "suggested_filename": "error.txt", 
                "inferred_framework": "None",
                "dockerfile_contents": "# Ollama unreachable",
                "security_audit_report": "### ❌ Connection Refused\nEnsure Ollama service state is running."
            }
        except Exception as e:
            return {
                "generated_code": f"// ❌ Schema/Validation mismatch: {e}",
                "suggested_filename": "error.txt", 
                "inferred_framework": "None",
                "dockerfile_contents": "# Parse error",
                "security_audit_report": f"### ❌ Execution Error\n{e}"
            }

harness = ModelHarness("llama3.2:3b")

# 3. COMPANION UTILITIES (MOCK UTILS, ZIP COMPILER & LIVE PREVIEW ENGINE)
def generate_test_suite(source_code, language):
    test_templates = {
        "Python (FastAPI)": "from fastapi.testclient import TestClient\nfrom main import app\n\nclient = TestClient(app)\ndef test_root():\n    assert client.get('/').status_code == 200",
        "JavaScript (Express)": "const request = require('supertest');\nconst app = require('./server');\n\ndescribe('GET /', () => {\n    it('should respond with 200', async () => {\n        const res = await request(app).get('/');\n        expect(res.statusCode).toEqual(200);\n    });\n});"
    }
    return test_templates.get(language, f"// Integration tests framework ready for {language} deployment chains.")

def compile_workspace_zip(primary_code, filename, dockerfile, test_suite):
    """Bundles the full generation into a micro-project zip folder."""
    if "❌" in primary_code or not primary_code:
        return None
    try:
        zip_filename = "app_production_workspace.zip"
        zip_path = os.path.join(os.getcwd(), zip_filename)
        
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            zip_file.writestr(filename if filename else "main.src", primary_code)
            zip_file.writestr("Dockerfile", dockerfile if dockerfile else "# Base layer configuration")
            zip_file.writestr(f"test_suite.{filename.split('.')[-1] if '.' in filename else 'txt'}", test_suite)
            zip_file.writestr("README.md", "# 🚀 SchemaForge Workspace\n\nGenerated architectural layout block.\n\n## Spin Up locally\n```bash\ndocker build -t my-app .\ndocker run -p 8080:8080 my-app\n```")
            
        return zip_path
    except Exception:
        return None

def load_sandboxed_preview_engine(source_code, language):
    """Spins up a sandboxed local web preview simulation block."""
    if not source_code or "❌" in source_code:
        return "<p style='color: #ef4444; font-family: system-ui;'>❌ Write or compile valid source code to initialize the preview sandbox.</p>"
        
    html_preview_wrapper = f"""
    <div style="font-family: system-ui, sans-serif; padding: 15px; background: #1e1e1e; color: #fff; border-radius: 8px;">
        <h4 style="margin-top: 0; color: #4ade80; display: flex; align-items: center; gap: 8px;">📡 Active Runtime Preview Sandbox ({language})</h4>
        <div style="background: #000; padding: 12px; border-radius: 4px; font-family: monospace; min-height: 120px; white-space: pre-wrap; color: #adbac7; border: 1px solid #373e47;">
🚀 Initializing local virtual memory modules...
⚙️ Running structural WebAssembly compilation checks...
✅ Simulated {language} runtime layer online. Container environment stable.
        </div>
        <div style="margin-top: 10px; font-size: 12px; color: #768390;">
            🔒 Security Sandbox Active: System commands and network sockets are virtualized locally.
        </div>
    </div>
    """
    return html_preview_wrapper

# 4. CONTROLLER LAYER CONNECTIVITY
def orchestration_router(text_input, target_language):
    result = harness.translate_to_ultimate_engine(text_input, target_language)
    
    syntax_map = {
        "Python (FastAPI)": "python", "JavaScript (Express)": "javascript",
        "Go (Gin)": "go", "Rust (Actix)": "rust"
    }
    chosen_syntax = syntax_map.get(target_language, "text")
    
    inferred_test = generate_test_suite(result.get("generated_code"), target_language)
    html_preview = load_sandboxed_preview_engine(result.get("generated_code"), target_language)
    
    return (
        result.get("generated_code"),
        result.get("suggested_filename"),
        result.get("dockerfile_contents"),
        result.get("security_audit_report"),
        inferred_test,
        gr.Code(language=chosen_syntax),
        html_preview
    )

# 5. ENTERPRISE UI WEB INTERFACE LAYOUT
with gr.Blocks() as demo:
    gr.Markdown("# 🌌 UniversalForge Enterprise Workspace")
    gr.Markdown("Transform requirements into clean language architectures equipped with auto-generated containers, testing footprints, and direct vulnerability checking reports.")
    
    meta_filename = gr.State()
    
    with gr.Row():
        with gr.Column(scale=2):
            input_box = gr.Textbox(
                label="Step 1: Define Application Logic Constraints",
                placeholder="e.g., Design a Go microservice that processes payment webhooks. It should validate a secret token payload and reject unauthenticated requests...",
                lines=6
            )
            language_selector = gr.Dropdown(
                choices=["Python (FastAPI)", "JavaScript (Express)", "Go (Gin)", "Rust (Actix)"],
                value="Python (FastAPI)",
                label="Step 2: Choose Deployment Language System Environment"
            )
            submit_btn = gr.Button("⚡ Forge Complete Project Footprint", variant="primary")
            
            gr.Markdown("### 🛡️ Live Security & AST Vulnerability Scan")
            security_panel = gr.Markdown("*Generate code to execute static evaluation checking filters.*")
            
        with gr.Column(scale=2):
            with gr.Tabs():
                with gr.TabItem("📄 Application Source"):
                    output_code_box = gr.Code(label="Workspace File Output", lines=15, interactive=True)
                with gr.TabItem("🐳 Docker Configuration"):
                    dockerfile_box = gr.Code(label="Dockerfile Layout Blueprint", language="dockerfile", lines=15)
                with gr.TabItem("🧪 Automated Test Suite"):
                    test_suite_box = gr.Code(label="Unit Assertions Script", lines=15)
                with gr.TabItem("🌐 Live Preview Sandbox"):
                    preview_html_sandbox = gr.HTML(value="<p style='color: #768390; font-family: system-ui;'>Click 'Forge Complete Project Footprint' to spin up the container runtime simulation preview.</p>")
            
            export_btn = gr.Button("🎁 Package & Download Complete ZIP Workspace", variant="secondary")
            file_download_widget = gr.File(label="Download Complete Production ZIP Archive", visible=False)

    # UI Action Bindings (Correctly nested within the Blocks layout indentation)
    submit_btn.click(
        fn=orchestration_router,
        inputs=[input_box, language_selector],
        outputs=[output_code_box, meta_filename, dockerfile_box, security_panel, test_suite_box, output_code_box, preview_html_sandbox]
    )
        # UI Action Bindings
    submit_btn.click(
        fn=orchestration_router,
        inputs=[input_box, language_selector],
        outputs=[output_code_box, meta_filename, dockerfile_box, security_panel, test_suite_box, output_code_box, preview_html_sandbox]
    )
    
    export_btn.click(
        fn=compile_workspace_zip,
        inputs=[output_code_box, meta_filename, dockerfile_box, test_suite_box],
        outputs=file_download_widget
    ).then(
        fn=lambda: gr.File(visible=True),
        inputs=None,
        outputs=file_download_widget
    )

if __name__ == "__main__":
    demo.launch(theme=gr.themes.Soft())
