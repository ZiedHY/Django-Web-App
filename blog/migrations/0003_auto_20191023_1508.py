# Generated by Django 2.2.6 on 2019-10-23 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191023_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='nom',
            field=models.CharField(max_length=40),
        ),
    ]
