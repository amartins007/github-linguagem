# Generated by Django 2.2.2 on 2019-07-10 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linguagem', '0006_auto_20190623_2206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='linguagem',
            name='fabricante',
        ),
        migrations.RemoveField(
            model_name='linguagem',
            name='rank',
        ),
        migrations.AddField(
            model_name='linguagem',
            name='forks',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Forks'),
        ),
        migrations.AddField(
            model_name='linguagem',
            name='watches',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Watches'),
        ),
    ]
