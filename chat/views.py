from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib import messages
from .decorators import unauthenticated_user
from .models import Message, Profile
from .forms import CreateUserForm

@unauthenticated_user
def signuppage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        username = request.POST.get('username')
        if form.is_valid():
            form.save()
            messages.success(request, 'Account has been created for ' + username)
            return redirect('login')
        else:
            messages.info(request, )
    context = {'form':form}
    return render(request, 'signup.html', context)

@unauthenticated_user
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username OR Password is incorrect.')
    context = {

    }
    return render(request, 'login.html', context)

def logoutpage(request):
    logout(request)
    return redirect('login')

@login_required
def index(request):
    user_profiles = Profile.objects.exclude(user=request.user)
    users = get_user_model().objects.exclude(username=request.user.username)
    # Create a list to store thread names
    thread_names = []
    # Loop through user profiles to generate thread names
    for user_profile in user_profiles:
        user_id_1 = request.user.id
        user_id_2 = user_profile.user.id
        thread_name = f'chat_{max(user_id_1, user_id_2)}_{min(user_id_1, user_id_2)}'
        thread_names.append(thread_name)
    # Fetch the last message for each thread
    last_messages = Message.objects.filter(thread_name__in=thread_names).order_by('thread_name', '-timestamp')
    # Create a dictionary to store the last messages for each thread
    last_messages_dict = {message.thread_name: message for message in last_messages}
    context = {'users': users, 'last_messages': last_messages_dict}
    return render(request, 'home.html', context)


@login_required
def chat_page(request, username):
    user_object = get_user_model().objects.get(username=username)
    users = get_user_model().objects.exclude(username=request.user.username)
    thread_name = (
        f'chat_{request.user.id}_{user_object.id}'
        if int(request.user.id) > int(user_object.id)
        else f'chat_{user_object.id}_{request.user.id}'
    )
    profiles = Profile.objects.get(user=user_object.id)
    messages = Message.objects.filter(thread_name=thread_name).select_related('sender')
    lastmessages = Message.objects.filter(thread_name=thread_name).order_by('-timestamp').first()
    context = {
        'users': users,
        'user_object': user_object,
        'messages': messages,
        'lastmessages': lastmessages,
        'profiles': profiles,
    }
    return render(request, 'messages.html', context)
