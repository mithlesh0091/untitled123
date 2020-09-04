from django.db import models
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render


# multiple#######################


# multiple#######################

class admission_infonn(models.Model):
    academic_year = models.CharField(max_length=200)
    academic_start = models.CharField(max_length=200)
    academic_end = models.CharField(max_length=200)
    online_admission_application = models.CharField(max_length=200)
    Admission_page_url = models.CharField(max_length=200)
    Facility_to_pay_admission_online = models.CharField(max_length=200)
    Admission_open = models.CharField(max_length=200)
    academic_contactpersonname = models.CharField(max_length=200)
    academic_contactpersonmob = models.CharField(max_length=200)
    academic_contactpersonemail = models.CharField(max_length=200)

    def __str__(self):
        return self.academic_year


class reg_sign(models.Model):
    School_Name = models.CharField(max_length=100)
    Cant_find_your_School = models.CharField(max_length=100)
    Contact_person_Name = models.CharField(max_length=100)
    Designation_at_School = models.CharField(max_length=100)
    Password1 = models.CharField(max_length=100)
    Password2 = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Mobile_No = models.CharField(max_length=100)

    def __str__self(self):
        return self.Email


class School(models.Model):
    title = models.CharField(max_length=124)

    def __str__(self):
        return self.title

    ####################################aminities facility######################


class Facility_info(models.Model):
    Activity_center = models.CharField(max_length=124)
    Computer_Labs = models.CharField(max_length=124)
    Library = models.CharField(max_length=124)
    Laboratories = models.CharField(max_length=124)
    Canteen_Cafteria = models.CharField(max_length=124)
    Transport_facilities = models.CharField(max_length=124)
    Sports_facilities = models.CharField(max_length=124)
    Medical_Facility = models.CharField(max_length=124)
    Lockers = models.CharField(max_length=124)
    CCTV = models.CharField(max_length=124)
    Audotorium_Seminar_Hall = models.CharField(max_length=124)

    Gymnasiumn = models.CharField(max_length=124)
    Play_Ground = models.CharField(max_length=124)
    Drinking_Water = models.CharField(max_length=124)
    Music_Dance = models.CharField(max_length=124)
    Stationary_Shop = models.CharField(max_length=124)
    Wifi = models.CharField(max_length=124)
    Car_Parking = models.CharField(max_length=124)
    Bike_Cycle_Parking = models.CharField(max_length=124)
    Security = models.CharField(max_length=124)
    Guard = models.CharField(max_length=124)

    Fire_Extinguihev = models.CharField(max_length=124)
    Hygienic = models.CharField(max_length=124)
    Washroom = models.CharField(max_length=124)
    Hostel = models.CharField(max_length=124)
    Swimming_Pool_Splash_Pool = models.CharField(max_length=124)
    Others = models.CharField(max_length=124)
    Facilities_Amenities_wsabi = models.CharField(max_length=124)
    campusimages = models.CharField(max_length=124)
    campusVideo = models.CharField(max_length=124)

    campus360 = models.CharField(max_length=124)
    Saftey = models.CharField(max_length=124)
    conteen = models.CharField(max_length=124)
    Parking = models.CharField(max_length=124)
    facilitiesandinfra = models.CharField(max_length=124)
    youtubeurl1 = models.CharField(max_length=124)
    youtubeurl2 = models.CharField(max_length=124)
    youtubeurl3 = models.CharField(max_length=124)
    youtubeurl4 = models.CharField(max_length=124)

    txtEditor14 = models.CharField(max_length=124)
    txtEditor15 = models.CharField(max_length=124)
    txtEditor16 = models.CharField(max_length=124)

    def __str__(self):
        return self.Activity_center
    ######################END#########aminities facility######################


# def admission_information(request):
#      return render(request,"dashboard.html")

class Admission_document_eligibility_info(models.Model):
    School_Admission_Details_and_Procedure = models.CharField(max_length=200)
    academic_year = models.CharField(max_length=200)
    Admission_Eligibility_Criteria = models.CharField(max_length=200)
    Documents_Required_for_Admission = models.CharField(max_length=200)
    # Age_Creteria = models.CharField(max_length=200)
    Lyco_Arts = models.CharField(max_length=200)
    Lyco_Science = models.CharField(max_length=200)
    Lyco_Commerce = models.CharField(max_length=200)
    Mcoe_Arts = models.CharField(max_length=200)
    Mcoe_Science = models.CharField(max_length=200)
    Mcoe_Commerce = models.CharField(max_length=200)

    def __str__(self):
        return self.Lyco_Arts


class Awards_Recognitioninfo(models.Model):
    awards_National_Ranking = models.CharField(max_length=200)
    awards_Ranking_Body = models.CharField(max_length=200)
    awards_uploadimages = models.CharField(max_length=200)
    awards_State_Ranking = models.CharField(max_length=200)
    # Age_Creteria = models.CharField(max_length=200)
    awards_Ranking_Body1 = models.CharField(max_length=200)
    awards_uploadimages1 = models.CharField(max_length=200)
    write_sometings_about_ranking = models.CharField(max_length=200)
    write_somethings_about_sport_awards = models.CharField(max_length=200)
    upload_images_and_others_Awards = models.CharField(max_length=200)

    def __str__(self):
        return self.awards_National_Ranking


