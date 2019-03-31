# Generated by Django 2.1.7 on 2019-03-25 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scannetwork', '0007_serviceversion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vulnerability',
            name='code',
        ),
        migrations.AddField(
            model_name='vulnerability',
            name='score',
            field=models.FloatField(default=0, verbose_name='score'),
            preserve_default=False,
        ),
    ]
