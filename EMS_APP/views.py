
from django.shortcuts import render, redirect 
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages



# by login you can sore data in session(user_id)
# by logout you can delete session which is created by login
# authenticate is check whather username and password is exist in database or not

from .models import User, EmployeeDetail,EmployeeExperience,EmployeeEducation

# Create your views here.
def index(request):
   
    return render(request,'index.html')

def emp_signup(request):
    if request.method == 'POST':
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        empid = request.POST.get('emp_id')
        email = request.POST.get('email_id')
        pwd = request.POST.get('password')
        error =""
        try:

            # Create a new user
            user = User.objects.create_user(username=email, password=pwd, first_name=firstname, last_name=lastname, email=email)
            # Create an EmployeeDetail object viaa the user
            EmployeeDetail.objects.create(user=user, emp_id=empid)

            EmployeeExperience.objects.create(user=user)
            EmployeeEducation.objects.create(user=user)
            # Redirect to the employee login page upon successful signup
            error= "false"
            return redirect("/emp_login")
        except:
            error = "true"
    else:
        error = "false"
        
    return render(request, 'emp_signup.html', {'error': error})


def emp_login(request):

    error=""
    if request.method=='POST':
        u = request.POST['email_id']
        p = request.POST['password']
        user = authenticate(username=u,password=p)
        # if user variable exist means( username and password match as DB


        #if the user variable contains a valid user object then.......
        if user:
            # data exist in user object so... call login() for store data (id of user ) in session
            login(request,user)
            messages.success(request, 'Logged in successfully.')
             
            
            
        # if username password not match as database
        else:
            error = "Invalid email or password. Please try again."
            messages.error(request, error)
    return render(request,'emp_login.html', {'error': error})


def emp_home(request):
    if not request.user.is_authenticated:
            return redirect('emp_login')
    return render(request,'emp_home.html')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""  
    employee = None  
    user = request.user  #whose student's data store in sesion ,wo user yaha se user variable mese milega...
                          # by request.user we can know curret user
    employee = EmployeeDetail.objects.get(user=user)
    if request.method == 'POST':
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        empid = request.POST.get('emp_id')
        desig = request.POST.get('emp_desig')
        address = request.POST.get('emp_add')
        dept = request.POST.get('emp_dept')
        dob = request.POST.get('b_date')
        contactt = request.POST.get('contact')
        jdate = request.POST.get('j_date')
        gender = request.POST.get('inlineRadioOptions')


        employee.user.first_name = firstname
        employee.user.last_name = lastname
        employee.emp_id = empid
        employee.designation = desig
        employee.address = address
        employee.department = dept
        employee.contact = contactt
        employee.gender = gender
        # use this method for image or date field ..... if data is there then update otherwise no
        if jdate: 
            employee.joining_date = jdate
        if dob:
            employee.date_of_birth =dob
        try:
            employee.save()
            employee.user.save()
            error = "false"
            messages.success(request, 'Profile updated successfully.')
            return redirect("/profile")
        except:
            error = "true"
        # return render(request, 'profile.html', {'error': error})

     #whose student's data store in sesion ,wo user yaha se user variable mese milega
        
    return render(request, 'profile.html', {'employee': employee,'error':error})

def Logout(request):
#when user logged in then one session will create by login() function
    logout(request)  #predefined logout function....it destroy the session and session variable
    return redirect('index')

# in this i want shows all data
def my_experience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    
    user = request.user  #whose student's data store in sesion ,wo user yaha se user variable mese milega
    employee_experience = EmployeeExperience.objects.get(user=user)
    
    

    return render(request,'myexperience.html',{'experience': employee_experience})



def edit_experience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""  
    experience = None  
    user = request.user  #whose student's data store in sesion ,wo user yaha se user variable mese milega
    experience = EmployeeExperience.objects.get(user=user)
    if request.method == 'POST':
       #variable                 (name of html form)
        name1 = request.POST.get('company1_name')
        designation1 = request.POST.get('company1_designation')
        salary1 = request.POST.get('company1_salary')
        duration1 = request.POST.get('company1_duration')

        name2 = request.POST.get('company2_name')
        designation2 = request.POST.get('company2_designation')
        salary2 = request.POST.get('company2_salary')
        duration2 = request.POST.get('company2_duration')

        name3 = request.POST.get('company3_name')
        designation3 = request.POST.get('company3_designation')
        salary3 = request.POST.get('company3_salary')
        duration3 = request.POST.get('company3_duration')


                #  .Feild_name     variable
        experience.company1_name = name1
        experience.company1_designation = designation1
        experience.company1_salary = salary1
        experience.company1_duration = duration1
        
        experience.company2_name = name2
        experience.company2_designation = designation2
        experience.company2_salary = salary2
        experience.company2_duration = duration2

        experience.company3_name = name3
        experience.company3_designation = designation3
        experience.company3_salary = salary3
        experience.company3_duration = duration3
       
        try:
            experience.save()
            error = "no"
            messages.success(request, 'Employee Experience Detail updated successfully.')
            return redirect("/my_experience")
        except:
            error = "yes"
        #return render(request, 'Edit_myexperience.html', {'error': error})

     #whose student's data store in sesion ,wo user yaha se user variable mese milega
        
    return render(request, 'Edit_myexperience.html', {'experience': experience,'error': error})

