from rest_framework.serializers import ModelSerializer
from .models import GGITUser, NoteElement
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)


class GGITUserSerializer(ModelSerializer):
    class Meta:
        model = GGITUser
        exclude = ['password', 'is_superuser', 'last_login']

class Note_element(ModelSerializer):
    class Meta:
        model = NoteElement
        exclude = ['note']

