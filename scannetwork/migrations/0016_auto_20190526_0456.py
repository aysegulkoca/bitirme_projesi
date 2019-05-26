# Generated by Django 2.1.7 on 2019-05-26 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scannetwork', '0015_auto_20190526_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vulnerability',
            name='cvss_score_v2',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='cvss_score_v2'),
        ),
        migrations.AlterField(
            model_name='vulnerability',
            name='cvss_score_v3',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='cvss_score_v3'),
        ),
    ]
