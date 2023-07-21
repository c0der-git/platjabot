from fastapi import FastAPI, HTTPException, Response
from typing import List
from models import Beach

# Temporary storage for the data (Replace this with a proper database)
database = []

app = FastAPI(debug=True)

@app.get("/platja/", response_model=List[Beach])
async def get_all_beaches():
    if not database:
        return Response(content="No Content", status_code=204)
    return database

@app.get("/platja/{platjaId}", response_model=Beach)
async def get_beach_by_id(platjaId: str):
    for beach in database:
        if beach.codiPlatja == platjaId:
            return beach
    raise HTTPException(status_code=404, detail="Beach not found")

@app.post("/platja/", response_model=Beach)
async def create_beach(beach: Beach):
    try:
        database.append(beach)
        return beach
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to add beach entry")