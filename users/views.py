
from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework.response import Response

from .serializers import UserSerializer, ProfileSerializer, RegistrationSerializer
from .models import Profile

from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

#::::REGISTRATION:::
class RegistrationView(APIView):
    def post(self, request):
        try:
            serializer = RegistrationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

##;::LOGIN:::
class LoginView(APIView):
    def post(self, request):
        try:
            username = request.data.get("username")
            password = request.data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return Response({"Message": "User logged in successfully"}, status=status.HTTP_200_OK)
            return Response({"Message": "Username / password not match"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#::::LOGOUT::::
class LogoutView(APIView):
    def post(self, request):
        try:
            logout(request)
            return Response({"Message": "You have logged out successfully"})
        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#:::DASHBOARD:::
class DashboardView(APIView):
    def get(self, request):
        try:
            profile = request.user.profile
            # Assuming you want to show username or profile info
            return Response({"Message": f"Welcome {profile.user.username}"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)