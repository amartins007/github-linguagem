# Generated by Django 2.2.2 on 2019-06-24 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linguagem', '0005_auto_20190620_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='linguagem',
            name='doc',
        ),
        migrations.AlterField(
            model_name='linguagem',
            name='rank',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='Rank'),
        ),
        migrations.DeleteModel(
            name='Documento',
        ),
    ]
