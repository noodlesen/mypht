# Generated by Django 3.0.5 on 2020-05-13 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0006_remove_producttoperson_intakes_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttoperson',
            name='w_awg',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='producttoperson',
            name='w_max',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='producttoperson',
            name='w_min',
            field=models.IntegerField(default=0),
        ),
    ]
