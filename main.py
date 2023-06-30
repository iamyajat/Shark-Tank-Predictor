import os
from os.path import join, dirname
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from dotenv import load_dotenv
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


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})


@app.post("/predict")
async def predict(ask_amount: int, ask_equity: int, ask_valuation: int, probabilities: bool = False):
    data = [[ask_amount, ask_equity, ask_valuation]]
    if probabilities:
        p = model.predict_proba(data)
        return {
            "deal": p[0][1],
            "no_deal": p[0][0]
        }
    p = model.predict(data)
    return {
        "deal": bool(p[0])
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=PORT,
                reload=DEV, workers=WORKERS)
