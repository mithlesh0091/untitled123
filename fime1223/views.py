from django.contrib import messages
from django.contrib import messages
from django.contrib.auth.models import auth
from django.http import *
from django.http import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
#
from fime1223.models import School

from .forms import *
from .models import *
from .models import Admission_document_eligibility_info
from .models import Awards_Recognitioninfo
from .models import Hostel_Accomodationinfo
from .models import Sports_curricularinfo
from .models import admission_infonn
from .models import fee_structureinfo
from .models import Basic_informationinfo
from .models import Facility_info


# s
# Create your views here.
##############multiple####################



def home(request):
    return render(request, 'home.html', {'name': 'navin'});


def registerpage(request):
    return render(request, 'registerpage.html');


def dashboard(request):
    return render(request, 'dashboard.html');


def collages(request):
    return render(request, 'collages.html');


def register(request):
    return render(request, 'register.html');


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # return redirect("dashboard")
            return render(request, 'dashboard.html');
        else:
            messages.info(request, 'invalid credentails')
            return redirect('login')
    return render(request, 'login.html');


#


# def reg_sign(request):
#     if request.method == 'POST':
#         form = reg_sign(request.POST)
#         if form.is_valid():
#             form.save()
#             return  HttpResponseRedirect('reg_sign')
#         else:
#             form = reg_sign()
#     return render(request, 'reg_sign.html',{form:form});


def addyourschool(request):
    if 'term' in request.GET:
        qs = School.objects.filter(title__icontains=request.GET.get('term'))
        titles = list()
        for school in qs:
            titles.append(school.title)
        titles = [product.title for product in qs]
        return JsonResponse(titles, safe=False)
    # if request.method == 'POST':
    #     schoolname = request.POST['schoolname']
    #     form_cfschpool = request.POST['form_cfschpool']
    #     Pessonname = request.POST['Pessonname']
    #     DesignationatSchool = request.POST['DesignationatSchool']
    #     password1 = request.POST['password']
    #     # password2 = request.POST['password2']
    #     email = request.POST['email']
    #     phone = request.POST['phone']
    #
    #     user = User.objects.created_user(schoolname=schoolname,Pessonname=Pessonname,DesignationatSchool=DesignationatSchool,password=password1,email=email,phone=phone)
    #     user.save()

    else:
        return render(request, 'addyourschool.html')


def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'register.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone_number = form.cleaned_data['phone_number']
                user.save()
                messages.success(request, 'Thank you !! you have successfully registr your School on MeritBell.com')
                # Login the user
                # login(request, user)

                # redirect to accounts page:
                return HttpResponseRedirect('http://127.0.0.1:8000/register/')

    # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('login')


def admission_informationvarn(request):
    # print("hello form is sucessfully submit")
    academic_year = request.POST["academic_year"]

    academic_start = request.POST['academic_start']
    academic_end = request.POST['academic_end']
    online_admission_application = request.POST['online_admission_application']
    Admission_page_url = request.POST['Admission_page_url']
    Facility_to_pay_admission_online = request.POST['Facility_to_pay_admission_online']
    Admission_open = request.POST['Admission_open']
    academic_contactpersonname = request.POST['academic_contactpersonname']
    academic_contactpersonmob = request.POST['academic_contactpersonmob']
    academic_contactpersonemail = request.POST['academic_contactpersonemail']
    admission_informationvarn = admission_infonn(academic_year=academic_year, academic_start=academic_start,
                                                 academic_end=academic_end,
                                                 online_admission_application=online_admission_application,
                                                 Admission_page_url=Admission_page_url,
                                                 Facility_to_pay_admission_online=Facility_to_pay_admission_online,
                                                 Admission_open=Admission_open,
                                                 academic_contactpersonname=academic_contactpersonname,
                                                 academic_contactpersonmob=academic_contactpersonmob,
                                                 academic_contactpersonemail=academic_contactpersonemail)

    admission_informationvarn.save()
    messages.success(request, 'save has been done')
    return render(request, "dashboard.html")
  ####################################aminities facility######################
