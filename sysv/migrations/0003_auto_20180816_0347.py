# Generated by Django 2.0.8 on 2018-08-16 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sysv', '0002_auto_20180816_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='imagem',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
