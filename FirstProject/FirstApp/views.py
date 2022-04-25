from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeModelForm

def addEmployeeModelForm(request):
    form = EmployeeModelForm()
    if request.method == 'POST':
        print('post')
        form = EmployeeModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_emp')
    template_name = 'FirstApp/addemployee.html'
    context = {'form':form}
    return render(request,template_name,context)

def showEmployee(request):
    employee = Employee.objects.all()
    template_name = 'FirstApp/showemployee.html'
    context = {'employee':employee}
    return render(request,template_name,context)

def deleteEmployee(request,i):
    employee = Employee.objects.get(eid=i)
    if request.method == 'POST':
        employee.delete()
        return redirect('add_emp')
    template_name = 'FirstApp/deleteemployee.html'
    context = {'employee':employee}
    return render(request,template_name,context)

def updateView(request,i):
    employee = Employee.objects.get(eid=i)
    form = EmployeeModelForm(instance=employee)
    if request.method == 'POST':
        form = EmployeeModelForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('show_emp')
    context = {'form':form}
    template_name = 'FirstApp/addemployee.html'
    return render(request,template_name,context)
# Create your views here.
