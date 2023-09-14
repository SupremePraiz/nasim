from django.contrib import admin
from . models import Profile

admin.site.site_header = "NASIMS"
admin.site.site_title = "nasims"

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_filter = ("other_name",)

model=[Profile,] 


admin.site.register(Profile)