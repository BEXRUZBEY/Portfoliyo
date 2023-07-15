from django.db import models


class Skill(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    image = models.ImageField(upload_to='blog/')
    title = models.CharField(max_length=155)
    user = models.ForeignKey(to='auth.User', on_delete=models.CASCADE, related_name='blogs')
    text = models.TextField()

    def __str__(self):
        return self.title



class Contact(models.Model):
    username = models.CharField(max_length=155)
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.email