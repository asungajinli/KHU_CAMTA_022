import config
import re
import random
import boto3
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

app = App(token=config.bot_token)
slack_client = WebClient(token=config.bot_token)

@app.event("app_mention")  # 앱을 언급했을 때
def who_am_i(event, client, message, say):
    print('event:', event)
    print('client:', client)
    print('message:', message)
    say(f'hello! <@{event["user"]}>')
    
@app.message(re.compile("맛집"))
def all_store_info(message, say):
    say('안녕하세요 해운대 맛집 리스트를 추천해드리겠습니다 :)')
    # DynamoDB 리소스 생성
    dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2') # 서울 리전의 코드(ap-northeast-2)로 설정
    
    # 테이블 정보 설정
    table_name = 'KHU_CAMTA_022' # 테이블 이름
    # partition_key = 'store_id' # 파티션 키
    
    # DynamoDB 테이블 가져오기
    table = dynamodb.Table(table_name)
    
    # 데이터 조회
    response = table.scan()
    items = response['Items']
    
    message = ""
    for item in items:
        store_id = item['store_id']
        title = item['title']
        category = item['category']
        url = item['url']
        
        # 선택된 음식점 정보 출력
        message = {
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*맛집명:* {title}\n*카테고리:* {category}\n*자세히보기:*<{url}|링크>"
                    }
                },
                {
                    "type": "divider"
                }
            ]
        }
        say(message)
        
        

@app.message(re.compile("추천"))
def regex(message, say):
    say('안녕하세요 해운대 맛집 추천해드리겠습니다 :) ')
    # DynamoDB 리소스 생성
    dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')  # 서울 리전의 코드(ap-northeast-2)로 설정
    
    # 테이블 정보 설정
    table_name = 'KHU_CAMTA_022'  # 테이블 이름
    partition_key = 'store_id'  # 파티션 키
    
    # DynamoDB 테이블 가져오기
    table = dynamodb.Table(table_name)
    
    # 데이터 조회
    response = table.scan()
    items = response['Items']
    
    # 랜덤하게 음식점 선택
    selected_item = random.choice(items)
    
    # 선택된 음식점 정보 출력
    store_id = selected_item[partition_key]
    title = selected_item['title']
    category = selected_item['category']
    url = selected_item['url']
    
    # 선택된 음식점 정보 출력
    message = {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*맛집 추천!* :star:\n\n*맛집명:* {title}\n*카테고리:* {category}\n*자세히보기:*<{url}|링크>"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "다른 음식점 추천받기"
                        },
                        "style": "primary",
                        "action_id": "recommend_another"
                    }
                ]
            }
        ]
    }

    say(message)
    
    
@app.action("recommend_another")
def recommend_another(ack, body, say):
    ack()
    
    dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')
    table_name = 'KHU_CAMTA_022'
    partition_key = 'store_id'
    table = dynamodb.Table(table_name)
    
    response = table.scan()
    items = response['Items']
    
    selected_item = random.choice(items)
    
    store_id = selected_item[partition_key]
    title = selected_item['title']
    category = selected_item['category']
    url = selected_item['url']
    
    message = {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*맛집 추천!* :star:\n\n*맛집명:* {title}\n*카테고리:* {category}\n*자세히보기:*<{url}|링크>"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "다른 음식점 추천받기"
                        },
                        "style": "primary",
                        "action_id": "recommend_another"
                    }
                ]
            }
        ]
    }

    say(message)
    
if __name__ == '__main__':
    SocketModeHandler(app, config.app_token).start()