from django.db import models
from assessment_app.models import Assessment

class ComplianceReport(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    report_data = models.TextField()  # Consider using JSONField for structured data
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Compliance Report for Assessment {self.assessment.id}"