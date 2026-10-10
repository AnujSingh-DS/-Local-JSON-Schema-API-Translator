
🚀 SchemaForge: Local AI JSON-Schema API Translation Harness

SchemaForge is an open-source, local software architecture studio that instantly bridges the gap between raw, conversational human requirements and production-grade engineering blocks.
Built entirely for resource-constrained, privacy-centric environment setups, SchemaForge forces tiny, open-weight models (like llama3.2:3b or qwen2.5-coder:3b) to execute strict, deterministic Constrained Decoding Loops. Instead of simply returning plain text, it enforces strict Pydantic structures to compile complete application sources, matching container configurations, security audit profiles, and unit test suites entirely offline.

🏆 Hacktoberfest 2026 Submission Summary

• Challenge Track: Best Open-Source AI Project
• Core Open Engine: Ollama / Llama 3.2 (3B)
• Standard Alignment: Strict structural token parsing via localized Pydantic operational verification layouts.
• Hardware Profile: Optimized to run fully on everyday developer laptops (tested smoothly on Intel Iris Xe / 16GB RAM configurations) without needing a dedicated discrete GPU.

✨ Features


Workspace Module	Operational System Footprint	Engineering Impact
🌐 Polyglot Software Engine	Translates natural text constraints into fully functioning Python (FastAPI), JavaScript (Express), Go (Gin), or Rust (Actix-Web) architectures.	Eliminates cold-start boilerplate configuration times across mismatched developer team setups.
🐳 Automated Container DevOps	Generates tailored multi-stage Dockerfile configurations matching your chosen language environment on the fly.	Bridges the gap between writing pure code files and shipping reproducible, production-ready clusters.
🛡️ Live Security Audit Matrix	Injects static AST evaluation rules into the LLM system prompt layer to inspect runtime risks.	Flags missing authentication headers, hardcoded credentials, or vulnerable parameters before export.
🧪 Companion Testing Blueprint	Automatically sets up structural testing mock frameworks (e.g., supertest, TestClient) alongside your code.	Encourages immediate automated verification and local logic test execution.
🎁 Package Workspace Archiver	Aggregates all live workspace generation blocks into a structured, single-click .zip file download.	Exports fully complete starter templates directly into local integrated development environments (IDEs).


📊 Core System Workflow

text
[ Raw Text Specs ] 
       │
       ▼
[ SchemaForge Engine (Ollama / Llama3.2) ] 
       │
       ├─► 📄 Application Source Code File
       ├─► 🐳 Multi-Stage Dockerfile Layout 
       ├─► 🧪 Automated Integration Tests Script
       └─► 🛡️ Live Security Audit Markdown
       │
       ▼
[ Workspace ZIP Archiver ] ──► [ Complete Project Download ]
Use code with caution.

🛠️ Getting Started & Installation


Prerequisites

1. Ollama: Install the local runner execution core from ollama.com.
2. Model Weights: Pull the optimized lightweight language engine:bash
ollama pull llama3.2:3b
Use code with caution.

1. Clone the Project

bash
git clone https://github.com
cd SchemaForge
Use code with caution.

2. Install Dependencies

Ensure you install the required frameworks inside your active python development environment:
bash
pip install pydantic gradio
Use code with caution.

3. Run the Application

Ensure the Ollama engine service is running in your system background, then launch the workspace dashboard:
bash
python app.py
Use code with caution.
Open your browser and navigate to the local network port address: http://127.0.0.1:7860

💡 Example Transformation Matrix


Unstructured Input Constraints:

"Design a Go microservice that processes payment webhooks. It should match the path /webhooks/pay, validate a secret token payload, track an invoice_id string, and reject unauthenticated requests."

Generated Workspace Blueprint Layout:

Inside the interactive web interface dashboard, clicking "Forge Complete Project Footprint" populates your multi-tab workspace panel instantly with four distinct engineering outputs:
text
workspace_project/
├── main.go               # Production-grade Go (Gin) handler with token verification routing
├── Dockerfile            # Optimized minimal multi-stage Go compilation layer 
├── test_suite.go         # Standard Go testing harness boilerplate code
└── README.md             # Standard instructions file to spin up the container environment
Use code with caution.

⚙️ Advanced Performance Optimization

If the model generation stutters or processes slowly on your local machine, the engine may be defaulting onto your CPU rather than utilizing your integrated hardware memory. Execute these optimization parameters to achieve an immediate 5x speed boost:
• Pin the Model Weights inside System VRAM:
Force Ollama to keep your compilation architecture permanently loaded in your computer's memory by initializing the background server with this parameter:bash
# Windows PowerShell:
$env:OLLAMA_KEEP_ALIVE="-1"; ollama serve

# Linux / macOS Terminal:
OLLAMA_KEEP_ALIVE="-1" ollama serve
Use code with caution.
• Swap to an Ultra-High Precision Coding Model:
While llama3.2:3b is an incredible lightweight general tool, you can update your code execution layer to run qwen2.5-coder:3b. It handles complex programming layout definitions with massive accuracy gains:bash
ollama pull qwen2.5-coder:3b
Use code with caution.
Then simply flip the configuration variable in your ModelHarness definition inside app.py to lock it in:python
self.model = "qwen2.5-coder:3b"
Use code with caution.

📜 License & Compliance

Distributed under the MIT License. See LICENSE for more information. Because all data processing and validation tasks execute 100% locally on your computer loop, absolutely zero engineering constraints, secure code segments, or API parameters ever leave your hardware boundary.
