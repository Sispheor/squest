# Generated by Django 3.2.13 on 2023-07-24 07:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('profiles', '0015_profile_theme'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='abstractscope',
            options={'default_permissions': ('add', 'change', 'delete', 'view', 'list')},
        ),
        migrations.AlterModelOptions(
            name='globalpermission',
            options={'default_permissions': ('add', 'change', 'delete', 'view', 'list'),
                     'permissions': [('view_users_globalpermission', 'Can view users in global permission'),
                                     ('add_users_globalpermission', 'Can add users in global permission'),
                                     ('delete_users_globalpermission', 'Can delete users in global permission')]},
        ),
        migrations.AlterModelOptions(
            name='organization',
            options={'default_permissions': ('add', 'change', 'delete', 'view', 'list'),
                     'permissions': [('view_users_organization', 'Can view users in organization'),
                                     ('add_users_organization', 'Can add users in organization'),
                                     ('delete_users_organization', 'Can delete users in organization')]},
        ),
        migrations.AlterModelOptions(
            name='quota',
            options={'default_permissions': ('add', 'change', 'delete', 'view', 'list')},
        ),
        migrations.AlterModelOptions(
            name='rbac',
            options={'default_permissions': ('add', 'change', 'delete', 'view', 'list')},
        ),
        migrations.AlterModelOptions(
            name='role',
            options={'default_permissions': ('add', 'change', 'delete', 'view', 'list')},
        ),
        migrations.AlterModelOptions(
            name='scope',
            options={'default_permissions': ('add', 'change', 'delete', 'view', 'list'),
                     'permissions': [('consume_quota_scope', 'Can consume quota of the scope')]},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'default_permissions': ('add', 'change', 'delete', 'view', 'list'),
                     'permissions': [('view_users_team', 'Can view users in team'),
                                     ('add_users_team', 'Can add users in team'),
                                     ('delete_users_team', 'Can delete users in team')]},
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='support_notification_enabled',
            new_name='instance_notification_enabled',
        ),
        migrations.RemoveField(
            model_name='abstractscope',
            name='roles',
        ),
        migrations.AddField(
            model_name='globalpermission',
            name='default_permissions',
            field=models.ManyToManyField(blank=True, help_text='Permissions assigned to all users without exception.',
                                         limit_choices_to={
                                             'content_type__app_label__in': ['service_catalog', 'profiles',
                                                                             'resource_tracker_v2', 'auth']},
                                         to='auth.Permission'),
        ),
        migrations.AddField(
            model_name='scope',
            name='roles',
            field=models.ManyToManyField(blank=True, help_text='The roles assigned to the scope.',
                                         related_name='scopes', related_query_name='scopes', to='profiles.Role',
                                         verbose_name='Default roles'),
        ),
        migrations.AlterField(
            model_name='role',
            name='permissions',
            field=models.ManyToManyField(blank=True, help_text='Permissions linked to this role.', limit_choices_to={
                'content_type__app_label__in': ['service_catalog', 'profiles', 'resource_tracker_v2', 'auth']},
                                         to='auth.Permission'),
        ),
    ]