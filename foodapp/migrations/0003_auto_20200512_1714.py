# Generated by Django 3.0.5 on 2020-05-12 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0002_auto_20200512_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_meta',
            field=models.BooleanField(default=False),
        ),
    ]
