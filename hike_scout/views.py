from rest_framework.decorators import api_view
from rest_framework.response import Response
from .settings import (
    JWT_AUTH_COOKIE,
    JWT_AUTH_REFRESH_COOKIE,
    JWT_AUTH_REFRESH_COOKIE,
    JW_AUTH_SAMESITE
)

@api_view()
def root_route(request):
    return Response({
        'message' : 'Welcome to hike scout api'
    })

@api_view(['POST'])
def logout_route(request):
    response = Response()
    response.set_cookie(
        key = JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JW_AUTH_SAMESITE,
        secrure=JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JW_AUTH_SAMESITE,
        secrure=JWT_AUTH_SECURE,
    )
    return response