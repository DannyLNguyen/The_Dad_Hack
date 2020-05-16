from django.db import models

import re

# Create your models here.



class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 2:
            errors["name"] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["name"] = "Last name should be at least 2 characters"
        if len(postData['password']) < 8:
            errors["password"] = "password should be at least 8 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = ("Invalid email address!")
        return errors



class User(models.Model):
        first_name = models.CharField(max_length = 50)
        last_name = models.CharField(max_length = 50)
        email = models.CharField(max_length = 50)
        password = models.CharField(max_length = 50)
        objects = UserManager()
