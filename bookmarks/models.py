from django.db import models

from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=60, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name', )
        verbose_name_plural = 'Categories'


class Link(models.Model):
    title = models.CharField(max_length=100, default='Title')
    slug = models.CharField(max_length=60, unique=True, null=True, blank=True)
    url = models.CharField(max_length=255, unique=True)
    rating = models.IntegerField(default=1)
    category = models.ForeignKey('Category')
    description = models.TextField(null=True,blank=True)
    tags = TaggableManager()
    submitted_by = models.CharField(max_length=100, default='')

    def __unicode__(self):
        return self.url

