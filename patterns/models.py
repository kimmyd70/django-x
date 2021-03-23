from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Pattern(models.Model):
    name = models.CharField(max_length = 64)
    description = models.TextField(default = '')
    added_by = models.ForeignKey(get_user_model(),on_delete = models.CASCADE)
    category = models.TextField(default = '')
    more_info = models.URLField(default = '')
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("pattern_detail", args=[str(self.id)])
 
    # I started to make the more_info clickable, 
    # but got down a rabbit hole...need more research

    # def show_more_info(self, obj):
    #     return '<a href="%s">%s</a>' % (obj.more_info, obj.more_info)
    # show_more_info.allow_tags = True