from django.contrib import admin
from .models import GeneratedContent, UserApiUsage, Feedback

# Register your models here.
admin.site.register(GeneratedContent)
admin.site.register(UserApiUsage)
admin.site.register(Feedback)