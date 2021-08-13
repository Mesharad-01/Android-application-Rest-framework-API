from re import M
from django.shortcuts import render
from .models import myimage
from rest_framework import views
from .serializers import myimageserializer
import django_filters.rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import os
from apitask.settings import BASE_DIR

class myimageView(APIView):
   
    def get(self, request):
        myimagelocal= myimage.objects.all()
        serializer = myimageserializer(myimagelocal, many=True)
        return Response(serializer.data)
  
    def post(self, request):
        my_id = request.data['my_id']
        image_exist =  myimage.objects.filter(my_id=my_id)
        
        #print(is_image_exist)
        if not image_exist :
            myname=request.data['my_image'].name
            myformat=""
            for c in reversed(myname):
                myformat+=c
                if c=='.' :
                    break
            myformat=myformat[: : -1]
            request.FILES['my_image'].name = request.data['my_name']+myformat
        
            serializer = myimageserializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response( status=status.HTTP_404_NOT_FOUND)
        

class myimagedetailsView(APIView):
    def get_object(self, id):
        try:
            return myimage.objects.get(id=id)
        except myimage.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
 
    def get(self, request, id):
        myimage_id = self.get_object(id)
        serializer =  myimageserializer(myimage_id)
        return Response(serializer.data)

    def put(self, request,id):
        myimage_id = self.get_object(id)

        myname=request.data['my_image'].name
        myformat=""
        for c in reversed(myname):
            myformat+=c
            if c=='.' :
                break
        myformat=myformat[: : -1]
        request.FILES['my_image'].name=request.data['my_id']+myformat
        serializer =  myimageserializer(myimage_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, id):
        myimage_id = self.get_object(id)
        myimage_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class allmyimagedetailsView(APIView): 


    # used in deleting all images in folder
    def get(self, request,my_id):
        m=myimage.objects.filter(my_id=my_id)
        serializer = myimageserializer(m,many=True)
        print(serializer.data)
        return Response(serializer.data)



    #deleting all images in folder and deleting empty folder in directory
    
    def delete(self, request, my_id):
        m=myimage.objects.filter(my_id=my_id)
        if not m :
            return Response(status=status.HTTP_404_NOT_FOUND)
        m.delete()

        REPOSITORY_ROOT = os.path.dirname(BASE_DIR)
        for root, dirs, files in os.walk(os.path.join(REPOSITORY_ROOT, 'media/images')):
            for d in dirs:
                dir = os.path.join(root, d)
                # check if dir is empty
                if not os.listdir(dir):
                    os.rmdir(dir)
        return Response(status=status.HTTP_204_NO_CONTENT)

    


