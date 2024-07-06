from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


# Lógica para obtener y crear imagenes
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes(IsAuthenticated)
def image_list_create(request):
    # Método GET para obtener las imagenes
    if request.method == 'GET':
        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Images loaded successfully',
        }, status=status.HTTP_200_OK)
    
    # Método POST para crear una imagen
    if request.method == 'POST':
        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Image uploaded successfully',
        }, status=status.HTTP_201_CREATED)


# Lógica para el detalle de imagenes
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes(IsAuthenticated)
def image_detail(request, image_id):
    # Método GET para obtener una imagen
    if request.method == 'GET':
        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Image details loaded successfully',
        }, status=status.HTTP_200_OK)
    
    # Método PUT para actualizar una imagen
    if request.method == 'PUT':
        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Image updated successfully',
        }, status=status.HTTP_200_OK)
    
    # Método DELETE para eliminar una imagen
    if request.method == 'DELETE':
        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Image deleted successfully',
        }, status=status.HTTP_200_OK)


# Lógica para buscar imagenes
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes(IsAuthenticated)
def search_images(request):
    # Respuesta exitosa
    return Response({
        'status': 'success',
        'message': 'Search results loaded successfully',
    }, status=status.HTTP_200_OK)
