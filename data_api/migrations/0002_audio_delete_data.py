# Generated by Django 4.1.4 on 2022-12-29 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data_api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Audio",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("audio_file", models.FileField(upload_to="")),
            ],
        ),
        migrations.DeleteModel(name="Data",),
    ]