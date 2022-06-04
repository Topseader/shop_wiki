# Generated by Django 4.0.4 on 2022-06-04 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='decription',
            field=models.TextField(default='', verbose_name='Decription'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='official_url',
            field=models.URLField(default='', verbose_name='Official URL'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='title',
            field=models.CharField(default='', max_length=64, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='wiredmicrophone',
            name='cable_detached',
            field=models.BooleanField(default=True, verbose_name='Cable detached'),
        ),
        migrations.AlterField(
            model_name='wiredmicrophone',
            name='color',
            field=models.CharField(max_length=32, verbose_name='Color'),
        ),
        migrations.AlterField(
            model_name='wiredmicrophone',
            name='connection_type',
            field=models.CharField(max_length=16, verbose_name='Connection type'),
        ),
        migrations.AlterField(
            model_name='wiredmicrophone',
            name='decription',
            field=models.TextField(blank=True, verbose_name='Decription'),
        ),
        migrations.AlterField(
            model_name='wiredmicrophone',
            name='diameter',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Diameter'),
        ),
        migrations.AlterField(
            model_name='wiredmicrophone',
            name='diaphragm_type',
            field=models.CharField(max_length=32, verbose_name='Diaphragm type'),
        ),
        migrations.AlterField(
            model_name='wiredmicrophone',
            name='impedance',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Impedance'),
        ),
        migrations.AlterField(
            model_name='wiredmicrophone',
            name='length',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Length'),
        ),
        migrations.AlterField(
            model_name='wiredmicrophone',
            name='manual_url',
            field=models.URLField(default='', verbose_name='Manual URL'),
        ),
        migrations.AlterField(
            model_name='wiredmicrophone',
            name='on_off_switch',
            field=models.BooleanField(default=False, verbose_name='On-off switch'),
        ),
        migrations.AlterField(
            model_name='wiredmicrophone',
            name='polar_pattern',
            field=models.CharField(max_length=32, verbose_name='Polar pattern'),
        ),
        migrations.AlterField(
            model_name='wiredmicrophone',
            name='polar_pattern_switch',
            field=models.BooleanField(default=False, verbose_name='Polar pattern switch'),
        ),
        migrations.AlterField(
            model_name='wiredmicrophone',
            name='require_phantom_power',
            field=models.BooleanField(default=False, verbose_name='Require phantom power'),
        ),
        migrations.AlterField(
            model_name='wiredmicrophone',
            name='sku',
            field=models.SlugField(max_length=7, verbose_name='SKU'),
        ),
        migrations.AlterField(
            model_name='wiredmicrophone',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='wiredmicrophone',
            name='warranty_years',
            field=models.PositiveSmallIntegerField(default=2, verbose_name='Warranty years'),
        ),
    ]