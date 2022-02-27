from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from realtor.models import Realtor
from currency.models import Currencies
from region.models import Region

# Create your models here.
FUNISHED_STATE = {
    ('FF', 'Fully Furnished'),
    ('SF', 'Semi Furnished'),
    ('NF', 'Not Furnished'),
}


def create_slug(title):  # new
    slug = slugify(title)
    qs = Listing.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        slug = "%s-%s" % (slug, qs.first().id)
    return slug


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE, related_name='listings')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=150)
    region = models.ForeignKey(Region, on_delete=models.DO_NOTHING)
    city = models.CharField(max_length=100)
    currency = models.ForeignKey(Currencies, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=50, decimal_places=2, blank=True)
    price_per_month = models.DecimalField(max_digits=50, decimal_places=2, blank=True)
    negotiable = models.BooleanField(default=False)
    bedrooms = models.IntegerField(blank=True, null=True)
    square_size = models.IntegerField(blank=True, null=True)
    lot_size = models.FloatField(blank=True, null=True)
    garage = models.BooleanField(default=False)
    swimming_pool = models.BooleanField(default=False)
    boys_quarters = models.BooleanField(default=False)
    furnished = models.BooleanField(default=False)
    furnished_state = models.CharField(max_length=20, choices=FUNISHED_STATE, blank=True)
    main_image = models.ImageField(upload_to='main_image_property/&Y/&m/&d/')
    main_image_1 = models.ImageField(upload_to='main_image_1_property/&Y/&m/&d/', blank=True)
    main_image6 = models.ImageField(upload_to='main_image_property/&Y/&m/&d/', blank=True)
    main_image5 = models.ImageField(upload_to='main_image_property/&Y/&m/&d/', blank=True)
    main_image4 = models.ImageField(upload_to='main_image_property/&Y/&m/&d/', blank=True)
    main_image3 = models.ImageField(upload_to='main_image_property/&Y/&m/&d/', blank=True)
    image2 = models.ImageField(upload_to='main_image_property/&Y/&m/&d/', blank=True)
    property_video = models.FileField(upload_to='videos_uploaded_properties', null=True, blank=True,
                                      validators=[
                                          FileExtensionValidator(
                                              allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    floor_plan = models.ImageField(upload_to='floor_plan', blank=True)
    first_floor = models.ImageField(upload_to='first_floor', blank=True)
    published = models.BooleanField(default=True)
    newly_built = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('listing_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = create_slug(self.title)
        return super().save(*args, **kwargs)

    # def __unicode__(self):
    #     return '%d: %s' % (self.description, self.title)
