from turtle import home
from typing import Generic
from urllib import response
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
# Create your views here.


from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework import serializers
from .serializers import RegistrationSerializer
import uuid
from rest_framework import status
from rest_framework import generics


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})





class RegistrationAPIView(generics.GenericAPIView):
     serializer_class = RegistrationSerializer

     def post(self, request):
        if request.method == 'POST':
         serializer = self.get_serializer(data = request.data)
         # serializer.is_valid(raise_exception = True)
         # serializer.save()
         if(serializer.is_valid()):
            serializer.save()
            return Response({
                "RequestId": str(uuid.uuid4()),
                "Message": "User created successfully",
                
                "User": serializer.data}, status=status.HTTP_201_CREATED
                )

        #  return render('dashboard/home.html')
        
         return Response({"Errors": serializers.errors}, status=status.HTTP_400_BAD_REQUEST)




