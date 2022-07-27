from django.contrib import admin

# Register your models here.
from first_site.models import Event, Question, Choice

admin.site.register(Event)
admin.site.register(Question)
admin.site.register(Choice)
