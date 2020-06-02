# Generated by Django 3.0.5 on 2020-04-28 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('kkal', models.FloatField()),
                ('prot', models.FloatField()),
                ('fat', models.FloatField()),
                ('carb', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=255, null=True)),
                ('text', models.TextField(null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_number', models.IntegerField(null=True)),
                ('date', models.DateField(null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Intake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.Meal')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.Person')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='foodapp.Product')),
            ],
        ),
    ]