from os import stat
from rest_framework import generics, status
from rest_framework.response import Response


class AppOrder(generics.GenericAPIView):
    def get(self, request):
        return Response(
            data={'message', 'Order App Test'},
            status=status.HTTP_200_OK
            )
        