from django.db import models

class Category(models.Model):
    name = models.CharField(u'Name', max_length=50)

    def __unicode__(self):
        return self.name

class User(models.Model):
    username = models.CharField(u'Username', max_length=50)
    account = models.CharField(u'Account', max_length=50)
    password = models.CharField(u'Password', max_length=50)

    def __unicode__(self):
        return self.account

class Article(models.Model):
    content = models.TextField(u'Content')
    title = models.CharField(u'Title', max_length=50)
    category = models.ForeignKey('Category',on_delete=models.CASCADE, blank=True, null=True)
    account = models.ForeignKey('User',on_delete=models.CASCADE, blank=True, null=True)
    
    def __unicode__(self):
        return self.title


# Create your models here.
