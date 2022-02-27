from django.contrib import admin
from listings.models import Listing
from realtor.models import Realtor
from currency.models import Currencies
from region.models import Region


# Register your models here.
@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ['realtor', 'title', 'created_at', 'published']
    search_fields = ['realtor', 'title', 'city']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    list_display = ['name_of_agency', 'phone_number']
    search_fields = ['name_of_agency']
    prepopulated_fields = {'slug': ('name_of_agency',)}


@admin.register(Currencies)
class CurrAdmin(admin.ModelAdmin):
    list_display = ['currency_code', 'currency_symbol']



@admin.register(Region)
class RegAdmin(admin.ModelAdmin):
    list_display = ['region_name']