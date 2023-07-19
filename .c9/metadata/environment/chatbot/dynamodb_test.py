{"filter":false,"title":"dynamodb_test.py","tooltip":"/chatbot/dynamodb_test.py","undoManager":{"mark":6,"position":6,"stack":[[{"start":{"row":0,"column":0},"end":{"row":30,"column":11},"action":"insert","lines":["dimport boto3","","# DynamoDB 리소스 생성","dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')  # 서울 리전의 코드(ap-northeast-2)로 설정","","# 테이블 정보 설정","table_name = 'test'  # 테이블 이름","partition_key = 'store_id'  # 파티션 키","","# DynamoDB 테이블 가져오기","table = dynamodb.Table(table_name)","","# 데이터 조회","response = table.scan()","items = response['Items']","","# store_id를 기준으로 오름차순으로 정렬","sorted_items = sorted(items, key=lambda x: x[partition_key])","","# 정렬된 데이터 출력","for item in sorted_items:","    store_id = item[partition_key]","    title = item['title']","    category = item['category']","    url = item['url']","    ","    print(f\"Store ID: {store_id}\")","    print(f\"Store Name: {title}\")","    print(f\"Category: {category}\")","    print(f\"URL: {url}\")","    print()"],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["d"],"id":2}],[{"start":{"row":6,"column":14},"end":{"row":6,"column":18},"action":"remove","lines":["test"],"id":3},{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"insert","lines":["K"]},{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"insert","lines":["H"]},{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"insert","lines":["U"]},{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"insert","lines":["_"]},{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"insert","lines":["0"]},{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"insert","lines":["2"]},{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"insert","lines":["2"]},{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"insert","lines":["_"]}],[{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"remove","lines":["_"],"id":4},{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"remove","lines":["2"]},{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"remove","lines":["2"]},{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"remove","lines":["0"]}],[{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"insert","lines":["C"],"id":5},{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"insert","lines":["A"]},{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"insert","lines":["<"]},{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"insert","lines":["T"]}],[{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"remove","lines":["T"],"id":6},{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"remove","lines":["<"]}],[{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"insert","lines":["M"],"id":7},{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"insert","lines":["T"]},{"start":{"row":6,"column":22},"end":{"row":6,"column":23},"action":"insert","lines":["A"]},{"start":{"row":6,"column":23},"end":{"row":6,"column":24},"action":"insert","lines":["_"]},{"start":{"row":6,"column":24},"end":{"row":6,"column":25},"action":"insert","lines":["0"]},{"start":{"row":6,"column":25},"end":{"row":6,"column":26},"action":"insert","lines":["2"]},{"start":{"row":6,"column":26},"end":{"row":6,"column":27},"action":"insert","lines":["2"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":13,"column":23},"end":{"row":13,"column":23},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1689658313806,"hash":"ee2b2425d3610b5ceb0f82aa30e0cfe8d51d09ba"}