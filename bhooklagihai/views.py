from django.shortcuts import render
from django.http import HttpResponse
from bhooklagihai.models import book_table

# Create your views here.python
def home (request):
    return render(request,'home.html')

def about (request):
    return render(request,'about.html')

def contact (request):
    return render(request,'contact.html')

def book_table (request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        date = request.POST.get('date')
        person = request.POST.get('person')

        # if (name !='' and email !='' and number !='' and date !='' and person !=''):

        #     data = book_table(Name = name,Email = email , Person = person , Date = date , Number =number)

        #     data.save()


    return render(request,'book_table.html')



