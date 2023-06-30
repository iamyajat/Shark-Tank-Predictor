import os
from os.path import join, dirname
from dotenv import load_dotenv
from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

import model


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

PORT = int(os.getenv("PORT", 8000))
DEV = bool(os.getenv("DEV", False))
WORKERS = int(os.getenv("WORKERS", 1))

app = FastAPI(title="Shark Tank India Predictor API", version="0.1.0",
              description="API for Shark Tank India Predictor")
app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=Response)
async def root(request: Request) -> Response:
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/predict", response_class=RedirectResponse)
async def predict(req: Request) -> Response:
    body = req.query_params
    data = [[body["ask_amount"], body["ask_equity"], body["ask_valuation"]]]
    if "probabilities" in body.keys() and bool(body["probabilities"]):
        p = model.predict_proba(data)
        return templates.TemplateResponse("result.html", {"request": req,
                                                          "prediction": round(p[0][1], 2)})
    p = model.predict(data)
    return HTMLResponse(status_code=200, content=p[0])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=PORT,
                reload=DEV, workers=WORKERS)
