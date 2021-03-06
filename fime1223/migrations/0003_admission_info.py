# Generated by Django 3.0.8 on 2020-08-21 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fime1223', '0002_reg_sign'),
    ]

    operations = [
        migrations.CreateModel(
            name='admission_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_year', models.CharField(max_length=200)),
                ('academic_start', models.CharField(max_length=200)),
                ('academic_end', models.CharField(max_length=200)),
                ('optradio1', models.CharField(max_length=200)),
                ('optradio2', models.CharField(max_length=200)),
                ('academic_contactpersonname', models.CharField(max_length=200)),
                ('academic_contactpersonmob', models.CharField(max_length=200)),
                ('academic_contactpersonemail', models.CharField(max_length=200)),
            ],
        ),
    ]
