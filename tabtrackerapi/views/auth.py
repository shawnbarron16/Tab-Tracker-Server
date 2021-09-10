from tabtrackerapi.models import user
from django.conf import UserSettingsHolder
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    """Handles the authentication of a user

    Method arguments:
        request -- The full HTTP request object
    """
    email = request.data['email']
    password = request.data['password']

    authenticated_user = authenticate(email=email, password=password)

    if authenticated_user is not None:
        token = Token.objects.get(user=authenticated_user)
        data = {
            'valid': True,
            'token': token.key
        }
        return Response(data)
    else:
        data = { 'valid':False}
        return Response(data)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    """Handles the creation of a new gamer for authentication

    Method arguments:
        request -- The full HTTP object
    """
    
    new_user = User.objects.create_user(
        email=request.data['email'],
        password=request.data['password'],
        first_name=request.data['first_name'],
        last_name=request.data['last_name']
    )
    
    User.objects.create(new_user)

    token = Token.objects.create(user=User)
    data = { 'token': token.key }
    return Response(data)