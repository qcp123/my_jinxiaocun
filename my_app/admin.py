from django.contrib import admin

# Register your models here.


from my_app.models import *


admin.site.register(goods)
admin.site.register(customer)
admin.site.register(order)
admin.site.register(cangku)