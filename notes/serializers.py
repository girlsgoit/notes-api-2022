from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from .models import GGITUser, NoteElement, Note
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)


class GGITUserSerializer(ModelSerializer):
    class Meta:
        model = GGITUser
        exclude = ['password', 'is_superuser', 'last_login']

class Note_elementSerializer(ModelSerializer):
    class Meta:
        model = NoteElement
        exclude = ['note']


class NoteSerializer(ModelSerializer):
    note_elements = Note_elementSerializer(many=True)
    
    class Meta:
        model = Note
        fields = '__all__'

    def create(self, data):
        note_elements = data.pop('note_elements')
        note = Note.objects.create(data)

        for item in note_elements:
            NoteElement.objects.create(note = note, tag=item['tag'], content = item['content'])
        
        return note

    def update(self,instance: Note, data):
        instance.note_elements.all().delete()
        note_elements = data.pop('note_elements')

        for item in note_elements:
            NoteElement.objects.create(note = instance, tag = item['tag'], content = item['content'])

        return instance




