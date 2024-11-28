
## 動機

webアプリを制作したいと思い、それに伴いwebAPIの作成の練習を行った。

## 目標

簡易的なAPIを作成し、リクエストを受けて返すということを目標にしている。

## システム概要

リクエストで受け取った２つの数字の引数を足した結果を返り値とする


## APIコーディング概要（おまけでエラー処理も実装した）
```python
@app.get("/add")
async def add_numbers(num1: float = Query(...), num2: float = Query(...)):
    try:
        result = num1 + num2
        return {"result": result}
    except ValueError:
        return JSONResponse(status_code=400, content={"error": "Invalid input. Please provide two numbers."})
```


## リクエスト送信&レスポンス

```bash
curl "http://127.0.0.1:8000/add?num1=10&num2=20"


StatusCode        : 200
StatusDescription : OK
Content           : {"result":30.0}
RawContent        : HTTP/1.1 200 OK
                    Content-Length: 15
                    Content-Type: application/json
                    Date: Thu, 28 Nov 2024 01:31:13 GMT
                    Server: uvicorn

                    {"result":30.0}
Forms             : {}
Headers           : {[Content-Length, 15], [Content-Type, application/json], [Date, Thu, 28 Nov 2024 01:31:13 GMT], [Server, uvicorn]}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 15
```

