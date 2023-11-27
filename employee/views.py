from django.shortcuts import render, redirect  
from employee.forms import EmployeeForm  
from employee.models import Employee  



# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'user/data.html',{'form':form})  


def show(request):  
    employees = Employee.objects.all()
    return render(request,"user/Index.html",{'employees':employees})  


def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'user/edit.html', {'employee':employee})  


def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  


def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  