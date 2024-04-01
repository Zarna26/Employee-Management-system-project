from django.db import models
from django.contrib.auth.models import User
## user = models.ForeignLey(User,on_delete=models.CASCADE)
#user is in built model that is provided by django
# some data of Employeedetail class, i want to store in user model
# bcoz...by this model we can get some field like firtname,lastname,password,usernames

# Create your models here.

class EmployeeDetail(models.Model):
    #if data deleted in user model ....then it also deleted in EmployeeDetail
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    emp_id = models.CharField(max_length=50,primary_key=True)
    department = models.CharField(max_length=50, null=True)
    designation = models.CharField(max_length=255,null=True)
    contact = models.CharField(max_length=255,null=True)
    gender = models.CharField(max_length=50,null=True)
    joining_date = models.DateField(null=True)
    date_of_birth = models.DateField(null=True)
    address = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.user.username


#when employee signup then we store all the data in EmployeeDetail table
# but in other table.......
# but when employee only signup then we want to store data in user field and other field None  in EmployeeEducation and EmployeeExperience 



class EmployeeEducation(models.Model):
    #if data deleted in user model ....then it also deleted in EmployeeEducation
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # course post graduation
    course_pg = models.CharField(max_length=200,null=True)
    school_clg_pg = models.CharField(max_length=200, null=True)
    year_of_Passing_pg = models.CharField(max_length=100,null=True)
    percentage_pg= models.CharField(max_length=100,null=True)
    #course graduation
    course_grad = models.CharField(max_length=200,null=True)
    school_clg_grad = models.CharField(max_length=200,null=True)
    year_of_Passing_grad = models.CharField(max_length= 100,null=True)
    percentage_grad = models.CharField(max_length=100,null=True)
    #course hsc
    course_hsc = models.CharField(max_length=200,null=True)
    school_clg_hsc = models.CharField(max_length=200, null=True)
    year_of_Passing_hsc = models.CharField(max_length=100,null=True)
    percentage_hsc= models.CharField(max_length=100,null=True)

    #course ssc
    course_ssc = models.CharField(max_length=200,null=True)
    school_clg_ssc = models.CharField(max_length=200, null=True)
    year_of_Passing_ssc = models.CharField(max_length=100,null=True)
    percentage_ssc= models.CharField(max_length=100,null=True)
    

    def __str__(self):
        return self.user.username




class EmployeeExperience(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    company1_name = models.CharField(max_length=200,null=True)
    company1_designation = models.CharField(max_length=200, null=True)
    company1_salary = models.CharField(max_length=100,null=True)
    company1_duration= models.CharField(max_length=100,null=True)

    company2_name = models.CharField(max_length=200,null=True)
    company2_designation = models.CharField(max_length=200, null=True)
    company2_salary = models.CharField(max_length=100,null=True)
    company2_duration= models.CharField(max_length=100,null=True)

    company3_name = models.CharField(max_length=200,null=True)
    company3_designation = models.CharField(max_length=200, null=True)
    company3_salary = models.CharField(max_length=100,null=True)
    company3_duration= models.CharField(max_length=100,null=True)
    

    def __str__(self):
        return self.user.username




