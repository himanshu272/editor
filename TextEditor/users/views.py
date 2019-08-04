from django.contrib.auth import authenticate
from django.conf import settings
from social_django.utils import psa
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from django.contrib.auth.models import User
from rest_framework import serializers


'''@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


class CreateUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def register(request):
    serializer = CreateUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key},
                        status=HTTP_200_OK)'''


class SocialSerializer(serializers.Serializer):
    access_token = serializers.CharField(
        allow_blank=False,
        trim_whitespace=True,
    )


@csrf_exempt
@api_view(["POST"])
@permission_classes([AllowAny])
@psa()
def exchange_token(request, backend):
    serializer = SocialSerializer(data=request.data)
    print(backend)
    if serializer.is_valid(raise_exception=True):
        user = request.backend.do_auth(
            serializer.validated_data['access_token'])
        print(user)
        if user:
            if user.is_active:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({
                    'token': token.key
                })
            else:
                return Response({
                    'errors': 'Authentication failed'
                }, status=HTTP_400_BAD_REQUEST)
