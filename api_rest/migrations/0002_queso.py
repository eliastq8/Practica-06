# Generated by Django 5.0.2 on 2024-03-02 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Queso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('peso', models.IntegerField()),
                ('presentacion', models.CharField(choices=[('Bolsa', 'Bolsa'), ('Paquete', 'Paquete')], max_length=30)),
                ('fecha_creado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
