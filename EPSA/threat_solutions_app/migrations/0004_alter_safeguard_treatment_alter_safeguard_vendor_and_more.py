# Generated by Django 5.0.4 on 2024-05-09 01:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("threat_solutions_app", "0003_vendor_safeguard_vendor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="safeguard",
            name="treatment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="safeguards_treatment",
                to="threat_solutions_app.risktreatment",
            ),
        ),
        migrations.AlterField(
            model_name="safeguard",
            name="vendor",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="safeguards_vendor",
                to="threat_solutions_app.vendor",
            ),
        ),
        migrations.CreateModel(
            name="ThreatMitigation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "threat",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ThreatMitigation",
                        to="threat_solutions_app.threat",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="safeguard",
            name="threats",
            field=models.ManyToManyField(
                blank=True,
                related_name="safeguards_threats",
                to="threat_solutions_app.threatmitigation",
            ),
        ),
    ]