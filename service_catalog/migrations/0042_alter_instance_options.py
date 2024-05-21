# Generated by Django 4.2.13 on 2024-05-21 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_catalog', '0041_operation_validators'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instance',
            options={'default_permissions': ('add', 'change', 'delete', 'view', 'list'), 'ordering': ['-last_updated'], 'permissions': [('archive_instance', 'Can archive instance'), ('unarchive_instance', 'Can unarchive instance'), ('request_on_instance', 'Can request a day2 operation on instance'), ('admin_request_on_instance', 'Can request an admin day2 operation on instance'), ('view_admin_spec_instance', 'Can view admin spec on instance'), ('change_admin_spec_instance', 'Can change admin spec on instance'), ('rename_instance', 'Can rename instance'), ('change_requester_on_instance', 'Can change owner of the instance')]},
        ),
    ]