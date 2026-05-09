# Local AI Agent Backend

## Setup

1. Create and activate a Python environment.
2. Install dependencies:

```bash
python -m pip install -r backend/requirements.txt
```

3. Make sure Tesseract OCR is installed on your machine and available in PATH.

## Run the server

From the workspace root:

```bash
uvicorn backend.api.main:app --reload
```

Then open:

- `http://127.0.0.1:8000/`

## Features

- `POST /analyze` — runs the risk, negotiation, and executive summary workflow.
- `POST /invoice` — uploads an invoice image and extracts OCR text.

## Notes

- The local LLM uses `Qwen/Qwen2.5-7B-Instruct`.
- If CUDA is available, it loads on GPU; otherwise it falls back to CPU.
- Ensure enough system memory if running a 7B model locally.
