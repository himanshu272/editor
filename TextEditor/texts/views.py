from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import NoteSerializer
from .models import Notes
# Create your views here.


class NoteviewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer
