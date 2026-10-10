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

* **Parameter Name:** `user_prompt`
* **Type:** `string`
* **Description:** The text explanation of the API endpoint, HTTP method, required inputs, data types, and authentication rules.
* **Example:** *"Make a GET endpoint called fetch_profile that requires a user_id string and a bearer authentication token."*

### 2. Guaranteed Skill Output (JSON Schema)
The skill intercepts the local LLM matrix and guarantees an output strictly mirroring this structural layout:

```json
{
  "$schema": "https://json-schema.org",
  "title": "ApiPayloadBlueprint",
  "type": "object",
  "properties": {
    "endpoint_name": {
      "type": "string",
      "description": "The semantic slug name of the action, lowercase with underscores."
    },
    "http_method": {
      "type": "string",
      "enum": ["GET", "POST", "PUT", "DELETE", "PATCH"],
      "description": "The determined standard HTTP verb execution layer."
    },
    "required_parameters": {
      "type": "array",
      "items": { "type": "string" },
      "description": "List of parameter keys parsed from the text description."
    },
    "auth_required": {
      "type": "boolean",
      "description": "True if the request explicitly mentions tokens, keys, passwords, or authentication."
    },
    "inferred_data_types": {
      "type": "object",
      "description": "Key-value mapping of parameters to their expected standard types."
    }
  },
  "required": ["endpoint_name", "http_method", "required_parameters", "auth_required", "inferred_data_types"]
}
```

---

## 🧪 Validated Operational Example

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
