# Generated by Django 2.2.2 on 2019-06-18 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linguagem', '0002_auto_20190618_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linguagem',
            name='rank',
            field=models.IntegerField(max_length=2, null=True, verbose_name='Rank'),
        ),
    ]
