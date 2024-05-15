# Generated by Django 5.0.4 on 2024-05-15 03:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("threat_solutions_app", "0005_threatmitigation_vendor_description_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="safeguard",
            name="threats",
        ),
        migrations.RemoveField(
            model_name="safeguard",
            name="treatment",
        ),
        migrations.AddField(
            model_name="safeguard",
            name="risk_treatment",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="threat_solutions_app.risktreatment",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="safeguard",
            name="threat_mitigations",
            field=models.ManyToManyField(
                blank=True,
                related_name="safeguards",
                to="threat_solutions_app.threatmitigation",
            ),
        ),
        migrations.AlterField(
            model_name="safeguard",
            name="vendor",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="safeguards",
                to="threat_solutions_app.vendor",
            ),
        ),
        migrations.AlterField(
            model_name="threatmitigation",
            name="threat",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="mitigations",
                to="threat_solutions_app.threat",
            ),
            preserve_default=False,
        ),
    ]