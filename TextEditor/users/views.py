from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
# Create your views here.

import requests

from .serializers import CreateUserSerializer

CLIENT_ID = 'DLHdCStXfnWAp9FN6v6pjMCn2e5efxfaLPrIe7oM'
CLIENT_SECRET = 'nNAELSKaA1C2cOas2hEleQ4O7z1py1bUvHD3l0op6dom9DYTtqweOZ62SBPmQVEtviblszBn4F1tVmwGIurwFBVBqeLzyyb2kAIzhCAPSJSBTtMzYSwzOZY7nsxhoaxp'


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = CreateUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        r = requests.post('http://127.0.0.1:8000/o/token/',
                          data={
                              'grant_type': 'password',
                              'username': request.data['username'],
                              'password': request.data['password'],
                              'client_id': CLIENT_ID,
                              'client_secret': CLIENT_SECRET,
                          },
                          )
        return Response(r.json())
    return Response(serializer.errors)


@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    r = requests.post(
        'http:/127.0.0.1:8000/o/token/',
        data={
            'grant_type': 'password',
            'username': request.data['username'],
            'password': request.data['password'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    r = requests.post(
        'http:/127.0.0.1:8000/o/token/',
        data={
            'grant_type': 'refresh_token',
            'refresh_token': request.data['refresh_token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def revoke_token(request):
    r = requests.post(
        'http:/127.0.0.1:8000/o/revoke_token',
        data={
            'grant_type': 'revoke_token',
            'refresh_token': request.data['token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    if r.status_code == requests.codes.ok:
        return Response({'message': 'token revoked'}, r.status_code)

    return Response(r.json(), r.status_code)
