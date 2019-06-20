from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import NoteSerializer
from .models import Notes
# Create your views here.


class NoteviewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = NoteSerializer
