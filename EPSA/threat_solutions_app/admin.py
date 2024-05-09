from django.contrib import admin
from .models import Threat, Safeguard, RiskTreatment

admin.site.register(Threat)
admin.site.register(Safeguard)
admin.site.register(RiskTreatment)
