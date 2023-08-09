import datetime
from fastapi import FastAPI, Request

app = FastAPI()

@app.get('/')
async def get_root():
    response = {
        "message": "Hello, world!"
        , "timestamp": datetime.datetime.now()
    }
    return response

@app.post('/')
async def post_root(request: Request):
    response = {
        "message": "Hello, world!"
        , "timestamp": datetime.datetime.now()
        , "request_body": (await request.body()).decode('utf-8')
    }
    return response