def my_education(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    
    user = request.user  #whose student's data store in sesion ,wo user yaha se user variable mese milega
    employee_education = EmployeeEducation.objects.get(user=user)
    
    

    return render(request,'myeducation.html',{'education':employee_education})



def edit_education(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""  
    education = None  
    user = request.user  #whose student's data store in sesion ,wo user yaha se user variable mese milega
    education = EmployeeEducation.objects.get(user=user)
    if request.method == 'POST':
        course_pg = request.POST.get('course_pg')
        school_clg_pg = request.POST.get('school_clg_pg')
        year_of_Passing_pg = request.POST.get('year_of_Passing_pg')
        percentage_pg = request.POST.get('percentage_pg')

        course_grad = request.POST.get('course_grad')
        school_clg_grad = request.POST.get('school_clg_grad')
        year_of_Passing_grad = request.POST.get('year_of_Passing_grad')
        percentage_grad = request.POST.get('percentage_grad')

        course_hsc = request.POST.get('course_hsc')
        school_clg_hsc = request.POST.get('school_clg_hsc')
        year_of_Passing_hsc = request.POST.get('year_of_Passing_hsc')
        percentage_hsc = request.POST.get('percentage_hsc')

        course_ssc = request.POST.get('course_ssc')
        school_clg_ssc = request.POST.get('school_clg_ssc')
        year_of_Passing_ssc = request.POST.get('year_of_Passing_ssc')
        percentage_ssc = request.POST.get('percentage_ssc')


        education.course_pg = course_pg
        education.school_clg_pg = school_clg_pg
        education.year_of_Passing_pg = year_of_Passing_pg
        education.percentage_pg = percentage_pg
        
        education.course_grad = course_grad
        education.school_clg_grad = school_clg_grad
        education.year_of_Passing_grad = year_of_Passing_grad
        education.percentage_grad = percentage_grad

        education.course_hsc = course_hsc
        education.school_clg_hsc = school_clg_hsc
        education.year_of_Passing_hsc = year_of_Passing_hsc
        education.percentage_hsc = percentage_hsc

        education.course_ssc = course_ssc
        education.school_clg_ssc = school_clg_ssc
        education.year_of_Passing_ssc = year_of_Passing_ssc
        education.percentage_ssc = percentage_ssc
       
        try:
            education.save()
            error = "no"
            messages.success(request, 'Education Detail updated successfully.')
            return redirect("/my_education")
        except:
            error = "yes"
        #return render(request, 'Edit_myexperience.html', {'error': error})

     #whose student's data store in sesion ,wo user yaha se user variable mese milega
        
    return render(request, 'Edit_myeducation.html', {'education': education,'error': error})






def change_password(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""  
    passw = None  
    user = request.user  #whose student's data store in sesion ,wo user yaha se user variable mese milega
    
    if request.method == 'POST':

        c= request.POST['current_password']
        n= request.POST['new_confirm_password']
        try:
            if user.check_password(c): #inbuilt function... it checks the current password field
                user.set_password(n)    #it saves the new password
                user.save()
                error = "no"
                messages.success(request, 'Password updated successfully.')
                
            else:
                error = "not"
            
        except:
            error = "yes"
    return render(request,'change_password.html',{'error': error})







def admin_login(request):

    error=""
    if request.method=='POST':
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username=u,password=p)


        # if user variable exist means( username and password match as DB)
        if user is not None and user.is_staff:
            # data exist in user variable so... call login() for store data (id of user ) in session
            login(request,user)
            messages.success(request, 'Logged in successfully.')
            error == "no"    
            
        # if username password not match as database
        else:
            error = "yes"
            messages.error(request, error)
    return render(request,'admin_login.html',{'error':error})

def admin_index(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request,'admin_index.html')


def admin_change_password(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""  
    passw = None  
    user = request.user  #whose student's data store in sesion ,wo user yaha se user variable mese milega
    
    if request.method == 'POST':

        c= request.POST['current_password']
        n= request.POST['new_confirm_password']
        try:
            if user.check_password(c): #inbuilt function... it checks the current password field
                user.set_password(n)    #it saves the new password
                user.save()
                error = "no"
                messages.success(request, 'Password updated successfully.')
                
            else:
                error = "not"
            
        except:
            error = "yes"
    return render(request,'admin_change_password.html',{'error': error})




def admin_all_employee(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')

    employee = EmployeeDetail.objects.all()

    return render(request,'admin_all_employee.html',{'employee':employee})


def admin_edit_profile(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""  
    employee = None  
    user = User.objects.get(id=pid)
    employee = EmployeeDetail.objects.get(user=user)
    if request.method == 'POST':
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        empid = request.POST.get('emp_id')
        desig = request.POST.get('emp_desig')
        address = request.POST.get('emp_add')
        dept = request.POST.get('emp_dept')
        dob = request.POST.get('b_date')
        contactt = request.POST.get('contact')
        jdate = request.POST.get('j_date')
        gender = request.POST.get('inlineRadioOptions')


        employee.user.first_name = firstname
        employee.user.last_name = lastname
        employee.emp_id = empid
        employee.designation = desig
        employee.address = address
        employee.department = dept
        employee.contact = contactt
        employee.gender = gender
        # use this method for image or date field ..... if data is there then update otherwise no
        if jdate: 
            employee.joining_date = jdate
        if dob:
            employee.date_of_birth =dob
        try:
            employee.save()
            employee.user.save()
            error = "no"
            messages.success(request, 'Profile updated successfully.')
          #  return redirect("/admin_edit_profile")
        except:
            error = "yes"

    return render(request,'admin_edit_profile.html',{'employee': employee,'error': error})


def admin_edit_education(request,pid):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""  
    education = None  
    #user = request.user  #whose student's data store in sesion ,wo user yaha se user variable mese milega
    user = User.objects.get(id=pid)
    education = EmployeeEducation.objects.get(user=user)
    if request.method == 'POST':
        course_pg = request.POST.get('course_pg')
        school_clg_pg = request.POST.get('school_clg_pg')
        year_of_Passing_pg = request.POST.get('year_of_Passing_pg')
        percentage_pg = request.POST.get('percentage_pg')

        course_grad = request.POST.get('course_grad')
        school_clg_grad = request.POST.get('school_clg_grad')
        year_of_Passing_grad = request.POST.get('year_of_Passing_grad')
        percentage_grad = request.POST.get('percentage_grad')

        course_hsc = request.POST.get('course_hsc')
        school_clg_hsc = request.POST.get('school_clg_hsc')
        year_of_Passing_hsc = request.POST.get('year_of_Passing_hsc')
        percentage_hsc = request.POST.get('percentage_hsc')

        course_ssc = request.POST.get('course_ssc')
        school_clg_ssc = request.POST.get('school_clg_ssc')
        year_of_Passing_ssc = request.POST.get('year_of_Passing_ssc')
        percentage_ssc = request.POST.get('percentage_ssc')


        education.course_pg = course_pg
        education.school_clg_pg = school_clg_pg
        education.year_of_Passing_pg = year_of_Passing_pg
        education.percentage_pg = percentage_pg
        
        education.course_grad = course_grad
        education.school_clg_grad = school_clg_grad
        education.year_of_Passing_grad = year_of_Passing_grad
        education.percentage_grad = percentage_grad

        education.course_hsc = course_hsc
        education.school_clg_hsc = school_clg_hsc
        education.year_of_Passing_hsc = year_of_Passing_hsc
        education.percentage_hsc = percentage_hsc

        education.course_ssc = course_ssc
        education.school_clg_ssc = school_clg_ssc
        education.year_of_Passing_ssc = year_of_Passing_ssc
        education.percentage_ssc = percentage_ssc
       
        try:
            education.save()
            error = "no"
            messages.success(request, 'Education Detail updated successfully.')
            
        except:
            error = "yes"
        #return render(request, 'Edit_myexperience.html', {'error': error})

     #whose student's data store in sesion ,wo user yaha se user variable mese milega
        
    return render(request, 'admin_edit_education.html', {'education': education,'error': error})



def admin_edit_experience(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""  
    experience = None  
    user = request.user  #whose student's data store in sesion ,wo user yaha se user variable mese milega {{OR}} who have succsesfully loged in
    
    user = User.objects.get(id=pid)  # get data of user whose id =pid
    experience = EmployeeExperience.objects.get(user=user)
    if request.method == 'POST':
       #variable                 (name of html form)
        name1 = request.POST.get('company1_name')
        designation1 = request.POST.get('company1_designation')
        salary1 = request.POST.get('company1_salary')
        duration1 = request.POST.get('company1_duration')

        name2 = request.POST.get('company2_name')
        designation2 = request.POST.get('company2_designation')
        salary2 = request.POST.get('company2_salary')
        duration2 = request.POST.get('company2_duration')

        name3 = request.POST.get('company3_name')
        designation3 = request.POST.get('company3_designation')
        salary3 = request.POST.get('company3_salary')
        duration3 = request.POST.get('company3_duration')


                #  .Feild_name     variable
        experience.company1_name = name1
        experience.company1_designation = designation1
        experience.company1_salary = salary1
        experience.company1_duration = duration1
        
        experience.company2_name = name2
        experience.company2_designation = designation2
        experience.company2_salary = salary2
        experience.company2_duration = duration2

        experience.company3_name = name3
        experience.company3_designation = designation3
        experience.company3_salary = salary3
        experience.company3_duration = duration3
       
        try:
            experience.save()
            error = "no"
            messages.success(request, 'Employee Experience Detail updated successfully.')
            #return redirect("/my_experience")
        except:
            error = "yes"
        #return render(request, 'Edit_myexperience.html', {'error': error})

     #whose student's data store in sesion ,wo user yaha se user variable mese milega
        
    return render(request, 'admin_edit_experience.html', {'experience': experience,'error': error})



def admin_delete_employee(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    
    user = User.objects.get(id=pid)
    user.delete()
    return redirect('admin_all_employee')






    
  