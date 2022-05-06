from django.contrib import admin

from .models import *

admin.site.register(Survey)
admin.site.register(Element)
admin.site.register(FilledSurvey)
admin.site.register(ElementValue)