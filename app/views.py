from django.shortcuts import render,redirect
from app.models import Product,Checkout,Contact
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth
from app.forms import CreateForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages



# Create your views here.
@login_required
def homeView(request):
    return render(request,"home.html")

def readDetails(request):

    all_products= Product.objects.all()

    if request.method=="POST":
        itemName = request.POST.get('search')

        if itemName !='' and itemName is not None:
            all_products = all_products.filter(name__contains=itemName)

    context={
        'all_products':all_products
    }
    return render(request,"home.html",context)

@login_required
def checkout(request):
    return render(request, "checkout.html")

class readOneData(DetailView):
    model = Product

def formView(request):
    if request.method == "POST":
        myfname = request.POST.get("fname")
        mylname = request.POST.get("lname")
        myemail = request.POST.get("email")
        myphoneno = request.POST.get("phoneno")
        mycity = request.POST.get("city")
        mypincode = request.POST.get("pincode")
        myaddress = request.POST.get("address")
        myprice = request.POST.get("price")

        c = Checkout(firstName=myfname, lastName=mylname, emailId=myemail, phoneNo=myphoneno,
                     city=mycity, pincode=mypincode, address=myaddress, price=myprice)

        c.save()

    return render(request, "form.html")
    
@login_required
def contactform(request):
    if request.method == "POST":
        myfname = request.POST.get("fname")
        mylname = request.POST.get("lname")
        myemail = request.POST.get("email")
        myphoneno = request.POST.get("phoneno")
        myquery = request.POST.get("query")
        cf = Contact(firstName=myfname, lastName=mylname, emailId=myemail, phoneNo=myphoneno,query=myquery)
        cf.save()

    return render(request, "contactus.html")

def signup(request):
    form = CreateForm()
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            return redirect("/accounts/login")
            
    context = {
        'form': form
    }
    return render(request,"signup.html", context)

def login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/read')
        else:
            messages.info(request,'Username or password is incorrect')
        
    context={}

    return render(request,'accounts/login.html',context)
@login_required
def logoutUser(request):
    logout(request)
    #return render(request,"logout.html")
    return redirect("/accounts/logout")