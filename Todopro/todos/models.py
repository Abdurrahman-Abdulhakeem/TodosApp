from django.db import models
from django.urls import reverse


# Create your models here.

class Todo(models.Model):
    todo_name = models.CharField(max_length=200)
    todo_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse('detail-todo', kwargs={'id':self.id})

    class Meta:
        ordering = ('-created_at',)



    def __str__(self):
        return self.todo_name


