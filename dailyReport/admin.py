from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(MorningEntry)
admin.site.register(RawMaterialRecieved)
admin.site.register(EndOfDayReport)
admin.site.register(Disribution)
admin.site.register(Pastries)
admin.site.register(FullReport)