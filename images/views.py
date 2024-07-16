from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import Image
from .serializers import ImageSerializer


# Lógica para obtener y crear imagenes
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def image_list_create(request):
    # Método GET para obtener las imagenes
    if request.method == 'GET':
        # Obtiene las imagenes del usuario
        images = Image.objects.filter(user=request.user).order_by('id')

        # Verifica que existan imagenes
        if not images.exists():
            # Respuesta de error
            return Response({
                'status': 'errors',
                'message': 'Validation failed',
                'errors': {
                    'images': [
                        'you do not have any images uploaded'
                    ]
                }
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Serializa los datos
        serializer = ImageSerializer(images, many=True)

        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Images loaded successfully',
            'data': {
                'images': serializer.data
            }
        }, status=status.HTTP_200_OK)
    
    # Método POST para crear una imagen
    if request.method == 'POST':
        # Serialize los datos recibidos en la solicitud
        serializer = ImageSerializer(data=request.data)

        # Verifica que los datos son válidos
        if serializer.is_valid():
            # Guarda la imagen
            serializer.save()
            # Respuesta exitosa
            return Response({
                'status': 'success',
                'message': 'Image uploaded successfully',
                'data': {
                    'image': serializer.data
                }
            }, status=status.HTTP_201_CREATED)
        
        # Respuesta de error
        return Response({
            'status': 'errors',
            'message': 'Validation failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


# Lógica para el detalle de imagenes
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def image_detail(request, image_id):
    try:
        # Obtiene la imagen del ID
        image = Image.objects.get(id=image_id)
    except Image.DoesNotExist:
        # Respuesta de error
        return Response({
            'status': 'errors',
            'message': 'Validation failed',
            'errors': {
                'image': [
                    'Image not found'
                ]
            }
        }, status=status.HTTP_404_NOT_FOUND)
    
    # Método GET para obtener una imagen
    if request.method == 'GET':
        # Serializa los datos de la imagen
        serializer = ImageSerializer(image)

        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Image details loaded successfully',
            'data': {
                'image': serializer.data
            }
        }, status=status.HTTP_200_OK)
    
    # Método PUT para actualizar una imagen
    if request.method == 'PUT':
        # Serializa los datos recibidos en la solicitud
        serializer = ImageSerializer(image, data=request.data)

        # Verifica que los datos son válidos
        if serializer.is_valid():
            # Actualiza los datos
            serializer.save()

            # Respuesta exitosa
            return Response({
                'status': 'success',
                'message': 'Image updated successfully',
                'data': {
                    'image': serializer.data
                }
            }, status=status.HTTP_200_OK)
        
        # Respuesta de error
        return Response({
            'status': 'errors',
            'message': 'Validation failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # Método DELETE para eliminar una imagen
    if request.method == 'DELETE':
        # Elimina la imagen
        image.delete()

        # Respuesta exitosa
        return Response({
            'status': 'success',
            'message': 'Image deleted successfully',
        }, status=status.HTTP_200_OK)


# Lógica para buscar imagenes
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def search_images(request):
    # Obtiene los párametros de búsqueda
    query = request.query_params.get('query', None)
    
    # Busca las imagenes que coincidan con la búsqueda
    images = Image.objects.filter(
        Q(title__icontains=query) |
        Q(description__icontains=query)
    )

    # Serializa los datos de las imagenes
    serializer = ImageSerializer(images, many=True)

    # Respuesta exitosa
    return Response({
        'status': 'success',
        'message': 'Search results loaded successfully',
        'data': {
            'images': serializer.data
        }
    }, status=status.HTTP_200_OK)
