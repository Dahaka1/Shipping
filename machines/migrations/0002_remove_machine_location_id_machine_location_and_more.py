# Generated by Django 4.2.1 on 2023-05-29 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        ('machines', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machine',
            name='location_id',
        ),
        migrations.AddField(
            model_name='machine',
            name='location',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='locations.location'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='tonnage',
            field=models.PositiveSmallIntegerField(default=114),
        ),
        migrations.AlterField(
            model_name='machine',
            name='uid',
            field=models.CharField(default='9259J', max_length=5, unique=True),
        ),
    ]