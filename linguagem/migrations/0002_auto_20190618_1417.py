# Generated by Django 2.2.2 on 2019-06-18 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linguagem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linguagem',
            name='fabricante',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Fabricante'),
        ),
        migrations.AlterField(
            model_name='linguagem',
            name='linguagem_name',
            field=models.CharField(max_length=30, verbose_name='Linguagem'),
        ),
        migrations.AlterField(
            model_name='linguagem',
            name='rank',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='Rank'),
        ),
    ]
