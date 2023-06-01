from django.contrib import admin
from hats.api.hats_rest.models import Hat, LocationVO

# Register your models here.
@admin.register(Hat)
class HatAdmin(admin.ModelAdmin):
    pass

@admin.register(LocationVO)
class LocationVOAdmin(admin.ModelAdmin):
    pass
