from django.contrib import admin

from tasks_app.models import Location, Task

admin.site.register(Task)
admin.site.register(Location)
# Register your models here.
