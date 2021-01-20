from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.views import JSONWebTokenAPIView

# Create your views here.
from jwtapp.serializer import UserModelSerializer


class LoginAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        # 账号使用account接收 密码使用pwd
        serializer = UserModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({
            "user": UserModelSerializer(serializer.obj).data,
            "token": serializer.token
        })
