from django.db import models

#for deleting images associated with models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

def upload_path(instance,filename):
    return '/'.join(['images',str(instance.my_id),filename])

# Create your models here.
class myimage(models.Model):
    my_id=models.CharField(max_length=50)
    my_name=models.CharField(max_length=50)
    my_image=models.ImageField(blank=True, null =True, upload_to=upload_path)

    def __str__(self):
        return self.my_name
        
    #def delete(self, *args, **kwargs):
        #storage, path = self.my_image.storage, self.my_image.path
        #super(myimage, self).delete(*args, **kwargs)
        #storage.delete(path)
@receiver(pre_delete, sender=myimage)
def mymodel_delete(sender, instance, **kwargs):
    instance.my_image.delete(False)
    
  