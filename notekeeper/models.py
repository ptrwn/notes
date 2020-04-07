import uuid
from django.utils import timezone
from django.db import models



CATEGORY_CHOICES= [
    ('link', 'Link'),
    ('note', 'Note'),
    ('memo', 'Memo'),
    ('todo', 'To do'),
    ]


class Note(models.Model):
    header = models.CharField(max_length=200)
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.header




