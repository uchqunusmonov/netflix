from django.contrib import admin
from .models import (
    CustomUser,
    Movie,
    Video,
    Profile,
)

admin.site.register(CustomUser)
admin.site.register(Movie)
admin.site.register(Video)
admin.site.register(Profile)