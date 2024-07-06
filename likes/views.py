from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


# Lógica para obtener y crear like
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes(IsAuthenticated)
def like_list_create(request, image_id):
    # Método GET para obtener los likes
    if request.method == 'GET':
        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Likes loaded successfully',
        }, status=status.HTTP_200_OK)
    
    # Método POST para crear un Like
    if request.method == 'POST':
        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Like added successfully',
        }, status=status.HTTP_201_CREATED)


# Lógica para el detalle de like
@api_view(['GET', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes(IsAuthenticated)
def like_detail(request, like_id):
    # Método GET para obtener un like
    if request.method == 'GET':
        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Like details loaded successfully',
        }, status=status.HTTP_200_OK)
    
    # Método DELETE para eliminar un like
    if request.method == 'DELETE':
        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Like deleted successfully',
        }, status=status.HTTP_200_OK)
