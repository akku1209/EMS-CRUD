from django.shortcuts import render,redirect
from myApp.forms import signupForm
from django.contrib.auth.decorators import login_required
from myApp.models import Employee
from myApp.forms import EmployeeForm

def home_view(request):
    e=Employee.objects.all()
    d={"Emp":e}
    return render(request,'myApp/home.html',d)
@login_required
def insert_view(request):
    f=EmployeeForm()
    if request.method=="POST":
        f=EmployeeForm(request.POST )
        if f.is_valid():
            f.save(commit=True)
        return redirect('/')
    d={"form":f}
    return render(request,"myApp/insert.html",d)
@login_required
def delete_view(request,id):
    e=Employee.objects.get(id=id)
    e.delete()
    return redirect('/')
@login_required
def update_view(request,id):
    e=Employee.objects.get(id=id)
    if request.method=="POST":
        f=EmployeeForm(request.POST,instance=e )
        if f.is_valid():
            f.save(commit=True)
        return redirect('/')
    d={"Emp":e}
    return render(request,"myApp/update.html",d)
def logout(request):
    return render(request, 'myApp/logout.html')
def signup(request):
    f=signupForm()
    if (request.method=="POST"):
        f=signupForm(request.POST)
        user=f.save()
        user.set_password(user.password)
        user.save()
        return redirect("/accounts/login")
    d={"form":f}
    return render(request, 'myApp/signup.html',d)
