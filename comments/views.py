from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from .serializers import CommentSerializer


# Lógica para obtener y crear comentarios
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_list_create(request, image_id):
    # Método GET para obtener los comentarios
    if request.method == 'GET':
        # Obtiene los comentarios de la imagen
        comments = Comment.objects.filter(image=image_id).order_by('id')

        # Verifica que existan imagenes
        if not comments.exists():
            # Respuesta de error
            return Response({
                'status': 'errors',
                'message': 'Validation failed',
                'errors': {
                    'comments': [
                        'The image has no comments'
                    ]
                }
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Serializa los datos
        serializer = CommentSerializer(comments, many=True)

        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Comments loaded successfully',
            'data': {
                'comments': serializer.data
            }
        }, status=status.HTTP_200_OK)
    
    # Método POST para crear un comentario
    if request.method == 'POST':
        # Serializa los datos recibidos en la solicitud
        serializer = CommentSerializer(data=request.data)

        # Verifica que los datos son válidos
        if serializer.is_valid():
            # Guarda el comentario
            serializer.save()

            # Respuesta exitosa
            return Response({
                'status': 'success',
                'message': 'Comment added successfully',
                'data': {
                    'comment': serializer.data
                }
            }, status=status.HTTP_201_CREATED)
        
        # Respuesta de error
        return Response({
            'status': 'errors',
            'message': 'Validation failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


# Lógica para el detalle de comentarios
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_detail(request, comment_id):
    try:
        # Obtiene el comentario del ID
        comment = Comment.objects.get(id=comment_id)
    except Comment.DoesNotExist:
        # Respuesta de error
        return Response({
            'status': 'errors',
            'message': 'Validation failed',
            'errors': {
                'comment': [
                    'Comment not found'
                ]
            }
        }, status=status.HTTP_400_BAD_REQUEST)

    # Método GET para obtener un comentario
    if request.method == 'GET':
        # Serializa los datos del comentario
        serializer = CommentSerializer(comment)

        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Comment details loaded successfully',
            'data': {
                'comment': serializer.data
            }
        }, status=status.HTTP_200_OK)
    
    # Método PUT para actualizar un comentario
    if request.method == 'PUT':
        # Serializa los datos recibidos en la solicitud
        serializer = CommentSerializer(comment, data=request.data)

        # Verifica que los datos son válidos
        if serializer.is_valid():
            # Actualiza los datos
            serializer.save()

            # Respuesta exitosa
            return Response({
                'status': 'success',
                'message': 'Comment updated successfully',
                'data': {
                    'comment': serializer.data
                }
            }, status=status.HTTP_200_OK)
        
        # Respuesta de error
        return Response({
            'status': 'errors',
            'message': 'Validation failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # Método DELETE para eliminar un comentario
    if request.method == 'DELETE':
        # Elimina el comentario
        comment.delete()
        
        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Comment deleted successfully',
        }, status=status.HTTP_200_OK)
