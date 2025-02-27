# Generated by Django 5.1.4 on 2025-02-25 02:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppHome', '0006_alter_demanda_solicitante'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='demanda',
            old_name='descricao',
            new_name='descricao_problema',
        ),
        migrations.AddField(
            model_name='demanda',
            name='data_solucao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='demanda',
            name='descricao_solucao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='demanda',
            name='servico',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='demanda',
            name='solicitante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='demanda',
            name='status',
            field=models.CharField(choices=[('Aberto', 'Aberto'), ('Em Andamento', 'Em Andamento'), ('Concluído', 'Concluído')], default='Aberto', max_length=20),
        ),
        migrations.AlterField(
            model_name='demanda',
            name='tipo',
            field=models.CharField(choices=[('Chamado', 'Chamado'), ('Projeto', 'Projeto')], default='Chamado', max_length=10),
        ),
    ]
