from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .api.serializers import RegistrationSerializer
from .api.renderers import UserJSONRenderer

# Create your views here.
class RegistrationAPIView(APIView):
    permission_classes = (AllowAny)
    serializer_class = RegistrationSerializer
    renderer_classes = (UserJSONRenderer,)
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
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
                request.session['email_id'] = user_queryset.id
                request.session.modified = True
                return redirect('/account')
            else:
                messages.info(request, "Password do not match")
                return render(request, 'user/login.html', {})
    else:
        return render(request, 'user/login.html', {})
