
from django.http.response import Http404
from django.shortcuts import render
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view, parser_classes,authentication_classes,permission_classes
from rest_framework.views import APIView
from .models import account
from .serializers import UserDataSerializer, UserRegister
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework import mixins


# Create your views here.


class RegistersViews(generics.CreateAPIView):
    serializer_class = UserRegister
    parser_classes = [MultiPartParser, FormParser]
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserRegister(user,context=self.get_serializer_context()).data,
            "message": "Registered Successfully.  Now perform Login to get your token",
        })


    def get_parsers(self):
        if getattr(self, 'swagger_fake_view', False):
            return []
        return super().get_parsers()     



class   UsersLists(APIView):
    permission_classes = [IsAdminUser]
    def get(self,request):
        user = account.objects.all()
        serializer = UserDataSerializer(user,many=True)
        return Response(serializer.data)

    def get_parsers(self):
        if getattr(self, 'swagger_fake_view', False):
            return []
        return super().get_parsers()    


class UserDetails(APIView):
    permission_classes = [IsAdminUser]

    def get_id(self,pk):
        return account.objects.get(pk=pk)
        
    def get(self,request,pk):
        user = self.get_id(pk)
        serializer = UserDataSerializer(user)
        return Response(serializer.data)
    
    
    def put(self,request,pk):
        user = self.get_id(pk)
        serializer = UserDataSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'data updated successfully'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self,request,pk):
        user = self.get_id(pk)
        user.delete()
        return Response({'message':'user deleted'})

    def get_parsers(self):
        if getattr(self, 'swagger_fake_view', False):
            return []
        return super().get_parsers()      
    
    
    
    
    
class getView(APIView):
    def get(self,request):
        data = account.objects.all()
        serializer = UserDataSerializer(data, many=True)
        return Response(serializer.data)

    def get_parsers(self):
        if getattr(self, 'swagger_fake_view', False):
            return []
        return super().get_parsers()    


class RegisterView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    def post(self,request):
        serializer = UserRegister(data=request.data)
        
        data = {}

        if serializer.is_valid(raise_exception=True):
            reg = serializer.save()
            
            data['response'] = "Registered Successfully"
            data['full_name'] = reg.full_name
            data['phone_number'] = reg.phone_number
            data['email'] = reg.email
            data['dob'] = reg.dob
            data['profile_picture'] = reg.profile_picture
            
            refresh = RefreshToken.for_user(reg)
            data['token'] = {
                                'refresh': str(refresh),
                                'access': str(refresh.access_token),
                            }
        else:
            data = serializer.errors
        return Response(data)

    def get_parsers(self):
        if getattr(self, 'swagger_fake_view', False):
            return []
        return super().get_parsers()
