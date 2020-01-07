# Generated by Django 2.2.6 on 2020-01-03 01:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpiweb', '0022_consolidate_location_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='exp_month_end',
            field=models.IntegerField(blank=True, help_text='Optional ending month range of when the product expires, if filled.', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)], verbose_name='Expiration End Month (Optional)'),
        ),
        migrations.AlterField(
            model_name='box',
            name='exp_month_start',
            field=models.IntegerField(blank=True, help_text='Optional starting month range of when the product expires, if filled.', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)], verbose_name='Expiration Start Month (Optional)'),
        ),
    ]