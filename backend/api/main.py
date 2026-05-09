import os
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from backend.orchestration.workflow import graph
from backend.services.multimodal_service import extract_text_from_invoice

app = FastAPI()

static_dir = os.path.join(os.path.dirname(__file__), "..", "static")
app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")


@app.post("/analyze")
async def analyze(data: dict):
    result = graph.invoke({
        "shipment_data": data.get("shipment_data", ""),
        "supplier_data": data.get("supplier_data", ""),
    })
    return JSONResponse(content=result)


@app.post("/invoice")
async def invoice_upload(file: UploadFile = File(...)):
    file_location = os.path.join(os.path.dirname(__file__), "..", "static", file.filename)
    with open(file_location, "wb") as f:
        f.write(await file.read())

    text = extract_text_from_invoice(file_location)
    return {"extracted_text": text}
