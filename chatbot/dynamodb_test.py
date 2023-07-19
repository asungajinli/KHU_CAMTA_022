import boto3

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

# store_id를 기준으로 오름차순으로 정렬
sorted_items = sorted(items, key=lambda x: x[partition_key])

# 정렬된 데이터 출력
for item in sorted_items:
    store_id = item[partition_key]
    title = item['title']
    category = item['category']
    url = item['url']
    
    print(f"Store ID: {store_id}")
    print(f"Store Name: {title}")
    print(f"Category: {category}")
    print(f"URL: {url}")
    print()