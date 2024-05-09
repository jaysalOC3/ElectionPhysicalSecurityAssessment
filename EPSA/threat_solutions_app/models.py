from django.db import models

class Threat(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class ThreatMitigation(models.Model):
    name = models.CharField(max_length=100)
    threat = models.ForeignKey(Threat, on_delete=models.CASCADE, related_name='ThreatMitigation', null=True, blank=True)
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
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='safeguards_vendor', null=True, blank=True)
    description = models.TextField()
    threats = models.ManyToManyField(ThreatMitigation, related_name='safeguards_threats', blank=True)
    treatment = models.ForeignKey(RiskTreatment, on_delete=models.CASCADE, related_name='safeguards_treatment', null=True, blank=True)

    def __str__(self):
        return self.name