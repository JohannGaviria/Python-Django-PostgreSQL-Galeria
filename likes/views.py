from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Like
from .serializers import LikeSerializer


# Lógica para obtener y crear like
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def like_list_create(request, image_id):
    # Método GET para obtener los likes
    if request.method == 'GET':
        # Obtiene los likes de la imagen
        likes = Like.objects.filter(image=image_id).order_by('id')

        # Verifica que existan likes
        if not likes.exists():
            # Respuesta de error
            return Response({
                'status': 'errors',
                'message': 'Validation failed',
                'errors': {
                    'likes': [
                        'The image has no likes'
                    ]
                }
            }, status=status.HTTP_400_BAD_REQUEST)

        # Serializa los datos
        serializer = LikeSerializer(likes, many=True)

        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Likes loaded successfully',
            'data': {
                'likes': serializer.data
            }
        }, status=status.HTTP_200_OK)
    
    # Método POST para crear un Like
    if request.method == 'POST':
        # Serializa los datos recibidos en la solicitud
        serializer = LikeSerializer(data=request.data)

        # Verifica que los datos son válidos
        if serializer.is_valid():
            # Guarda el like
            serializer.save()

            # Respuesta exitosa
            return Response({
                'status': 'success',
                'message': 'Like added successfully',
                'data': {
                    'like': serializer.data
                }
            }, status=status.HTTP_201_CREATED)
        
        # Respuesta de error
        return Response({
            'status': 'errors',
            'message': 'Validation failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


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
