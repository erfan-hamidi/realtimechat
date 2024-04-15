from django.shortcuts import render, get_object_or_404, redirect 
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ChatmessageCreateForm
# Create your views here.

@login_required
def chat_view(req):
    chat_group = get_object_or_404(ChatGroup, group_name="public chat")
    chat_messages = chat_group.chat_messages.all()[:30]
    form = ChatmessageCreateForm()

    if req.htmx:
        form = ChatmessageCreateForm(req.POST)
        if form.is_valid:
            message = form.save(commit=False)
            message.author = req.user
            message.group = chat_group
            message.save()
            print(message)
            context = {
                'message' : message,
                'user' : req.user
            }
            return render(req, 'a_rtchat/partials/chat_message_p.html', context)
            

    return render(req, 'a_rtchat/chat.html', {'chat_messages' : chat_messages, 'form' : form})