def Facility(request):
    Activity_center = request.POST["Activity_center"]
    Computer_Labs = request.POST["Computer_Labs"]
    Library = request.POST["Library"]
    Laboratories = request.POST["Laboratories"]
    Canteen_Cafteria = request.POST["Canteen_Cafteria"]
    Transport_facilities = request.POST["Transport_facilities"]
    Sports_facilities = request.POST["Sports_facilities"]

    Medical_Facility = request.POST["Medical_Facility"]
    Lockers = request.POST["Lockers"]
    CCTV = request.POST["CCTV"]
    Audotorium_Seminar_Hall = request.POST["Audotorium_Seminar_Hall"]

    Gymnasiumn = request.POST["Gymnasiumn"]
    Play_Ground = request.POST["Play_Ground"]
    Drinking_Water = request.POST["Drinking_Water"]
    Music_Dance = request.POST["Music_Dance"]

    Stationary_Shop = request.POST["Stationary_Shop"]
    Wifi = request.POST["Wifi"]
    Car_Parking = request.POST["Car_Parking"]
    Bike_Cycle_Parking = request.POST["Bike_Cycle_Parking"]

    Security = request.POST["Security"]
    Guard = request.POST["Guard"]
    Fire_Extinguihev = request.POST["Fire_Extinguihev"]
    Hygienic = request.POST["Hygienic"]
    Washroom = request.POST["Washroom"]
    Hostel = request.POST["Hostel"]
    Swimming_Pool_Splash_Pool = request.POST["Swimming_Pool_Splash_Pool"]
    Others = request.POST["Others"]
    Facilities_Amenities_wsabi = request.POST["Facilities_Amenities_wsabi"]
    campusimages = request.POST["campusimages"]
    campusVideo = request.POST["campusVideo"]
    campus360 = request.POST["campus360"]
    Saftey = request.POST["Saftey"]
    conteen = request.POST["conteen"]
    Parking = request.POST["Parking"]
    facilitiesandinfra = request.POST["facilitiesandinfra"]
    youtubeurl1 = request.POST["youtubeurl1"]
    youtubeurl2 = request.POST["youtubeurl2"]
    youtubeurl3 = request.POST["youtubeurl3"]
    youtubeurl4 = request.POST["youtubeurl4"]
    txtEditor14 = request.POST["txtEditor14"]
    txtEditor15 = request.POST["txtEditor15"]
    txtEditor16 = request.POST["txtEditor16"]

    Facilityvarn = Facility_info(
        Activity_center=Activity_center,
        Computer_Labs=Computer_Labs,
        Library=Library,
        Laboratories=Laboratories,
        Canteen_Cafteria=Canteen_Cafteria,
        Transport_facilities=Transport_facilities,
        Sports_facilities=Sports_facilities,
        Medical_Facility=Medical_Facility,
        Lockers=Lockers,
        CCTV=CCTV,
        Audotorium_Seminar_Hall=Audotorium_Seminar_Hall,
        Gymnasiumn=Gymnasiumn,
        Play_Ground=Play_Ground,
        Drinking_Water=Drinking_Water,
        Music_Dance=Music_Dance,
        Stationary_Shop=Stationary_Shop,
        Wifi=Wifi,
        Car_Parking=Car_Parking,
        Bike_Cycle_Parking=Bike_Cycle_Parking,
        Security=Security,
        Guard=Guard,
        Fire_Extinguihev=Fire_Extinguihev,
        Hygienic=Hygienic,
        Washroom=Washroom,
        Hostel=Hostel,
        Swimming_Pool_Splash_Pool=Swimming_Pool_Splash_Pool,
        Others=Others,
        Facilities_Amenities_wsabi=Facilities_Amenities_wsabi,
        campusimages=campusimages,
        campusVideo=campusVideo,
        campus360=campus360,
        Saftey=Saftey,
        conteen=conteen,
        Parking=Parking,
        facilitiesandinfra=facilitiesandinfra,
        youtubeurl1=youtubeurl1,
        youtubeurl2=youtubeurl2,
        youtubeurl3=youtubeurl3,
        youtubeurl4=youtubeurl4,
        txtEditor14=txtEditor14,
        txtEditor15=txtEditor15,
        txtEditor16=txtEditor16,



    )
    Facilityvarn.save()
    return HttpResponseRedirect('http://127.0.0.1:8000/dashboard/#admission-eligi')
