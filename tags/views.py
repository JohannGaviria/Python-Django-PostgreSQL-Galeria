from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


# Lógica para obtener las etiquetas
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def labels_list(request):
    # Respuesta exitosa
    return Response({
        'status': 'success',
        'message': 'Tags loaded successfully'
    }, status=status.HTTP_200_OK)
