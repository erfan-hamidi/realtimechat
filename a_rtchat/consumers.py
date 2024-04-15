from channels.generic.websocket import WebsocketConsumer
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from asgiref.sync import async_to_sync
import json
from .models import *


class ChatroomConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()