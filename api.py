from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/add")
async def add_numbers(num1: float = Query(...), num2: float = Query(...)):
    try:
        result = num1 + num2
        return {"result": result}
    except ValueError:
        return JSONResponse(status_code=400, content={"error": "Invalid input. Please provide two numbers."})

