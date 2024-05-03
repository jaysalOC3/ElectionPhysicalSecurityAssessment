# Generated by Django 5.0.4 on 2024-04-26 19:01

import assessment_app.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("assessment_app", "0004_alter_assessmentquestion_assessment_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="AssessmentQuestionCollection",
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
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="assessmentquestion",
            name="assessment",
        ),
        migrations.AddField(
            model_name="assessmentquestion",
            name="collection",
            field=models.ForeignKey(
                default=assessment_app.models.get_default_collection,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="questions",
                to="assessment_app.assessmentquestioncollection",
            ),
        ),
    ]