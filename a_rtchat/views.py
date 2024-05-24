from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect 
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ChatmessageCreateForm
# Create your views here.

@login_required
def chat_view(req, chatroom_name = 'pub-chat'):
    chat_group = get_object_or_404(ChatGroup, group_name=chatroom_name)
    chat_messages = chat_group.chat_messages.all()[:30]
    form = ChatmessageCreateForm()

    other_user = None
    if chat_group.is_private:
        if req.user not in chat_group.members.all():
            raise Http404()
        for member in chat_group.members.all():
            if member != req.user:
                other_user = member
                break
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

    context = {
        'chat_messages': chat_messages,
        "form" : form,
        'other_user': other_user,
        'chatroom_name': chatroom_name
    }       

    return render(req, 'a_rtchat/chat.html', context=context)

@login_required
def get_or_create_chatroom(request, username):
    if request.user.username == username:
        return redirect('home')
    
    other_user = User.objects.get(username = username)
    my_chatrooms = request.user.chat_groups.filter(is_private=True)
    
    
    if my_chatrooms.exists():
        for chatroom in my_chatrooms:
            if other_user in chatroom.members.all():
                chatroom = chatroom
                break
            else:
                chatroom = ChatGroup.objects.create(is_private = True)
                chatroom.members.add(other_user, request.user)
    else:
        chatroom = ChatGroup.objects.create(is_private = True)
        chatroom.members.add(other_user, request.user)
        
    return redirect('chatroom', chatroom.group_name)