######################END#########aminities facility######################

def Admission_document_eligibility(request):
    School_Admission_Details_and_Procedure = request.POST["School_Admission_Details_and_Procedure"]
    # academic_year = request.POST["academic_year"]
    Admission_Eligibility_Criteria = request.POST["Admission_Eligibility_Criteria"]
    Documents_Required_for_Admission = request.POST["Documents_Required_for_Admission"]
    Age_Creteria = request.POST["Age_Creteria"]
    Lyco_Arts = request.POST["Lyco_Arts"]
    Lyco_Science = request.POST["Lyco_Science"]
    Lyco_Commerce = request.POST["Lyco_Commerce"]
    Mcoe_Arts = request.POST["Mcoe_Arts"]
    Mcoe_Science = request.POST["Mcoe_Science"]
    Mcoe_Commerce = request.POST["Mcoe_Commerce"]
    Admission_document_eligibilityvarn = Admission_document_eligibility_info(
        School_Admission_Details_and_Procedure=School_Admission_Details_and_Procedure,
        # academic_year=academic_year,
        Admission_Eligibility_Criteria=Admission_Eligibility_Criteria,
        Documents_Required_for_Admission=Documents_Required_for_Admission,
        # Age_Creteria=Age_Creteria,
        Lyco_Arts=Lyco_Arts,
        Lyco_Science=Lyco_Science,
        Lyco_Commerce=Lyco_Commerce,
        Mcoe_Arts=Mcoe_Arts,
        Mcoe_Science=Mcoe_Science,
        Mcoe_Commerce=Mcoe_Commerce
    )
    Admission_document_eligibilityvarn.save()
    # return render(request, "dashboard.html")
    return HttpResponseRedirect('http://127.0.0.1:8000/dashboard/#admission-eligi')


#############################################Basic_information######################
def Basic_information(request):
    Basic_information_school_name = request.POST["Basic_information_school_name"]
    Basic_information_school_short_name = request.POST["Basic_information_school_short_name"]
    date = request.POST["date"]
    Basic_information_tag_line_of_school = request.POST["Basic_information_tag_line_of_school"]
    Basic_information_url = request.POST["Basic_information_url"]
    Basic_information_school_logo = request.POST["Basic_information_school_logo"]
    Basic_information_school_trusty_socity = request.POST["Basic_information_school_trusty_socity"]
    Basic_information_school_cover_img = request.POST["Basic_information_school_cover_img"]
    Basic_information_school_upload_brochure = request.POST["Basic_information_school_upload_brochure"]
    Basic_informationvar = Basic_informationinfo(
        Basic_information_school_name=Basic_information_school_name,
        Basic_information_school_short_name=Basic_information_school_short_name,
        date=date,
        Basic_information_tag_line_of_school=Basic_information_tag_line_of_school,
        Basic_information_url=Basic_information_url,
        Basic_information_school_logo=Basic_information_school_logo,
        Basic_information_school_trusty_socity=Basic_information_school_trusty_socity,
        Basic_information_school_cover_img=Basic_information_school_cover_img,
        Basic_information_school_upload_brochure=Basic_information_school_upload_brochure,
    )
    Basic_informationvar.save()
    messages.success(request, 'Updated successfully!')




    return HttpResponseRedirect('http://127.0.0.1:8000/dashboard/#basic-infolink')
##########################################END----Basic_information######################
# ############################################Awards_Recognition###############
def Awards_Recognition(request):
    awards_National_Ranking = request.POST["awards_National_Ranking"]
    awards_Ranking_Body = request.POST["awards_Ranking_Body"]
    awards_uploadimages = request.POST["awards_uploadimages"]
    awards_State_Ranking = request.POST["awards_State_Ranking"]
    awards_Ranking_Body1 = request.POST["awards_Ranking_Body1"]
    awards_uploadimages1 = request.POST["awards_uploadimages1"]
    write_sometings_about_ranking = request.POST["write_sometings_about_ranking"]
    write_somethings_about_sport_awards = request.POST["write_somethings_about_sport_awards"]
    upload_images_and_others_Awards = request.POST["upload_images_and_others_Awards"]
    Awards_Recognitionvar = Awards_Recognitioninfo(
        awards_National_Ranking=awards_National_Ranking,
        awards_Ranking_Body=awards_Ranking_Body,
        awards_uploadimages=awards_uploadimages,
        awards_State_Ranking=awards_State_Ranking,
        awards_Ranking_Body1=awards_Ranking_Body1,
        awards_uploadimages1=awards_uploadimages1,
        write_sometings_about_ranking=write_sometings_about_ranking,
        write_somethings_about_sport_awards=write_somethings_about_sport_awards,
        upload_images_and_others_Awards=upload_images_and_others_Awards,
    )
    Awards_Recognitionvar.save()
    messages.success(request, 'Updated successfully!')
    # return render(request, "http://127.0.0.1:8000/dashboard/#Awards-Recognition")
    return HttpResponseRedirect('http://127.0.0.1:8000/dashboard/#Awards-Recognition')


