{"filter":false,"title":"slack_test_sports.py","tooltip":"/chatbot/slack_test_sports.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":10,"column":48},"action":"insert","lines":["import config","import re","import random","import boto3","from slack_bolt import App","from slack_bolt.adapter.socket_mode import SocketModeHandler","from slack_sdk import WebClient","from slack_sdk.errors import SlackApiError","","app = App(token=config.bot_token)","slack_client = WebClient(token=config.bot_token)"],"id":1}],[{"start":{"row":12,"column":0},"end":{"row":51,"column":20},"action":"insert","lines":["@app.message(re.compile(\"맛집\"))","def all_store_info(message, say):","    say('안녕하세요 해운대 맛집 리스트를 추천해드리겠습니다 :)')","    # DynamoDB 리소스 생성","    dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2') # 서울 리전의 코드(ap-northeast-2)로 설정","    ","    # 테이블 정보 설정","    table_name = 'KHU_CAMTA_022' # 테이블 이름","    # partition_key = 'store_id' # 파티션 키","    ","    # DynamoDB 테이블 가져오기","    table = dynamodb.Table(table_name)","    ","    # 데이터 조회","    response = table.scan()","    items = response['Items']","    ","    message = \"\"","    for item in items:","        store_id = item['store_id']","        title = item['title']","        category = item['category']","        url = item['url']","        ","        # 선택된 음식점 정보 출력","        message = {","            \"blocks\": [","                {","                    \"type\": \"section\",","                    \"text\": {","                        \"type\": \"mrkdwn\",","                        \"text\": f\"*맛집명:* {title}\\n*카테고리:* {category}\\n*자세히보기:*<{url}|링크>\"","                    }","                },","                {","                    \"type\": \"divider\"","                }","            ]","        }","        say(message)"],"id":3}],[{"start":{"row":10,"column":48},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":11,"column":0},"end":{"row":12,"column":0},"action":"insert","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":10,"column":48},"end":{"row":10,"column":48},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":14,"mode":"ace/mode/python"}},"timestamp":1689660716408,"hash":"2d1c40d20b148d586597f0ae3a2c064e22056d6d"}