from django.db import models
from django.contrib.auth.models import User
from student.models import StudentProfile


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return "%s - %s "%(self.pk, self.title)


class Post(models.Model):
    description = models.TextField()
    category = models.ForeignKey(Category)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='likes')

    def get_author_campus_name(self):
        campus_name=StudentProfile.objects.get(user=self.author).campus.name
        return campus_name

    @property
    def total_likes(self):
        '''
        likes for blog post
        :return:Integer: total like count
        '''
        return self.likes.count()

    def __str__(self):
        return str(self.pk)