# fee structure section----------------------------------------------------#
def fee_Scructure(request):
    admission_fee_classwise = request.POST["admission_fee_classwise"]
    admission_fee_security = request.POST["admission_fee_security"]
    admission_fee_other = request.POST["admission_fee_other"]
    application_register_admission_fee_classwise = request.POST["application_register_admission_fee_classwise"]
    application_register_Transpotation_admission_fee_other = request.POST[
        "application_register_Transpotation_admission_fee_other"]
    application_register_fee_for_day_school = request.POST["application_register_fee_for_day_school"]
    india_Admission_Application_fee = request.POST["india_Admission_Application_fee"]
    india_Security_deposite_fees = request.POST["india_Security_deposite_fees"]
    india_Extra_fees = request.POST["india_Security_deposite_fees"]
    india_Yearly_fees = request.POST["india_Yearly_fees"]
    Admission_Application_fee_international = request.POST["Admission_Application_fee_international"]
    Security_deposite_fees_international = request.POST["Security_deposite_fees_international"]
    Extra_fees_international = request.POST["Extra_fees_international"]
    Yearly_fees_international = request.POST["Yearly_fees_international"]
    Estimated_annualfees_class_Wise_international = request.POST["Yearly_fees_international"]
    fee_Scructurevar = fee_structureinfo(
        admission_fee_classwise=admission_fee_classwise,
        admission_fee_security=admission_fee_security,
        admission_fee_other=admission_fee_other,
        application_register_admission_fee_classwise=application_register_admission_fee_classwise,
        application_register_Transpotation_admission_fee_other=application_register_Transpotation_admission_fee_other,
        application_register_fee_for_day_school=application_register_fee_for_day_school,
        india_Admission_Application_fee=india_Admission_Application_fee,
        india_Security_deposite_fees=india_Security_deposite_fees,
        india_Extra_fees=india_Extra_fees,
        india_Yearly_fees=india_Yearly_fees,
        Admission_Application_fee_international=Admission_Application_fee_international,
        Security_deposite_fees_international=Security_deposite_fees_international,
        Extra_fees_international=Extra_fees_international,
        Yearly_fees_international=Yearly_fees_international,
        Estimated_annualfees_class_Wise_international=Estimated_annualfees_class_Wise_international
    )

    fee_Scructurevar.save()
    messages.success(request, 'Updated successfully!')
    return HttpResponseRedirect('http://127.0.0.1:8000/dashboard/#fee_structure_for_day_school')


# end fee structure section------------------------------------------------#

