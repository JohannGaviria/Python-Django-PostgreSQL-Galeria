from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


# Lógica para obtener y crear comentarios
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes(IsAuthenticated)
def comment_list_create(request, image_id):
    # Método GET para obtener los comentarios
    if request.method == 'GET':
        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Comments loaded successfully',
        }, status=status.HTTP_200_OK)
    
    # Método POST para crear un comentario
    if request.method == 'POST':
        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Comment added successfully',
        }, status=status.HTTP_201_CREATED)


# Lógica para el detalle de comentarios
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes(IsAuthenticated)
def comment_detail(request, comment_id):
    # Método GET para obtener un comentario
    if request.method == 'GET':
        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Comment details loaded successfully',
        }, status=status.HTTP_200_OK)
    
    # Método PUT para actualizar un comentario
    if request.method == 'PUT':
        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Comment updated successfully',
        }, status=status.HTTP_200_OK)
    
    # Método DELETE para eliminar un comentario
    if request.method == 'DELETE':
        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Comment deleted successfully',
        }, status=status.HTTP_200_OK)
