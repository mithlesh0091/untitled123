# Generated by Django 3.0.8 on 2020-08-26 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fime1223', '0012_auto_20200826_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='myClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(blank=True, default=False)),
            ],
        ),
    ]