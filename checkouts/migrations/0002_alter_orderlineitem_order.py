# Generated by Django 4.2 on 2025-01-03 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkouts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='checkouts.order'),
        ),
    ]