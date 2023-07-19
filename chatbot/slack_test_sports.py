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