# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Log in Model for database uses Email, Username and Password


class LoginDB(models.Model):
    user_name = models.CharField('User_Name', max_length=60)
    email = models.CharField('Email', max_length=60)
    password = models.CharField('Password', max_length=10)

    def __str__(self):
        return self.user_name
# def str returns the name or a title for an entry
# this allows us to see the name of the user in our django admin dash~
