from rest_framework import status as rest_status
from rest_framework.response import Response

def response_success(data=None):
    http_status = rest_status.HTTP_200_OK if data is not None else rest_status.HTTP_204_NO_CONTENT
    return Response(data, status=http_status)

def response_failed(error=None, status_code=rest_status.HTTP_400_BAD_REQUEST):
    data = {'message': error}
    return Response(data, status=status_code)