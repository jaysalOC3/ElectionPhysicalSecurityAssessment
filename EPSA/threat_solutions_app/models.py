from django.db import models

class Threat(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class ThreatMitigation(models.Model):
    name = models.CharField(max_length=100)
    threat = models.ForeignKey(Threat, on_delete=models.CASCADE, related_name='mitigations')  
    vendor_description = models.TextField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class RiskTreatment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Safeguard(models.Model):
    name = models.CharField(max_length=100)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='safeguards', null=True, blank=True)
    description = models.TextField()
    threat_mitigations = models.ManyToManyField(ThreatMitigation, related_name='safeguards', blank=True)
    risk_treatment = models.ForeignKey(RiskTreatment, on_delete=models.CASCADE)

    def __str__(self):
        return self.name