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
    # X-Line-Signature ヘッダーの値を取得
    # signature = request.headers.get('X-Line-Signature', '')

    # request body から event オブジェクトを取得
    # events = line_parser.parse((await request.body()).decode('utf-8'), signature)

    # 各イベントの処理（※1つの Webhook に複数の Webhook イベントオブジェっｚクトが含まれる場合あるため）
    # for event in events:
    #     if event.type != 'message':
    #         continue
    #     if event.message.type != 'text':
    #         continue

    #     # LINE パラメータの取得
    #     line_user_id = event.source.user_id
    #     line_message = event.message.text

    #     # ChatGPT からトークデータを取得
    #     response = openai.ChatCompletion.create(
    #         model = 'gpt-3.5-turbo'
    #         , temperature = 0.5
    #         , messages = [
    #             {
    #                 'role': 'system'
    #                 , 'content': OPENAI_CHARACTER_PROFILE.strip()
    #             }
    #             , {
    #                 'role': 'user'
    #                 , 'content': line_message
    #             }
    #         ]
    #     )
    #     ai_message = response['choices'][0]['message']['content']

    # LINE Webhook サーバーへ HTTP レスポンスを返す
    return 'ok'