  # 🛠️ Agent Skill Manifest: API Schema Transformer

  This file provides a standardized specification for the **SchemaForge API Translation Skill**, adhering to the principles of the **Agent Skill Open Standard**. It defines how autonomous agent networks can invoke this tool to translate unstructured natural language requirements into strict, type-safe JSON objects.

  ---

  ## 📌 Skill Metadata

  | Attribute | Specification |
  | :--- | :--- |
  | **Skill Name** | `api_schema_transformer` |
  | **Version** | `1.0.0` |
  | **Description** | Transforms unstructured developer text descriptions into type-safe, validated backend API payloads. |
  | **Core Engine** | `llama3.2:3b` (Constrained token decoding mode) |
  | **Output Constraints** | Strict JSON Schema Compliance via Pydantic mapping |

  ---

  ## ⚡ Execution Interface

  ### 1. Expected Skill Input (Parameters)
  The skill expects a natural language prompt defining a desired backend routing mechanism.

• Parameter Name: user_prompt
	• Type: string
	• Description: The unstructured text description detailing microservice functionality, database integration, validation rules, paths, or variables.
	• Example: "Design a Python FastAPI router engine that handles user registration profile updates on path /register. The logic must take a username string and check if age is over 18."
• Parameter Name: target_language
	• Type: string
	• Enum: ["Python (FastAPI)", "JavaScript (Express)", "Go (Gin)", "Rust (Actix-Web)", "Java (Spring Boot)", "C++ (Crow)", "HTML/CSS/JS Web Blueprint"]
	• Description: The environment configuration target engine chosen to compile and deploy the source script.


  ### 2. Guaranteed Skill Output (JSON Schema)
  The skill intercepts the local LLM matrix and guarantees an output strictly mirroring this structural layout:

  ```json
  {
  "$schema": "https://json-schema.org",
  "title": "UltimateCodeBlueprint",
  "type": "object",
  "properties": {
    "target_language": {
      "type": "string",
      "description": "The programming language selected to build the runtime."
    },
    "inferred_framework": {
      "type": "string",
      "description": "The most optimal standard framework name determined for the context (e.g., Gin, FastAPI)."
    },
    "generated_code": {
      "type": "string",
      "description": "The complete, syntax-accurate primary backend microservice source code."
    },
    "suggested_filename": {
      "type": "string",
      "description": "The native file name with the appropriate language extension (e.g., main.go, app.py)."
    },
    "dockerfile_contents": {
      "type": "string",
      "description": "A production-ready, multi-stage Dockerfile optimized to containerize this source code block."
    },
    "security_audit_report": {
      "type": "string",
      "description": "A thorough markdown security checklist detailing vulnerability reviews, missing auth validations, or threat mitigations."
    }
  },
  "required": [
    "target_language", 
    "inferred_framework", 
    "generated_code", 
    "suggested_filename", 
    "dockerfile_contents", 
    "security_audit_report"
  ]
}

  ---

  ## 🧪 Validated Operational Example

  Agent Invocation Request Context:

  json
  {
    "target_language": "Go (Gin)",
    "user_prompt": "Design a high-performance Go Gin endpoint on path /telemetry that captures live analytics logs. It accepts device_id string, CPU_load float, and memory_bytes integer variables."
  }

  ### Agent Invocation Context:
  ```text
  "Create a POST route named user_registration. It needs an email string, password string, and age integer. Must require authentication token header."
  ```

  ### Deterministic Resulting State:
  ```json
  {
      "endpoint_name": "user_registration",
      "http_method": "POST",
      "required_parameters": [
          "email",
          "password",
          "age"
      ],
      "auth_required": true,
      "inferred_data_types": {
          "email": "string",
          "password": "string",
          "age": "int"
      }
  }
  ```

  ---

  ## 🛡️ Error & Boundary States
  * **Connection Failures:** Returns a structural error payload if the local Ollama background execution loop is unreachable (`503 Service Unavailable`).
  * **Validation Anomalies:** If the generated tokens do not match the expected constraints, the harness automatically fails open, rejecting standard string anomalies to protect data processing flows.
