from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from ..serializers import *
from ..models import *



@api_view(['POST'])
def user_create(request):
    password = request.data['password']
    serializer = GGITUserSerializer(data=request.data)
    
    if serializer.is_valid():
        instance = serializer.save()
        instance.set_password(password)
        instance.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=406)
    


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_me(request):
    user = request.user
    serializer = GGITUserSerializer(user)
    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def users_list(request):
    users = GGITUser.objects.all()
    serializer = GGITUserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def user_is_unique(request):
    serializer = GGITUserSerializer(data = request.data)
    if  GGITUser.objects.filter(username = request.data['username']).exists():
      return Response(status = 400)
    else:
     return Response(status = 200)


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def user_id(request, pk):
    if (request.method == 'GET'):
        users = get_object_or_404(GGITUser, pk = pk)
        serializer = GGITUserSerializer(users)
        return Response(serializer.data)
    
    elif(request.method == 'PUT'):
        users = get_object_or_404(GGITUser, pk = pk)
        serializer = GGITUserSerializer(instance = users, data = request.data)
        if  serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



