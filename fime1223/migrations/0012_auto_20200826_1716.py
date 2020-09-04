# Generated by Django 3.0.8 on 2020-08-26 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fime1223', '0011_auto_20200826_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sports_curricularinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outdoors_sports_cricket', models.CharField(blank=True, max_length=200, null=True)),
                ('outdoors_sports_Football', models.CharField(blank=True, max_length=200, null=True)),
                ('outdoors_sportsHockey', models.CharField(blank=True, max_length=200, null=True)),
                ('outdoors_sports_Others', models.CharField(blank=True, max_length=200, null=True)),
                ('indoor_sports', models.CharField(blank=True, max_length=200, null=True)),
                ('indoor_Carrom', models.CharField(blank=True, max_length=200, null=True)),
                ('indoor_Tennis', models.CharField(blank=True, max_length=200, null=True)),
                ('indoor_Boxing', models.CharField(blank=True, max_length=200, null=True)),
                ('indoor_Others', models.CharField(blank=True, max_length=200, null=True)),
                ('Kids_play_Area', models.CharField(blank=True, max_length=200, null=True)),
                ('Toy_Room', models.CharField(blank=True, max_length=200, null=True)),
                ('Cricket_Ground', models.CharField(blank=True, max_length=200, null=True)),
                ('Swimming_pool_flash', models.CharField(blank=True, max_length=200, null=True)),
                ('sports_facilities_Others', models.CharField(blank=True, max_length=200, null=True)),
                ('indore_outdoor_pic', models.CharField(blank=True, max_length=200, null=True)),
                ('pic_facilities', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Sports_curricular',
        ),
    ]
