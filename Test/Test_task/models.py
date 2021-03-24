from django.db import models
from django.utils import timezone


# class Groups(models.Model):
#     # ID = models.ForeignKey()? onetomany
#     name = models.CharField(max_length=50)
#     descriptions = models.CharField(max_length=200)
#
#     class Meta:
#         db_table = "Groups"
#     # def __str__(self):
#     #     return self.name


class Users(models.Model):
    username = models.CharField('User nickname', blank=True, default=0, max_length=50)
    created = models.DateField('Date of creating the user', default=timezone.now)
    group = models.CharField('select group', blank=True, default=0, max_length=50)#change to foreignkey?

    # actions

    class Meta:
        db_table = "Users"

    def __str__(self):
        return self.username
