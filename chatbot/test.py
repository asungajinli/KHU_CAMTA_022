import config
import re
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

app = App(token=config.bot_token)


@app.event("app_mention")  # 앱을 언급했을 때
def who_am_i(event, client, message, say):
    print('event:', event)
    print('client:', client)
    print('message:', message)
    say(f'hello! <@{event["user"]}>')

@app.message(re.compile("lunch"))
def regex(event, client, message, say):
    say('eat burger')

if __name__ == '__main__':
    SocketModeHandler(app, config.app_token).start()