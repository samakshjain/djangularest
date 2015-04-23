from django.db import models

# Create your models here.
from authentication.models import Account

from django.forms import ModelForm
def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class Post(models.Model):
    author = models.ForeignKey(Account)
    content = models.TextField()
    pic = models.ImageField(upload_to=get_image_path, blank=True, null=True)    
    upload_date = models.DateTimeField(auto_now_add =True)

    def __unicode__(self):
        return '{0}'.format(self.content)
