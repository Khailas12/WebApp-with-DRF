
from rest_framework import generics, status
from rest_framework.response import Response

from .models import AppOrder
from .serializers import AppOrderSeraializer


class AppOrder(generics.GenericAPIView):
    def get(self, request):
        return Response(
            data={'message', 'Order App Test'},
            status=status.HTTP_200_OK
            )
        
        
class AppOrderCreate(generics.ListCreateAPIView):
    queryset = AppOrder
    serializer_class = AppOrderSeraializer
    

class AppOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppOrder
    serializer_class = AppOrderSeraializer