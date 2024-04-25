from django.contrib import admin
from .models import UserRole, Comment, NotificationPreference

admin.site.register(UserRole)
admin.site.register(Comment)
admin.site.register(NotificationPreference)
