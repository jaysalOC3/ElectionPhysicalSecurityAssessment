from django.contrib import admin
from .models import Threat, ThreatMitigation, Safeguard, RiskTreatment, Vendor

admin.site.register(Threat)
admin.site.register(ThreatMitigation)
admin.site.register(Safeguard)
admin.site.register(RiskTreatment)
admin.site.register(Vendor)
