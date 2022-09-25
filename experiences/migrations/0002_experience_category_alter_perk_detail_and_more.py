# Generated by Django 4.1 on 2022-09-25 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0001_initial"),
        ("experiences", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="experience",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="categories.category",
            ),
        ),
        migrations.AlterField(
            model_name="perk",
            name="detail",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name="perk",
            name="explanation",
            field=models.TextField(blank=True, null=True),
        ),
    ]
