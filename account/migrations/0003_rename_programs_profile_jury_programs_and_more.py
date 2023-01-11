# Generated by Django 4.1.4 on 2023-01-11 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0003_remove_businessunit_jury_businessunit_jury'),
        ('account', '0002_rename_jury_programs_profile_programs_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='programs',
            new_name='jury_programs',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='business_units',
        ),
        migrations.AddField(
            model_name='profile',
            name='jury_business_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='program.businessunit'),
        ),
    ]
