from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .serializers import CreateGoogleDocViewCreateSerializer
from .utils import create_google_doc


class CreateGoogleDocView(APIView):
    """Представление для создания Google Docs документа"""

    @swagger_auto_schema(request_body=CreateGoogleDocViewCreateSerializer)
    def post(self, request, *args, **kwargs):
        serializer = CreateGoogleDocViewCreateSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            data = serializer.validated_data['data']

            try:
                document_id = create_google_doc(data, name)
                return Response({'message': 'Документ успешно создан.', 'link': f'https://docs.google.com/document/d/{document_id}'}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
