# Generated by Django 3.0.5 on 2020-05-13 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0005_auto_20200513_1234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producttoperson',
            name='intakes_list',
        ),
    ]
