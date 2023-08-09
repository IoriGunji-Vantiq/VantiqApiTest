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
async def get_horoscope():
    zodiac_sign = ['牡羊座', '牡牛座', '双子座', '蟹座', '獅子座', '乙女座', '天秤座', '蠍座', '射手座', '山羊座', '水瓶座', '魚座']
    random_num = random.randint(0, 11)
    print(random_num)
    random_sign = zodiac_sign(random_num)
    print(random_sign)
    return random_sign

@app.post('/auth-area')
async def post_auth_area(request: Request):
    token = request.headers.get('Authorization', '')
    if(token == "vantiq-token"):
        return 'OK'
    else:
        return 'NG'
