# Generated by Django 4.0.3 on 2023-06-02 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hats_rest', '0003_alter_locationvo_href'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationvo',
            name='href',
            field=models.CharField(max_length=300, unique=True),
        ),
    ]
