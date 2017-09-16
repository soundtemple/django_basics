from django.db import models

# Create your models here.


class Course(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    # used to display object names when printed
    def __str__(self):
        return self.title

class Step(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course)
    content = models.TextField(blank=True, default='')

    class Meta:
        ordering = ['order',]


    def __str__(self):
        return self.title

