import compile
import re
import config
import os
import random
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

#set the bot token for your Slack bot 
bot_token = config.bot_token

#Initialize a Slack Bolt app
app = App(token=config.bot_token)

phrase=["저는 항상 당신 곁에 있어요! 지켜드릴게요. 절대 죽으면 안돼요!🤗  ","그런 생각 마세요!가족들을 생각하세요!","제가 꼭 안아줄게요!(づ｡◕‿‿◕｡)づ","맘껏 울어요! 아무도 뭐라고 안해요.🥰  "]

phrase2=["세상에서 가장 못생긴 새는?:우리 생김새","높은 곳에서 아기를 낳으면?:하이에나","서울이 추우면?:서울시립대","땅이 어떻게 울까?:흙흙","11월에 뱀이랑 벌이 없는 이유는?:노뱀벌","미국에 비가 내리면?: USB","살찐 사람들이 많은 동네는?: 개포동",'피카츄가 담배 피고 싶을 때 하는 말은?: 피까','수소가 암소의 발을 밟았을 때 하는 말은?: 암소쏘리','물리치료가 물리치료인 이유는?: 병을 물리치려고']

@app.message("힘들어")
def ask_who(message,say):
    random_int = random.randint(0,3)
    say(phrase[random_int])
    
@app.message("아재개그")
def ask_humor(message,say):
    random_int = random.randint(0,9)
    say(phrase2[random_int])
    

#start the Socket Mode handler
if __name__ == "__main__":
    handler = SocketModeHandler(app_token=config.app_token,app=app)
    handler.start()