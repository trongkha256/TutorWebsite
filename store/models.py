from django.conf import settings
from django.db import models
from django.urls import reverse


class CourseManager(models.Manager):
    def get_queryset(self):
        return super(CourseManager, self).get_queryset().filter(is_active=True)


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.name


class Course(models.Model):
    category = models.ForeignKey(Category, related_name='course', on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='course_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default='images/default.png')
    slug = models.SlugField(max_length=255)
    price = models.BigIntegerField()
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    courses = CourseManager()

    class Meta:
        verbose_name_plural = 'courses'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('store:course_detail', args=[self.slug])

    def __str__(self):
        return self.title