# ------------------------fee_Scructureinfo-----------#
class fee_structureinfo(models.Model):
    admission_fee_classwise = models.CharField(max_length=200)
    admission_fee_security = models.CharField(max_length=200)
    admission_fee_other = models.CharField(max_length=200)
    application_register_admission_fee_classwise = models.CharField(max_length=200)
    application_register_fee_for_day_school = models.CharField(max_length=200)
    application_register_Transpotation_admission_fee_other = models.CharField(max_length=200)
    india_Admission_Application_fee = models.CharField(max_length=200)
    india_Security_deposite_fees = models.CharField(max_length=200)
    india_Extra_fees = models.CharField(max_length=200)
    india_Yearly_fees = models.CharField(max_length=200)
    Yearly_fees_international = models.CharField(max_length=200)
    Admission_Application_fee_international = models.CharField(max_length=200)
    Security_deposite_fees_international = models.CharField(max_length=200)
    Extra_fees_international = models.CharField(max_length=200)
    Estimated_annualfees_class_Wise_international = models.CharField(max_length=200)

    def __str__(self):
        return self.admission_fee_classwise


# ------------------------END fee_Scructureinfo-----------#


class Hostel_Accomodationinfo(models.Model):
    hostel_Boys = models.CharField(max_length=200, blank=True, null=True)
    # hostel_Boys = models.BooleanField(max_length=200, blank=True, null=True)
    hostel_Girls = models.CharField(max_length=200, blank=True, null=True)
    hostel_boys_Boys_Girls = models.CharField(max_length=200, blank=True, null=True)
    hostel_total_no = models.CharField(max_length=200, blank=True, null=True)
    hostel_total_no_boys_yes = models.CharField(max_length=200, blank=True, null=True)
    hostel_total_no_boys_no = models.CharField(max_length=200, blank=True, null=True)
    hostel_total_no_boys_no_ac = models.CharField(max_length=200, blank=True, null=True)
    hostel_total_no_boys_no_non_ac = models.CharField(max_length=200, blank=True, null=True)
    Hostel_in_campus = models.CharField(max_length=200, blank=True, null=True)
    Hostel_out_campus = models.CharField(max_length=200, blank=True, null=True)
    booking_facility_avalilable_from = models.CharField(max_length=200, blank=True, null=True)
    booking_facility_avalilable_to = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.hostel_Boys


# class Sports_curricularinfo#

class Basic_informationinfo(models.Model):
    Basic_information_school_name = models.CharField(max_length=200)
    Basic_information_school_short_name = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    Basic_information_tag_line_of_school = models.CharField(max_length=200)
    Basic_information_url = models.CharField(max_length=200)
    Basic_information_school_logo = models.CharField(max_length=200)
    Basic_information_school_trusty_socity = models.CharField(max_length=200)
    Basic_information_school_cover_img = models.CharField(max_length=200)
    Basic_information_school_upload_brochure = models.CharField(max_length=200)

    def __str__(self):
        return self.Basic_information_school_name


# SPORTS AND EXTRA-CURRICULAR ACTIVITES

class Sports_curricularinfo(models.Model):
    outdoors_sports_cricket = models.CharField(max_length=200, blank=True, null=True)
    outdoors_sports_Football = models.CharField(max_length=200, blank=True, null=True)
    outdoors_sportsHockey = models.CharField(max_length=200, blank=True, null=True)
    outdoors_sports_Others = models.CharField(max_length=200, blank=True, null=True)
    # Age_Creteria = models.CharField(max_length=200)
    indoor_sports = models.CharField(max_length=200, blank=True, null=True)
    indoor_Carrom = models.CharField(max_length=200, blank=True, null=True)
    indoor_Tennis = models.CharField(max_length=200, blank=True, null=True)
    indoor_Boxing = models.CharField(max_length=200, blank=True, null=True)
    indoor_Others = models.CharField(max_length=200, blank=True, null=True)
    Kids_play_Area = models.CharField(max_length=200, blank=True, null=True)
    Toy_Room = models.CharField(max_length=200, blank=True, null=True)
    Cricket_Ground = models.CharField(max_length=200, blank=True, null=True)
    Swimming_pool_flash = models.CharField(max_length=200, blank=True, null=True)
    sports_facilities_Others = models.CharField(max_length=200, blank=True, null=True)
    indore_outdoor_pic = models.CharField(max_length=200, blank=True, null=True)
    pic_facilities = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.outdoors_sports_cricket


class myClass(models.Model):
    completed = models.BooleanField(default=False, blank=True)
    completed1 = models.BooleanField(default=False, blank=True)
    completed2 = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.completed
