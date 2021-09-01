from django.contrib import admin

# Register your models here.
from .models import user_entry, category,roommaster,checkin,checkout
from home import models


admin.site.register(user_entry)
admin.site.register(category)
admin.site.register(roommaster)
admin.site.register(checkin)
admin.site.register(checkout)

