from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.utils import timezone
from datetime import timedelta
from .models import User
from .serializers import UserSerializer


# Lógica para el registro de usuarios
@api_view(['POST'])
def register(request):
    # Serializa los datos enviados en la solicitud
    serializer = UserSerializer(data=request.data)

    # Verifica que los datos sean válidos
    if serializer.is_valid():
        # Guarda el usuario
        serializer.save()

        # Obtiene el usuario recién registrado
        user = User.objects.get(email=serializer.data['email'])
        # Hashea la contraseña del usuario
        user.set_password(request.data['password'])
        # Guarda el cambio
        user.save()
        
        # Crea un token de autenticación para el usuario
        token = Token.objects.create(user=user)

        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Registration successful',
            'data': {
                'token' : {
                    'token_key': token.key
                },
                'user': serializer.data
            }
        }, status=status.HTTP_201_CREATED)
    
    # Respuesta de error
    return Response({
        'status': 'errors',
        'message': 'Validation failed',
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


# Lógica para el inicio de sesión
@api_view(['POST'])
def login(request):
    # Obtiene los datos enviados en la solicitud
    email = request.data.get('email')
    password = request.data.get('password')

    # Busca al usuario que intenta iniciar sesión
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        # Respuesta de error
        return Response({
            'status': 'errors',
            'message': 'Validation failed',
            'errors': {
                'email': [
                    'Email is incorrect'
                ]
            }
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # Verifica que la contraseña sea válida
    if not user.check_password(password):
        # Respuesta de error
        return Response({
            'status': 'errors',
            'message': 'Validation failed',
            'errors': {
                'password': [
                    'Password is incorrect'
                ]
            }
        }, status=status.HTTP_400_BAD_REQUEST)

    # Calcula la fecha de expiración del token
    expiration = timezone.now() + timedelta(days=3)

    # Crea el token del usuario
    token, _ = Token.objects.get_or_create(user=user)

    # Serializa los datos del usuario
    serializer = UserSerializer(user)

    # Respuesta exitosa
    return Response({
        'status': 'success',
        'message': 'Login successful',
        'data': {
            'token': {
                'token_key': token.key,
                'token_expiration': expiration
            },
            'user': serializer.data
        }
    }, status=status.HTTP_200_OK)


# Lógica para el cierre de sesión
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    # Obtiene al usuario actual
    user = request.user

    # Elimina el token de acceso
    Token.objects.get(user=user).delete()

    # Respuesta exitosa
    return Response({
        'status': 'success',
        'message': 'Logout successful'
    }, status=status.HTTP_200_OK)


# Lógica para el perfil de usuario
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    # Obtiene el usuario actual
    user = request.user

    # Método GET para obtener el perfil
    if request.method == 'GET':
        # Serializa los datos del usuario
        serializer = UserSerializer(user)

        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Profile loaded successfully',
            'data': {
                'user': serializer.data
            }
        }, status=status.HTTP_200_OK)

    # Método PUT para actualizar el perfil
    if request.method == 'PUT':
        # Serializa los datos enviados en la solicitud
        serializer = UserSerializer(user, data=request.data)

        # Verifica que los datos sean válidos
        if serializer.is_valid():
            # Actualiza el usuario
            serializer.save()

            # Hashea la contraseña del usuario
            user.set_password(request.data['password'])
            # Guarda el cambio
            user.save()
            
            # Elimina el token viejo del usuario
            Token.objects.filter(user=user).delete()

            # Crea un nuevo token para el usuario
            token = Token.objects.create(user=user)

            # Calcula la nueva fecha de expiración del token
            expiration = timezone.now() + timedelta(days=3)

            # Respuesta exitosa
            return Response({
                'status': 'success',
                'message': 'Profile updated successfully',
                'data': {
                    'token' : {
                        'token_key': token.key,
                        'token_expiration': expiration
                    },
                    'user': serializer.data
                }
            }, status=status.HTTP_200_OK)
        
        # Respuesta de error
        return Response({
            'status': 'errors',
            'message': 'Validation failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    
    # Método DELETE para eliminar el perfil
    if request.method == 'DELETE':
        # Elimana el usuario
        user.delete()

        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Profile deleted successfully'
        }, status=status.HTTP_200_OK)
