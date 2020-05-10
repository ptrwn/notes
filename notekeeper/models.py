import uuid
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Note(models.Model):
    header = models.CharField(max_length=200)
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    uuid = models.UUIDField(null=True, editable=False)
    created_by = models.ForeignKey(User, related_name='own_note', on_delete=models.CASCADE)
    is_favorite = models.BooleanField(default=False)
    category = models.ForeignKey(Category, blank=False, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.header

    def add_uuid(self):
        self.uuid = uuid.uuid4()
        self.save()
        return self.uuid

    def del_uuid(self):
        self.uuid = None
        self.save()

    # def make_favorite(self):
    #     self.is_favorite = True
    #     self.save()
    #     return self.is_favorite
    #
    # def make_not_favorite(self):
    #     self.is_favorite = False
    #     self.save()
    #     return self.is_favorite

