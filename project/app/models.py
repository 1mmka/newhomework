from django.db import models

# Create your models here.
class TaskList(models.Model):
    title = models.CharField(max_length=32)
    body = models.TextField()
    status = models.BooleanField(default=False,null=False,blank=False)
    deadline = models.DateTimeField()

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return f'complete/{self.pk}'
    
    # def get_edit_id(self):
    #     return f'edit/{self.pk}'