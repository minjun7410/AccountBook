from django.shortcuts import render
from .models import User
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == "POST" :
        if not(User.objects.filter(email=request.POST['email'])):
            user = User.objects.create_user(email=request.POST['email'], username=request.POST['username'], password=request.POST['password'])
            return render(request, 'user/login.html', {})
        else:
            messages.info(request, 'Duplicated email. rewrite!')
            return render(request, 'user/signup.html', {})

    return render(request, 'user/signup.html', {})

def login(request):
    if request.method == "POST":
        return render(request, 'user/login.html', {})
    else:
        return render(request, 'user/login.html', {})
