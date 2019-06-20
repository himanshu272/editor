from django.urls import path, include
from rest_framework import routers
from .views import NoteviewSet

router = routers.DefaultRouter()
router.register('notes', NoteviewSet)

urlpatterns = [
    path('', include(router.urls)),
]
