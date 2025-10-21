from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from sentiment_service import load_model, predict_sentiments

app = FastAPI(title="Sentiment Analysis API", version="1.0")

@app.on_event("startup")
def startup_event():
    load_model()

# Define request and response
class SentimentRequest(BaseModel):
    message: list[str]

class SentimentResponse(BaseModel):
    message: str
    label: str
    confidence: float

@app.get("/")
def root():
    return {"message": "Sentiment Analysis API is running!"}


@app.post("/predict-sentiment", response_model=list[SentimentResponse])
def predict_sentiment(req: SentimentRequest):
    return predict_sentiments(req.message)


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)
