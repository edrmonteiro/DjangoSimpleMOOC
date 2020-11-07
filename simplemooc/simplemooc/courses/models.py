from django.db import models

class CourseManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(description__icontains=query)
        )


class Course(models.Model):
    name = models.CharField('Name', max_length=100)
    slug = models.SlugField('Shortcut')
    description = models.TextField('Short description', blank=True)
    about = models.TextField('About the course', blank=True)
    start_date = models.DateField(
        'Start date', null=True, blank=True
    )
    image = models.ImageField(
        upload_to = 'courses/images', 
        verbose_name='Image',
        null=True, blank=True
    )
    created_at = models.DateTimeField("Created at", auto_now_add=True)  #when the object is created
    updated_at = models.DateTimeField("Created at", auto_now=True)      #when there is any change in the object

    objects = CourseManager()
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return 'courses/details/' + self.slug

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ['name']