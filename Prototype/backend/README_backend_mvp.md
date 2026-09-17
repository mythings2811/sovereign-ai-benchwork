# API-backed evaluation backend

The live startup script runs `backend_mvp.py` on `http://127.0.0.1:8000`.

## Configure (bash/zsh)
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export LLM_API_KEY="YOUR_PROVIDER_KEY"
export LLM_BASE_URL="https://api.openai.com/v1"
export LLM_MODEL_GENERAL="gpt-4o-mini"
export LLM_MODEL_REASONING="gpt-4o-mini"
uvicorn backend_mvp:app --host 127.0.0.1 --port 8000 --reload
```

For Windows PowerShell:
```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:LLM_API_KEY=""
$env:LLM_BASE_URL="https://api.openai.com/v1"
$env:LLM_MODEL_GENERAL="gpt-4o-mini"
$env:LLM_MODEL_REASONING="gpt-4o-mini"
$env:LLM_TIMEOUT_SECONDS="60"
$env:W2_MAX_UPLOAD_BYTES="26214400"
$env:W2_VISION_ENABLED="false"
$env:LLM_MODEL_VISION=""
uvicorn backend_mvp:app --host 127.0.0.1 --port 8000 --reload
```

Open `http://127.0.0.1:8000/docs` to inspect/test endpoints.

## Important prototype limitations
- W3 calls an OpenAI-compatible Chat Completions API. Configure provider base URL and model IDs using environment variables.
- The included knowledge entries are synthetic demonstration seeds; retrieval is keyword matching, not uploaded-file ingestion or a vector database.
- W2 accepts PDF, PNG, JPG, and JPEG files at `POST /api/v1/workflows/w2/analyze`. The default PDF path is local: it validates the file and extracts embedded text and tag-like identifiers with page evidence. Scanned PDFs return a needs-OCR warning because no OCR engine is bundled.
- Image analysis is disabled unless `W2_VISION_ENABLED=true`, `LLM_MODEL_VISION` is set to a model that actually supports image input, and the configured provider accepts OpenAI-compatible vision messages. When enabled, image bytes are sent to that external provider; this is not local-only processing.
- W5 remains blocked for non-developer roles and code execution is disabled.
- API requests transmit the user query and retrieved passages to the configured provider. Use only approved non-sensitive evaluation data.
- The model names are examples; set them to model IDs available to your chosen provider.

## W2 testing

Install the requirements and run `pytest -q` from `Prototype/backend`. The test suite uses local PDF/image fixtures and mocks provider calls; it does not require a paid API key. For a manual test, open `Prototype/index.html` from an allowed frontend origin, select a supported file in W2, and choose **Analyze File**.
