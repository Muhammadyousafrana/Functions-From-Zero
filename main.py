from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from my_lib.bot import scrape
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


class Wiki(BaseModel):
    name: str


app = FastAPI()


@app.get("/")
async def home():
    return {"message": "hello"}


@app.post("/predict")
async def predict_story(wiki: Wiki):
    result = scrape(wiki.name)
    payload = {"wikipage:": result}
    json_compatible_data_item = jsonable_encoder(payload)
    return JSONResponse(content=json_compatible_data_item)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
