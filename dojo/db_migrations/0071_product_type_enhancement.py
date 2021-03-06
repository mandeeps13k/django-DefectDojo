# Generated by Django 2.2.17 on 2021-01-02 15:06

from django.conf import settings
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dojo', '0070_increase_alert_field_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_type',
            name='description',
            field=models.CharField(max_length=4000, null=True),
        ),
        migrations.AddField(
            model_name='notifications',
            name='product_type_added',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('slack', 'slack'), ('msteams', 'msteams'), ('mail', 'mail'), ('alert', 'alert')], default='alert', max_length=24),
        ),
    ]
