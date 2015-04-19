from django.db import models

# Create your models here.
from authentication.models import Account

from django.forms import ModelForm
class Post(models.Model):
    author = models.ForeignKey(Account)
    content = models.TextField()
    pic = models.ImageField("Image", upload_to="images/")    
    upload_date = models.DateTimeField(auto_now_add =True)

    def __unicode__(self):
        return '{0}'.format(self.content)
class UploadPost(ModelForm):
    class Meta:
        model = Post        