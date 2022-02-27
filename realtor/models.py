from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify  # new


# from phone_field import PhoneField


# Create your models here.

def create_slug(name_of_agency):  # new
    slug = slugify(name_of_agency)
    qs = Realtor.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        slug = "%s-%s" % (slug, qs.first().id)
    return slug


class Realtor(models.Model):
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=100, blank=True)
    name_of_agency = models.CharField(max_length=100)
    photo = models.ImageField(blank=True, upload_to='Realtor/&Y/&m/&d/')
    phone_number = models.CharField(blank=True, max_length=15, help_text='Contact phone number')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    mvp = models.BooleanField(default=False)

    def __str__(self):
        return self.name_of_agency

    def get_absolute_url(self):
        return reverse('realtor_details', kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = create_slug(self.name_of_agency)
        return super().save(*args, **kwargs)
