from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from ..serializers  import *
from ..models import *

# Create your views here.

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])

def notes(request, pk):
    
    if request.method == 'GET':
        return Response(get_note(request, pk))
    if request.method == 'PUT':
        return Response(put_note(request, pk))
    if request.method == 'DELETE':
        return delete_note(request, pk)

def get_note(request, pk):
    note_get = get_object_or_404(Note, pk = pk)
    serializer = NoteSerializer(note_get)
    return serializer.data


def put_note(request, pk):
    note_put = get_object_or_404(Note, pk = pk)
    serializer = NoteSerializer(data = request.data)
    data = request.data
    data['user'] = request.user.id
    serializer_2 = NoteSerializer(instance = note_put, data = request.data)
    if serializer_2.is_valid():
            serializer_2.save()
            return serializer_2.data
    else:
            return serializer_2.errors


def delete_note(request, pk):
    note_delete = get_object_or_404(Note, pk = pk)
    note_delete.delete()
    return Response(status = 200)

