from django.db import models

class Threat(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class RiskTreatment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class Safeguard(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    threats = models.ManyToManyField(Threat, related_name='safeguards', blank=True)
    treatment = models.ForeignKey(RiskTreatment, on_delete=models.CASCADE, related_name='safeguards', null=True, blank=True)

    def __str__(self):
        return self.name