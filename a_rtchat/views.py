from django.shortcuts import render

# Create your views here.

def chat_view(req):
    return render(req, 'a_rtchat/chat.html')