def Hostel_Accomodation(request):
    hostel_Boys = request.POST["hostel_Boys"]
    hostel_Girls = request.POST["hostel_Girls"]
    hostel_boys_Boys_Girls = request.POST["hostel_boys_Boys_Girls"]
    hostel_total_no = request.POST["hostel_total_no"]
    hostel_total_no_boys_yes = request.POST["hostel_total_no_boys_yes"]
    hostel_total_no_boys_no = request.POST["hostel_total_no_boys_no"]
    hostel_total_no_boys_no_ac = request.POST["hostel_total_no_boys_no_ac"]
    hostel_total_no_boys_no_non_ac = request.POST["hostel_total_no_boys_no_non_ac"]
    Hostel_in_campus = request.POST["Hostel_in_campus"]
    Hostel_out_campus = request.POST["Hostel_out_campus"]
    booking_facility_avalilable_from = request.POST["booking_facility_avalilable_from"]
    booking_facility_avalilable_to = request.POST["booking_facility_avalilable_to"]
    Hostel_Accomodationvar = Hostel_Accomodationinfo(
        hostel_Boys=hostel_Boys,
        hostel_Girls=hostel_Girls,
        hostel_boys_Boys_Girls=hostel_boys_Boys_Girls,
        hostel_total_no=hostel_total_no,
        hostel_total_no_boys_yes=hostel_total_no_boys_yes,
        hostel_total_no_boys_no=hostel_total_no_boys_no,
        hostel_total_no_boys_no_ac=hostel_total_no_boys_no_ac,
        hostel_total_no_boys_no_non_ac=hostel_total_no_boys_no_non_ac,
        Hostel_in_campus=Hostel_in_campus,
        Hostel_out_campus=Hostel_out_campus,
        booking_facility_avalilable_from=booking_facility_avalilable_from,
        booking_facility_avalilable_to=booking_facility_avalilable_to

    )
    Hostel_Accomodationvar.save()

    messages.success(request, 'Updated successfully!')
    return HttpResponseRedirect('http://127.0.0.1:8000/dashboard/#Hostel-Accomodation')

# #################################dashboard.html###########SPORTS AND EXTRA-CURRICULAR ACTIVITES###############

def Sports_curricular(request):
    outdoors_sports_cricket = request.POST["outdoors_sports_cricket"]
    outdoors_sports_Football = request.POST["outdoors_sports_Football"]
    outdoors_sportsHockey = request.POST["outdoors_sportsHockey"]
    outdoors_sports_Others = request.POST["outdoors_sports_Others"]
    indoor_sports = request.POST["indoor_sports"]
    indoor_Carrom = request.POST["indoor_Carrom"]
    indoor_Tennis = request.POST["indoor_Tennis"]
    indoor_Boxing = request.POST["indoor_Boxing"]
    indoor_Others = request.POST["indoor_Others"]
    Kids_play_Area = request.POST["Kids_play_Area"]
    Toy_Room = request.POST["Toy_Room"]
    Cricket_Ground = request.POST["Cricket_Ground"]
    Swimming_pool_flash = request.POST["Swimming_pool_flash"]
    sports_facilities_Others = request.POST["sports_facilities_Others"]
    indore_outdoor_pic = request.POST["indore_outdoor_pic"]
    pic_facilities = request.POST["pic_facilities"]
    sports_and_extra_cirrvar = Sports_curricularinfo(
        outdoors_sports_cricket=outdoors_sports_cricket,
        outdoors_sports_Football=outdoors_sports_Football,
        outdoors_sportsHockey=outdoors_sportsHockey,
        outdoors_sports_Others=outdoors_sports_Others,
        indoor_sports=indoor_sports,
        indoor_Carrom=indoor_Carrom,
        indoor_Tennis=indoor_Tennis,
        indoor_Boxing=indoor_Boxing,
        indoor_Others=indoor_Others,
        Kids_play_Area=Kids_play_Area,
        Toy_Room=Toy_Room,
        Cricket_Ground=Cricket_Ground,
        Swimming_pool_flash=Swimming_pool_flash,
        sports_facilities_Others=sports_facilities_Others,
        indore_outdoor_pic=indore_outdoor_pic,
        pic_facilities=pic_facilities
    )
    sports_and_extra_cirrvar.save()
    messages.success(request, 'Updated successfully!')
    return HttpResponseRedirect('http://127.0.0.1:8000/dashboard/#Sports-exta')
    # return render(request, "dashboard.html")

def create_myClass(request):
    # create a dictionary
    context = {
        "data": [1, 2, 3],
    }

    messages.success(request, 'Updated successfully!')
    # return response
    return render(request, "dashboard.html", context)



# def create_myClass(request):
#     context = {
#           }
#     # completed = request.POST.get('completed')
#     completed = request.POST.get('completed', '') == 'on'
#     completed1 = request.POST.get('completed1', '') == 'on'
#     completed2= request.POST.get('completed2', '') == 'on'
#     toSave = myClass(completed=completed, completed1=completed1, completed2=completed2)
#     toSave.save()
#     return render(request, "dashboard.html")