# Generated by Django 3.0.5 on 2020-05-12 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='intake',
            name='weight',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='fiber',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='holes',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='is_meta',
            field=models.BooleanField(default=None),
        ),
        migrations.AddField(
            model_name='product',
            name='kali',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='nat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='nfat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='source',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='sugar',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='meal',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='foodapp.Person'),
        ),
        migrations.AlterField(
            model_name='product',
            name='carb',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='fat',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='kkal',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='prot',
            field=models.FloatField(null=True),
        ),
        migrations.CreateModel(
            name='RecipePart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField(null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.Product')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='ProductToPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intakes_list', models.TextField(null=True)),
                ('intakes_count', models.IntegerField(default=0)),
                ('wmin', models.IntegerField()),
                ('wmax', models.IntegerField()),
                ('wawg', models.IntegerField()),
                ('w_typ', models.TextField(null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.Person')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(null=True)),
                ('product1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product1', to='foodapp.Product')),
                ('product2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product2', to='foodapp.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.Person')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.Product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='foodapp.Brand'),
        ),
    ]