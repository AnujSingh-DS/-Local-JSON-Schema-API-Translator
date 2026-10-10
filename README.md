# 🚀 SchemaForge: Local AI JSON-Schema API Translation Harness

**SchemaForge** is an open-source model harness designed to bridge the gap between unstructured human developer ideas and type-safe, validated backend API specifications. 

Built entirely for privacy-focused and resource-constrained local development setups, SchemaForge forces tiny, lightweight open-weight models (like `llama3.2:3b`) to execute strict, deterministic **Constrained Decoding Loops**—completely bypassing the corporate cloud and guaranteeing structured JSON outputs every single time.

---

## 🏆 Hacktoberfest 2026 Submission Summary
- **Challenge Track:** Best Open-Source AI Project
- **Core Open Engine:** Ollama / Llama 3.2 (3B) [0]
- **Standard Alignment:** Implements deterministic schema enforcement architecture using localized Pydantic operational validations.
- **Hardware Profile:** Optimized to run fully on everyday developer laptops (tested smoothly on Intel Iris Xe / 16GB RAM setups) without requiring dedicated discrete graphics.

---

## ✨ Features
* **Zero-Cloud Architecture:** Your data never leaves your machine. Full parsing happens completely offline on your CPU via Ollama.
* **Guaranteed Structural Invariance:** Small language models usually struggle with rigid text formatting. SchemaForge leverages native JSON-schema injections directly into the token-decoding level to eliminate syntax errors.
* **Auto Type-Inference:** Intelligently maps natural text variables into systematic programming data structures (`string`, `int`, `float`, `boolean`).
* **Beautiful Interactive Dashboard:** Includes a clean, intuitive web interface to quickly prototype backend schema endpoints.

---

## 📊 System Architecture Flow
```text
[ Natural Language Text ] ──> [ SchemaForge Harness ] ──> [ Constrained Token Matrix ] ──> [ Pydantic Verification ] ──> [ Perfect Type-Safe JSON ]
```

---

## 🛠️ Getting Started & Installation

### Prerequisites
1. **Ollama:** Install the local runner from [ollama.com](https://ollama.com) [0]
2. **Model Base:** Pull the optimized lightweight engine:
   ```bash
   ollama pull llama3.2:3b
   ```

### 1. Clone the Project
```bash
git clone https://github.com
cd SchemaForge
```

### 2. Install Dependencies
```bash
pip install pydantic gradio
```

### 3. Run the Application
Ensure Ollama is running in your system background, then launch the ecosystem app:
```bash
python app.py
```
Open your browser and navigate to: `http://127.0.0.1:7860`

---

## 💡 Example Translation Matrix

### Unstructured Developer Requirement Input:
> *"Create a POST endpoint called checkout_basket. It must require an array of integers named item_ids, a coupon_code string parameter, and a total_price float. It doesn't require any API tokens or login to test."*

### SchemaForge Enforced Output:
```json
{
    "endpoint_name": "checkout_basket",
    "http_method": "POST",
    "required_parameters": [
        "item_ids",
        "coupon_code",
        "total_price"
    ],
    "auth_required": false,
    "inferred_data_types": {
        "item_ids": "array",
        "coupon_code": "string",
        "total_price": "float"
    }
}
```

---

## 📜 License
Distributed under the **MIT License**. See `LICENSE` for more information. All code complies with open-source development workflows.
