from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Album
from .serializers import AlbumSerializer


# Lógica para obtener y crear albums
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def album_list_create(request):
    # Método GET para obtener los albumes
    if request.method == 'GET':
        # Intenta obtener los álbumes del usuario
        albums = Album.objects.filter(user=request.user).order_by('id')

        if not albums.exists():
            # Si no hay álbumes, devuelve un error
            return Response({
                'status': 'errors',
                'message': 'Validation failed',
                'errors': {
                    'album': [
                        'you do not have albums created'
                    ]
                }
            }, status=status.HTTP_400_BAD_REQUEST)

        # Serializa los datos
        serializer = AlbumSerializer(albums, many=True)

        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Albums loaded successfully',
            'data': {
                'albumes': serializer.data
            }
        }, status=status.HTTP_200_OK)
    
    # Método POST para crear un album
    if request.method == 'POST':
        # Serializa los datos enviados en la solicitud
        serializer = AlbumSerializer(data=request.data)

        # Verifica que los datos son válidos
        if serializer.is_valid():
            # Guarda el nuevo album
            serializer.save()

            # Respuesta exitosa
            return Response({
                'status': 'success',
                'message': 'Album created successfully',
                'data': {
                    'album': serializer.data
                }
            }, status=status.HTTP_201_CREATED)
        
        # Respuesta de error
        return Response({
            'status': 'errors',
            'message': 'Validation failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


# Lógica para el detalle de albumes
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def album_detail(request, album_id):
    try:
        # Obtiene el álbum por su ID
        album = Album.objects.get(id=album_id)
    except Album.DoesNotExist:
        # Respuesta de error
        return Response({
            'status': 'errors',
            'message': 'Validation failed',
            'errors': {
                'album': [
                    'Album not found'
                ]
            }
        }, status=status.HTTP_404_NOT_FOUND)

    # Método GET para obtener un album
    if request.method == 'GET':
        # Serializa los datos
        serializer = AlbumSerializer(album)

        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Album details loaded successfully',
            'data': {
                'album': serializer.data
            }
        }, status=status.HTTP_200_OK)
    
    # Método PUT para actualizar un album
    if request.method == 'PUT':
        # Serializa los datos enviados en la solicitud
        serializer = AlbumSerializer(album, data=request.data)

        # Verifica que los datos son válidos
        if serializer.is_valid():
            # Actualiza los datos
            serializer.save()

            # Respuesta exitosa
            return Response({
                'status': 'success',
                'message': 'Album updated successfully',
                'data': {
                    'album': serializer.data
                }
            }, status=status.HTTP_200_OK)
        
        # Respuesta de error
        return Response({
            'status': 'errors',
            'message': 'Validation failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # Método DELETE para eliminar un album
    if request.method == 'DELETE':
        # Elimina el album
        album.delete()

        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Album deleted successfully',
        }, status=status.HTTP_200_OK)
