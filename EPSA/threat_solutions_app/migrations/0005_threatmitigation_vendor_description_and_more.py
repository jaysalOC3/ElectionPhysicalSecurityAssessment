# Generated by Django 5.0.4 on 2024-05-09 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "threat_solutions_app",
            "0004_alter_safeguard_treatment_alter_safeguard_vendor_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="threatmitigation",
            name="vendor_description",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="threatmitigation",
            name="description",
            field=models.TextField(blank=True),
        ),
    ]
