{"filter":false,"title":"test.py","tooltip":"/chatbot/test.py","undoManager":{"mark":9,"position":9,"stack":[[{"start":{"row":0,"column":0},"end":{"row":20,"column":52},"action":"insert","lines":["import config","import re","from slack_bolt import App","from slack_bolt.adapter.socket_mode import SocketModeHandler","","app = App(token=config.bot_token)","","","@app.event(\"app_mention\")  # 앱을 언급했을 때","def who_am_i(event, client, message, say):","  print('event:', event)","  print('client:', client)","  print('message:', message)","\tsay(f'hello! <@{event[\"user\"]}>')","","@app.message(re.compile(\"lunch\"))","def regex(event, client, message, say):","    say('eat burger')","","if __name__ == '__main__':","    SocketModeHandler(app, config.app_token).start()"],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":20,"column":52},"action":"remove","lines":["import config","import re","from slack_bolt import App","from slack_bolt.adapter.socket_mode import SocketModeHandler","","app = App(token=config.bot_token)","","","@app.event(\"app_mention\")  # 앱을 언급했을 때","def who_am_i(event, client, message, say):","  print('event:', event)","  print('client:', client)","  print('message:', message)","\tsay(f'hello! <@{event[\"user\"]}>')","","@app.message(re.compile(\"lunch\"))","def regex(event, client, message, say):","    say('eat burger')","","if __name__ == '__main__':","    SocketModeHandler(app, config.app_token).start()"],"id":5},{"start":{"row":0,"column":0},"end":{"row":20,"column":52},"action":"insert","lines":["import config","import re","from slack_bolt import App","from slack_bolt.adapter.socket_mode import SocketModeHandler","","app = App(token=config.bot_token)","","","@app.event(\"app_mention\")  # 앱을 언급했을 때","def who_am_i(event, client, message, say):","  print('event:', event)","  print('client:', client)","  print('message:', message)","\tsay(f'hello! <@{event[\"user\"]}>')","","@app.message(re.compile(\"lunch\"))","def regex(event, client, message, say):","    say('eat burger')","","if __name__ == '__main__':","    SocketModeHandler(app, config.app_token).start()"]}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"remove","lines":["\t"],"id":6}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "],"id":7}],[{"start":{"row":12,"column":1},"end":{"row":12,"column":2},"action":"remove","lines":[" "],"id":8}],[{"start":{"row":12,"column":1},"end":{"row":12,"column":4},"action":"insert","lines":["   "],"id":9}],[{"start":{"row":11,"column":1},"end":{"row":11,"column":2},"action":"remove","lines":[" "],"id":10}],[{"start":{"row":11,"column":1},"end":{"row":11,"column":4},"action":"insert","lines":["   "],"id":11}],[{"start":{"row":10,"column":1},"end":{"row":10,"column":2},"action":"remove","lines":[" "],"id":12}],[{"start":{"row":10,"column":1},"end":{"row":10,"column":4},"action":"insert","lines":["   "],"id":13}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":7,"column":0},"end":{"row":7,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1689654667384,"hash":"9ad981e2f3f6d0691f2a326fa05a8eb7910bbbd3"}