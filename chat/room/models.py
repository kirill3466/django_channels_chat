from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField('URL', null=True, editable=False)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Room, self).save(*args, **kwargs)


class Message(models.Model):
    room = models.ForeignKey(
        Room, related_name='messages',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User, related_name='messages',
        on_delete=models.CASCADE
    )
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)

    def __str__(self) -> str:
        return self.name
