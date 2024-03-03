from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import CustomUser
from profiles.serializers import RegisterSerializer, UserSerializer
from rest_framework import status
from rest_framework.response import Response
# Create your views here.


class RegisterView(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(data=UserSerializer(user).data,
                        status=status.HTTP_201_CREATED)
