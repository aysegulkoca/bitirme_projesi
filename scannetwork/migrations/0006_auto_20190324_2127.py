# Generated by Django 2.1.7 on 2019-03-24 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scannetwork', '0005_auto_20190324_2105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceversion',
            name='service_id',
        ),
        migrations.RemoveField(
            model_name='serviceversion',
            name='version_id',
        ),
        migrations.DeleteModel(
            name='ServiceVersion',
        ),
    ]
