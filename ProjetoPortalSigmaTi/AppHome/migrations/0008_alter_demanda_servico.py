# Generated by Django 5.1.4 on 2025-02-25 03:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppHome', '0007_rename_descricao_demanda_descricao_problema_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demanda',
            name='servico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppHome.servico'),
        ),
    ]
