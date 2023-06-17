from django.contrib import admin
from .models import Users, Queue, Operator

admin.site.register(Users)
admin.site.register(Queue)
admin.site.register(Operator)
