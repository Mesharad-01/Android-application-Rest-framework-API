from django.db import models


# Create your models here.
class myimage(models.Model):
    my_id=models.CharField(max_length=50)
    my_name=models.CharField(max_length=50)
    my_image=models.ImageField(upload_to='Images/',default='Images/None/No-img.jpg')

    def __str__(self):
        return self.my_name
        
    def delete(self, *args, **kwargs):
        storage, path = self.my_image.storage, self.my_image.path
        super(myimage, self).delete(*args, **kwargs)
        storage.delete(path)
  