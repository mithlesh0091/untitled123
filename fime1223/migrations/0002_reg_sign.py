# Generated by Django 3.0.8 on 2020-07-30 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fime1223', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='reg_sign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('School_Name', models.CharField(max_length=100)),
                ('Cant_find_your_School', models.CharField(max_length=100)),
                ('Contact_person_Name', models.CharField(max_length=100)),
                ('Designation_at_School', models.CharField(max_length=100)),
                ('Password1', models.CharField(max_length=100)),
                ('Password2', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Mobile_No', models.CharField(max_length=100)),
            ],
        ),
    ]
