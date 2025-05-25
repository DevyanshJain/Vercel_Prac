from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/")
async def get_marks(request: Request):
    # Get all 'name' query params (like ?name=X&name=Y)
    names = request.query_params.getlist("name")

    with open("marks.json") as f:
        data = json.load(f)

    data_dict = {item["name"]: item["marks"] for item in data}
    result = [data_dict.get(name, None) for name in names]

    return JSONResponse(content={"marks": result})
