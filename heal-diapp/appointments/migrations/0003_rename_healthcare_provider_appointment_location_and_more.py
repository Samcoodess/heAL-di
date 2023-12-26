# Generated by Django 5.0 on 2023-12-26 06:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("appointments", "0002_appointment_notes"),
    ]

    operations = [
        migrations.RenameField(
            model_name="appointment",
            old_name="healthcare_provider",
            new_name="location",
        ),
        migrations.RemoveField(
            model_name="appointment",
            name="notes",
        ),
        migrations.AddField(
            model_name="appointment",
            name="age",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="appointment",
            name="confirmation_message",
            field=models.TextField(default="Your appointment is confirmed"),
        ),
        migrations.AddField(
            model_name="appointment",
            name="name",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="appointment",
            name="note",
            field=models.TextField(default="I will call"),
        ),
        migrations.AlterField(
            model_name="appointment",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
