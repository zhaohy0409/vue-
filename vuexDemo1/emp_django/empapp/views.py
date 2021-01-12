from django.http import HttpResponse, JsonResponse
from rest_framework import status, mixins
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from empapp.models import User
# from empapp.serializer import UserSerializer, UserDeSerializer


# def mydefault2(obj):
#     # print(obj.date)
#     if isinstance(obj, User):
#         return {'id': obj.id, 'username': obj.username, 'userpassword': obj.userpassword, 'age': str(obj.age),
#                 'salay': str(obj.salay), 'date': str(obj.date)}
#
#
# def index(request):
#     user = list(User.objects.all())
#     # return HttpResponse('哈哈哈哈哈哈')
#     return JsonResponse(user, json_dumps_params={"default": mydefault2}, safe=False)
#
#
# def deluser(request):
#     user = request.GET.get("id")
#     try:
#         User.objects.get(pk=user).delete()
#         return HttpResponse('删除成功')
#     except:
#         return HttpResponse('删除失败')
#
#
# def getunpuser(request):
#     user_id = request.GET.get("id")
#     user = User.objects.filter(pk=user_id).first()
#     return JsonResponse(user, json_dumps_params={"default": mydefault2}, safe=False)
#
#
# def unpuser(request):
#     user_id = request.GET.get("id")
#     username = request.GET.get("username")
#     userpassword = request.GET.get("userpassword")
#     age = request.GET.get("age")
#     salay = request.GET.get("salay")
#     date = request.GET.get("date")
#     try:
#         user = User.objects.get(pk=user_id)
#         user.username = username
#         user.userpassword = userpassword
#         user.age = age
#         user.salay = salay
#         user.date = date
#         user.save()
#         return HttpResponse('修改成功')
#     except:
#         return HttpResponse('修改失败')
#
#
# def adduser(request):
#     username = request.GET.get("username")
#     userpassword = request.GET.get("userpassword")
#     age = request.GET.get("age")
#     salay = request.GET.get("salay")
#     date = request.GET.get("date")
#     try:
#         User.objects.create(username=username, userpassword=userpassword, age=age, salay=salay, date=date)
#         return HttpResponse('添加成功')
#     except:
#         return HttpResponse('添加失败')

# class UserAPIVIew(APIView):
#
#     def get(self, request, *args, **kwargs):
#         user_id = kwargs.get("id")
#         if user_id:
#             user_obj = User.objects.get(pk=user_id)
#             serializer = UserSerializer(user_obj).data
#             return Response({"results": serializer})
#         else:
#             user_all = User.objects.all()
#             user_ser = UserSerializer(user_all, many=True).data
#             return Response({"results": user_ser})
#
#     def post(self, request, *args, **kwargs):
#         request_data = request.data
#         print(request_data)
#         if not isinstance(request_data, dict) or request_data == {}:
#             return Response({"message": "请求参数有误"}, status=400)
#         serializer = UserDeSerializer(data=request_data)
#         if serializer.is_valid():
#             user_obj = serializer.save()
#             return Response({"message": "创建成功",
#                              "results": UserDeSerializer(user_obj).data},
#                             status=status.HTTP_201_CREATED)
#         else:
#             return Response({"message": serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#     def delete(self,request, *args, **kwargs):
from empapp.serializer import UserDeMoDELSerializer
from utils.response import APIResponse


# class UserAPIVIew(APIView):
#
#     def get(self, request, *args, **kwargs):
#         user_id = kwargs.get("id")
#         # print(user_id)
#         if user_id:
#             user_obj = User.objects.get(pk=user_id)
#             serializer = UserDeMoDELSerializer(user_obj).data
#             return Response({"results": serializer})
#         else:
#             user_all = User.objects.all()
#             user_ser = UserDeMoDELSerializer(user_all, many=True).data
#             return Response({"results": user_ser})
#
#     def post(self, request, *args, **kwargs):
#         request_data = request.data
#         if isinstance(request_data, dict) or request_data != {}:
#             many = False
#         elif isinstance(request_data, list) or request_data != {}:
#             many = True
#         else:
#             return Response({"message": "请求参数有误"}, status=400)
#         serializer = UserDeMoDELSerializer(data=request_data, many=many)
#         serializer.is_valid(raise_exception=True)
#         user_obj = serializer.save()
#         return Response({"message": "创建成功",
#                          "results": UserDeMoDELSerializer(user_obj, many=many).data},
#                         status=status.HTTP_201_CREATED)
#
#     def delete(self, request, *args, **kwargs):
#         user_id = kwargs.get("id")
#         # print(user_id)
#         if user_id:
#             ids = [user_id]
#         else:
#             ids = request.data.get("ids")
#         try:
#             response = User.objects.get(pk__in=ids).delete()
#             return Response({
#                 "message": "删除成功",
#             }, status=status.HTTP_200_OK)
#
#         except:
#             return Response({
#                 "message": "删除失败或用户不存在",
#             }, status=status.HTTP_400_BAD_REQUEST)
#
#     def patch(self, raquest, *args, **kwargs):
#         request_data = raquest.data
#         print(request_data)
#         user_id = kwargs.get("id")
#         print(user_id)
#         try:
#             user_obj = User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return Response({
#                 "message": "修改的用户不存在"
#             }, status=status.HTTP_400_BAD_REQUEST)
#         serializer = UserDeMoDELSerializer(data=request_data, instance=user_obj, partial=True)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response({
#             "message": "修改成功",
#             "results": UserDeMoDELSerializer(user).data
#         }, status=status.HTTP_200_OK)


class UserGenericsAPIView(GenericAPIView,
                            ListModelMixin,
                            RetrieveModelMixin,
                            CreateModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserDeMoDELSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        if "id" in kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        response = self.create(request, *args, **kwargs)
        return APIResponse(results=response.data)

    def put(self, request, *args, **kwargs):
        response = self.update(request, *args, **kwargs)
        return APIResponse(results=response.data)

    def patch(self, request, *args, **kwargs):
        response = self.partial_update(request, *args, **kwargs)
        return APIResponse(results=response.data)

    def delete(self, request, *args, **kwargs):
        response = self.destroy(request, *args, **kwargs)
        return APIResponse(results=response.data)


class LoginViewSet(ViewSet):

    def login_count(self, request, *args, **kwargs):
        request_data = request.data
        print(request_data)
        user = request_data.user
        pwd = request_data.pwd
        user_login = User.objects.filter(username=user, userpassword=pwd)
        if user_login:
            return APIResponse(results=True, data_message="登陆成功")
        else:
            return APIResponse(results=False, data_message="登陆失败")
