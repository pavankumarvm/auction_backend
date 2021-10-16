import random

from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
import rest_framework.status as status
from rest_framework.views import APIView

from .serializers import UserSerializer
from .models import User, Otp
from rest_framework.authtoken.models import Token


class RegisterView(APIView):
    def post(self, request):
        usertype = request.data.get('usertype')
        username = request.data.get('username')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        phone_no = request.data.get('phone_no')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')

        if not (username and first_name and last_name and email and phone_no and password1 and password2):
            return Response(
                {
                    'message': 'Details not filled',
                }
            )
        elif password1 == password2:
            if User.objects.filter(username=username):
                return Response(
                    {
                        'message': 'Username already exists.Try another.',
                    }, status=status.HTTP_400_BAD_REQUEST
                )
            elif User.objects.filter(email=email):

                return Response(
                    {
                        'message': 'Email Address exists.Try another.',
                    }, status=status.HTTP_400_BAD_REQUEST
                )
            else:
                try:
                    user = User.objects.create_user(
                        username=username,
                        password=password1,
                        email=email,
                        phone_no=phone_no,
                        first_name=first_name,
                        last_name=last_name,
                        usertype=usertype)
                    token = Token.objects.create(user=user)
                    return Response(
                        {
                            'message': 'User registered successfully.',
                            'token': token.key,
                            'user': UserSerializer(user).data
                        }, status=status.HTTP_201_CREATED
                    )
                except:
                    return Response(
                        {
                            'message': 'User was not registered.Try Again.',
                        }, status=status.HTTP_400_BAD_REQUEST
                    )
        else:
            return Response(
                {
                    'message': "Passwords doesn't match",
                }, status=status.HTTP_400_BAD_REQUEST
            )


class LoginView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            try:
                login(request, user)
                if Token.objects.filter(user=user):
                    # print("token present")
                    Token.objects.get(user=user).delete()
                token = Token.objects.create(user=user)
                return Response(
                    {
                        'message': 'Logged in Successfully.',
                        'token': token.key
                    }, status=status.HTTP_200_OK
                )
            except:
                return Response({
                    'message': 'Something went wrong.Try again.',
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {
                    'message': 'Username or Password incorrect.',
                }, status=status.HTTP_401_UNAUTHORIZED
            )


class LogoutView(APIView):

    def post(self, request):
        try:
            if Token.objects.filter(user=request.user):
                token_obj = Token.objects.get(user=request.user)
                token_obj.delete()
                logout(request)
                return Response({
                    'message': 'Logged out successfully.',
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'message': 'Token not valid.',
                }, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({
                'message': 'Something went wrong.Try again.',
            }, status=status.HTTP_400_BAD_REQUEST)


def random_otp():
    random_str = ""
    for i in range(6):
        if i == 0:
            random_str += str(random.randrange(1, 9, 1))
        else:
            random_str += str(random.randrange(0, 9, 1))
    return random_str


class ForgotPasswordView(APIView):
    def post(self, request):
        pass
