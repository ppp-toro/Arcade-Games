# Generated by Django 4.2 on 2023-07-03 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.TextField(max_length=8)),
                ('Apellidos', models.TextField(max_length=16)),
                ('Gmail', models.TextField(max_length=24)),
                ('Descripcion', models.TextField(max_length=50)),
                ('Usuario', models.TextField(max_length=8)),
                ('Contraseña', models.TextField(max_length=12)),
                ('Imagen', models.ImageField(upload_to='user_images/')),
            ],
        ),
    ]
