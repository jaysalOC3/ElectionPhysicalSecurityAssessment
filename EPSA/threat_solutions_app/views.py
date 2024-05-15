from django.shortcuts import render
from django.http import JsonResponse
from .models import Threat, ThreatMitigation, RiskTreatment, Vendor, Safeguard

def risk_landscape_data(request):
    data = {
        "nodes": [],
        "links": []
    }

    threats = Threat.objects.all()
    mitigations = ThreatMitigation.objects.all()
    treatments = RiskTreatment.objects.all()
    vendors = Vendor.objects.all()
    safeguards = Safeguard.objects.all()

    # Create nodes for Threats, Mitigations, Treatments, Vendors, and Safeguards
    for obj_list, node_type in [(threats, 'Threat'), (mitigations, 'Mitigation'), 
                                (treatments, 'Treatment'), (vendors, 'Vendor'), (safeguards, 'Safeguard')]:
        for obj in obj_list:
            data["nodes"].append({"name": obj.name, "type": node_type})

    # Create links
    for safeguard in safeguards:
        for threat_mitigation in safeguard.threat_mitigations.all():
            data["links"].append({"source": threat_mitigation.name, "target": safeguard.name, "value": 1})  # Adjust 'value' as needed
        data["links"].append({"source": safeguard.name, "target": safeguard.risk_treatment.name, "value": 1})

    return JsonResponse(data)
