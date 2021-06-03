from rest_framework import serializers
from .models import myimage

class myimageserializer(serializers.ModelSerializer):
    
    class Meta:
        model =myimage
        fields=('id','my_id','my_name','my_image')
