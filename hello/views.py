from django.shortcuts import render

# Create your views here.
def home(request):
    name="Rajan"
    fees=500
    seats=23
    details={"nm":name,"f":fees,"s":seats}
    return render(request,"hello/home.html",details)
