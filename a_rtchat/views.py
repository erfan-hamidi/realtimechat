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

    if req.method == 'POST':
        form = ChatmessageCreateForm(req.POST)
        if form.is_valid:
            message = form.save(commit=False)
            print(req.user)
            message.group = chat_group
            message.author = req.user
            
            message.save()
            return redirect('home')

    return render(req, 'a_rtchat/chat.html', {'chat_messages' : chat_messages, 'form' : form})
