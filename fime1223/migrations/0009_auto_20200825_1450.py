3# Generated by Django 3.0.8 on 2020-08-25 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fime1223', '0008_remove_awards_recognitioninfo_awards_recognitionvar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hostel_Accomodationinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostel_Boys', models.CharField(max_length=200)),
                ('hostel_Girls', models.CharField(max_length=200)),
                ('hostel_boys_Boys_Girls', models.CharField(max_length=200)),
                ('hostel_total_no', models.CharField(max_length=200)),
                ('hostel_total_no_boys_yes', models.CharField(max_length=200)),
                ('hostel_total_no_boys_no', models.CharField(max_length=200)),
                ('hostel_total_no_boys_no_ac', models.CharField(max_length=200)),
                ('hostel_total_no_boys_no_non_ac', models.CharField(max_length=200)),
                ('Hostel_in_campus', models.CharField(max_length=200)),
                ('Hostel_out_campus', models.CharField(max_length=200)),
                ('booking_facility_avalilable_from', models.CharField(max_length=200)),
                ('booking_facility_avalilable_to', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='sports_and_extra_cirrinfo',
        ),
    ]