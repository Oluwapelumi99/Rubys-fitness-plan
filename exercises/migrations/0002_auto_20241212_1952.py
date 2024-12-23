# Generated by Django 3.2.25 on 2024-12-12 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='reps',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='sets',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='warm_up',
        ),
        migrations.AddField(
            model_name='exercise',
            name='reps1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='reps2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='reps3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='reps4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='sets1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='sets2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='sets3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='sets4',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
