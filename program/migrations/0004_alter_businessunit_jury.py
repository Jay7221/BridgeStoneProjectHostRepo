# Generated by Django 4.1.4 on 2023-01-11 04:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('program', '0003_remove_businessunit_jury_businessunit_jury'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessunit',
            name='jury',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
