# Generated by Django 4.1.2 on 2022-12-15 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smbapp', '0014_remove_musician_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='musician',
            old_name='user_id',
            new_name='user',
        ),
    ]
