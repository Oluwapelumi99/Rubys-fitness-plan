# Generated by Django 3.2.25 on 2024-12-14 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='color',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]