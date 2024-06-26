# Generated by Django 4.0 on 2024-03-31 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_alter_enviosnisira_kilosenviados'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='gmail',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='telefono',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
