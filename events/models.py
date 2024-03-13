from django.db import models
from organizations.models import Organization
from django.utils.safestring import mark_safe

class Event(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    organizations = models.ManyToManyField(Organization)
    image = models.ImageField(upload_to='events/images/', blank=True, null=True)
    date = models.DateField()

    def get_users(self):
        users = []
        for org in self.organizations.all():
            users.extend(org.users.all())
        return users

    def image_thumbnail(self):
        if self.image:
            return mark_safe('<img src="%s" width="100" height="100" />' % self.image.url)
        else:
            return 'No image'

    image_thumbnail.short_description = 'Thumbnail'
    image_thumbnail.allow_tags = True

    def __str__(self):
        return self.title
