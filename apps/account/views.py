from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import *
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth import get_user_model
from .send_mail import send_confirmation_email
from rest_framework_simplejwt.views import TokenObtainPairView
from .send_sms import sending_sms

User = get_user_model()


class RegistrationView(APIView):
    permission_classes = permissions.AllowAny,

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if user:
            try:
                send_confirmation_email(user.email, user.activation_code)
                sending_sms(receiver=user.phone_number)
            except:
                return Response({'message': 'Registered, but trouble with email',
                                 'data': serializer.data}, status=201)
        return Response(serializer.data, status=201)


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = permissions.IsAuthenticated,


class ActivationView(APIView):
    def get(self, request):
        code = request.GET.get('u')
        user = get_object_or_404(User, activation_code=code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response('Successfully activate', status=200)


class LoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny, )




