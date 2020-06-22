from django.contrib import admin
from emallapp.models import Register,payment,nearestloc,Category,addproduct

# Register your models here.

admin.site.register(Register)
admin.site.register(payment)
admin.site.register(nearestloc)
admin.site.register(Category)
class proAdmin(admin.ModelAdmin):
    list_display = ("pname","price","stock")
admin.site.register(addproduct,proAdmin)

