from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from ..serializers  import *
from ..models import *

# Create your views here.

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])

def note_details(request, pk):

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

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def notes(request):
    if request.method == 'GET':
        notes = Note.objects.filter(user=request.user).all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    if request.method =='POST':
        notes= request.data
        serializer = NoteSerializer(data=notes)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors)            

       