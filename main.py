from fastapi import FastAPI
import model


app = FastAPI(title="Shark Tank India Predictor API", version="0.1.0", description="API for Shark Tank India Predictor")


@app.get("/")
async def root():
    return {"message": "Up and running!"}

@app.get("/predict")
async def predict(ask_amount: int, ask_equity:int, ask_valuation: int, probabilities: bool = False):
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

