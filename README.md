-API-

webアプリを制作したいと思い、今までやってこなかったwebAPIの作成の練習を行った。簡易的なAPIを作成し、リクエストを受けて返すということを目標にしている。

```python
@app.get("/add")
async def add_numbers(num1: float = Query(...), num2: float = Query(...)):
    try:
        result = num1 + num2
        return {"result": result}
    except ValueError:
        return JSONResponse(status_code=400, content={"error": "Invalid input. Please provide two numbers."})

