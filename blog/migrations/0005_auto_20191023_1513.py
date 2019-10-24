# Generated by Django 2.2.6 on 2019-10-23 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191023_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Categorie'),
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
    ]
