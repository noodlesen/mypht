# Generated by Django 3.0.5 on 2020-05-15 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0009_auto_20200515_1508'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='group',
            new_name='groups',
        ),
    ]
