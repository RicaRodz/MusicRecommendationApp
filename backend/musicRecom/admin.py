# Register your models here.
from django.contrib import admin
from .models import SongRecomendation
from .models import SongInput


# Register your models here.
admin.site.register(SongRecomendation)
admin.site.register(SongInput)