from django.contrib import admin
from emallapp.models import Register,payment,nearestloc,Category

# Register your models here.

admin.site.register(Register)
admin.site.register(payment)
admin.site.register(nearestloc)
admin.site.register(Category)
