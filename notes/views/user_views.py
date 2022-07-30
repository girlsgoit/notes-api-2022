from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from ..serializers import *
from ..models import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@swagger_auto_schema(
 method = "POST",
 operation_description = "Create a user.",
 request_body=openapi.Schema(
     type = openapi.TYPE_OBJECT,
    properties = {
         'username' : openapi.Schema( type = openapi.TYPE_STRING,
         description = 'unique username'
         ),
   
         'password' : openapi.Schema(type = openapi.TYPE_STRING,
         description = 'User password'
     ),
    
         'first_name' : openapi.Schema(type = openapi.TYPE_STRING,
         description = 'First Name'
     ),
    
        'last_name' : openapi.Schema(type = openapi.TYPE_STRING,
         description = 'Last name'
     ),
    
         'email' : openapi.Schema(type = openapi.TYPE_STRING,
         description = 'User email'
         ),    
     },
     required = ['username', 'password'],  
 ),
     responses = {201:GGITUserSerializer()},     
 )


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


   


@swagger_auto_schema(
method = "GET",
operation_description = "Get the user information.",
responses = {200:GGITUserSerializer()}
)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_me(request):
    user = request.user
    serializer = GGITUserSerializer(user)
    return Response(serializer.data)

   


@swagger_auto_schema( 
method = "GET",
operation_description = "Get the users list.",
responses = {200:GGITUserSerializer()}    
)
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



