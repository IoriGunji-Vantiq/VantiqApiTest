import datetime
import random
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
        , "request": {
            "body": await request.body()
        }
    }
    return response

@app.get('/horoscope')
async def get_horoscope(month = 0):
    zodiac_sign = ['牡羊座', '牡牛座', '双子座', '蟹座', '獅子座', '乙女座', '天秤座', '蠍座', '射手座', '山羊座', '水瓶座', '魚座']
    result_sign = ''
    if(1 <= int(month) and int(month) <= 12):
        result_sign = zodiac_sign[int(month) - 1]
    else:
        result_sign = zodiac_sign[random.randint(0, 11)]
    return result_sign

@app.get('/auth-area')
async def get_auth_area(request: Request):
    token = request.headers.get('Authorization', '')
    if(token == "vantiq-token"):
        return 'Get OK'
    else:
        return 'Get NG'

@app.post('/auth-area')
async def post_auth_area(request: Request):
    token = request.headers.get('Authorization', '')
    if(token == "vantiq-token"):
        return 'Post OK'
    else:
        return 'Post NG'

@app.put('/anything')
async def put_anything(request: Request):
    token = request.headers.get('Authorization', '')
    if(token == "vantiq-token"):
        return 'Put OK'
    else:
        return 'Put NG'
