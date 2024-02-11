from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from Summlytics.pipeline.prediction import PredictionPipeline

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def train(request: Response):
    try:
        os.system("python main.py")
        return Response("Training successful")
    except Exception as e:
        return Response(f"Training failed: {e}")


@app.post("/predict")
async def predict(text):
    try:
        pipeline = PredictionPipeline()
        response = pipeline.predict(text)
        return response
    except Exception as e:
        return Response(f"Prediction failed: {e}")
    
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))