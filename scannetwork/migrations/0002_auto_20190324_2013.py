# Generated by Django 2.1.7 on 2019-03-24 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scannetwork', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=200, verbose_name='product_name')),
                ('product', models.CharField(max_length=200, verbose_name='product_service')),
            ],
        ),
        migrations.AlterField(
            model_name='version',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scannetwork.Service', verbose_name='product_id'),
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
