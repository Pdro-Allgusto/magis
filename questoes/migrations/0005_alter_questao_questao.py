# Generated by Django 4.0.4 on 2022-05-10 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questoes', '0004_questao_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questao',
            name='questao',
            field=models.CharField(max_length=300),
        ),
    ]
