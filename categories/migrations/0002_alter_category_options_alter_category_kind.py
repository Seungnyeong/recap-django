# Generated by Django 4.1 on 2022-09-25 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
        migrations.AlterField(
            model_name="category",
            name="kind",
            field=models.CharField(
                choices=[("rooms", "Rooms"), ("experiences", "Experiences")],
                max_length=15,
            ),
        ),
    ]
