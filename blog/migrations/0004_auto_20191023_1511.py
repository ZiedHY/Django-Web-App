# Generated by Django 2.2.6 on 2019-10-23 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191023_1508'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categorie',
            new_name='Categories',
        ),
    ]