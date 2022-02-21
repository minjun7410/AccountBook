from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.contrib.auth.hashers import check_password

# Create your views here.
def signup(request):
    if request.method == "POST" :
        if not(User.objects.filter(email=request.POST['email'])):
            User.objects.create_user(email=request.POST['email'], username=request.POST['username'], password=request.POST['password'])
            return render(request, 'user/login.html', {})
        else:
            messages.info(request, 'Duplicated email. rewrite!')
            return render(request, 'user/signup.html', {})

    return render(request, 'user/signup.html', {})

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        if not(User.objects.filter(email=email)):
            messages.info(request, "No Email")
            return render(request, 'user/login.html', {})
        else:
            user_queryset = User.objects.get(email=email)
            if check_password(request.POST['password'], user_queryset.password):
                request.session['username'] = user_queryset.username
                request.session['email'] = user_queryset.email
                request.session.modified = True
                return redirect('/account')
            else:
                messages.info(request, "Password do not match")
                return render(request, 'user/login.html', {})
    else:
        return render(request, 'user/login.html', {})
