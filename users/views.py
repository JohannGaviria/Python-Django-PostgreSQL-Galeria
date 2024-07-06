from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


# Lógica para el registro de usuarios
@api_view(['POST'])
def register(request):
    # Respuesta exitosa
    return Response({
        'status': 'success',
        'message': 'Registration successful'
    }, status=status.HTTP_201_CREATED)


# Lógica para el inicio de sesión
@api_view(['POST'])
def login(request):
    # Respuesta exitosa
    return Response({
        'status': 'success',
        'message': 'Login successful'
    }, status=status.HTTP_200_OK)


# Lógica para el cierre de sesión
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
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
    # Método GET para obtener el perfil
    if request.method == 'GET':
        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Profile loaded successfully'
        }, status=status.HTTP_200_OK)

    # Método PUT para actualizar el perfil
    if request.method == 'PUT':
        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Profile updated successfully'
        }, status=status.HTTP_200_OK)
    
    # Método DELETE para eliminar el perfil
    if request.method == 'DELETE':
        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Profile deleted successfully'
        }, status=status.HTTP_200_OK)
