# Generated by Django 2.1.7 on 2019-03-22 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200, verbose_name='product_name')),
                ('product_service', models.CharField(max_length=200, verbose_name='product_service')),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=200, verbose_name='version')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scannetwork.Product', verbose_name='product_id')),
            ],
        ),
        migrations.CreateModel(
            name='Vulnerability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vulnerability', models.CharField(max_length=200, verbose_name='vulnerability')),
                ('description', models.TextField(verbose_name='description')),
                ('solution', models.TextField(verbose_name='solution')),
                ('code', models.TextField(verbose_name='code')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scannetwork.Version', verbose_name='version_id')),
            ],
        ),
    ]
