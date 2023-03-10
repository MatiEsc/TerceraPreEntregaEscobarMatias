# Generated by Django 4.1.7 on 2023-03-07 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTerceraPreEntregaEscobarMatias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('dni', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('profesion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Patrocinante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('dni', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('marca', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('dni', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('marca', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('dni', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Clientes',
        ),
        migrations.DeleteModel(
            name='Patrocinantes',
        ),
        migrations.DeleteModel(
            name='Proveedores',
        ),
        migrations.DeleteModel(
            name='Vendedores',
        ),
    ]
