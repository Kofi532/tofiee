from django.shortcuts import render, redirect
from .models import Member
from .forms import memberf
from django.views.generic import ListView, CreateView
from django.views import generic
import Levenshtein
import pandas as pd
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from datetime import datetime
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def find_closest_string(element, string_list):
    closest_element = min(string_list, key=lambda x: Levenshtein.distance(x, element))
    return closest_element
# Create your views here.

def first(request):
    if request.method == 'POST':
        region_ = request.POST.get('regional')
        city_ = request.POST.get('district')
        price_from_ = request.POST.get('price_from') 
        price_to_ = request.POST.get('price_to') 
        reason_ = request.POST.get('reason') 
        room_ = request.POST.get('rooms') 
        words = region_.split('_')
        capitalized_words = [word.capitalize() if i == 0 else word for i, word in enumerate(words)]
        output_string = ' '.join(capitalized_words)
        words = city_.split()
        capitalized_city = [word.capitalize() for word in words]
        capitalized_string = ' '.join(capitalized_city)

        if reason_ == None:
            r =1
            drop = Member.objects.filter(region__icontains=output_string).filter(city__icontains=capitalized_string).filter(price__gte=price_from_, price__lte=price_to_)
        elif room_ == None:
            r=2
            drop = Member.objects.filter(region__icontains=output_string).filter(city__icontains=capitalized_string).filter(category__icontains=reason_).filter(price__gte=price_from_, price__lte=price_to_)
        else:
            r=3
            drop = Member.objects.filter(region__icontains=output_string).filter(city__icontains=capitalized_string).filter(rooms=room_).filter(category__icontains=reason_).filter(price__gte=price_from_, price__lte=price_to_)
        
        return render (request=request, template_name="filter.html", context={"member":drop})
    member = Member.objects.all().order_by('-date')[:2]
    members = Member.objects.all().order_by('-date')[:10]
    return render (request=request, template_name="index.html", context={"member":member, "members":members})


class Memberview(CreateView): 
    model = Member
    form_class = memberf
    success_url = "/"
    template_name = "one.html"
    
class PostDetail(generic.DetailView):
    model = Member
    template_name = 'details.html'

class UserDetail(generic.DetailView):
    model = Member
    template_name = 'userdetails.html'

def sell(request):
    member = Member.objects.all().order_by('-date')
    return render (request=request, template_name="sell.html", context={"member":member})

def buy(request):
    if request.method == "POST":
        region_ = request.POST.get('region')
        city_ = request.POST.get('district')
        price_from_ = request.POST.get('price_from') 
        price_to_ = request.POST.get('price_to') 
        room_ = request.POST.get('rooms') 
        words = region_.split('_')
        capitalized_words = [word.capitalize() if i == 0 else word for i, word in enumerate(words)]
        output_string = ' '.join(capitalized_words)
        words = city_.split()
        capitalized_city = [word.capitalize() for word in words]
        capitalized_string = ' '.join(capitalized_city)
        if room_ == None:
                r=2
                drop = Member.objects.filter(region__icontains=output_string).filter(city__icontains=capitalized_string).filter(category__icontains='rent').filter(price__gte=price_from_, price__lte=price_to_)
        else:
                r=3
                drop = Member.objects.filter(region__icontains=output_string).filter(city__icontains=capitalized_string).filter(rooms=room_).filter(category__icontains='rent').filter(price__gte=price_from_, price__lte=price_to_)
        return render (request=request, template_name="rent.html", context={"member":drop})

    member = Member.objects.all().order_by('-date')
    return render (request=request, template_name="buy.html", context={"member":member})

def rent(request):
    if request.method == "POST":
        region_ = request.POST.get('region')
        city_ = request.POST.get('district')
        price_from_ = request.POST.get('price_from') 
        price_to_ = request.POST.get('price_to') 
        room_ = request.POST.get('rooms') 
        item = request.POST.get('item_p')
        maxtime =  request.POST.get('maxtime')
        words = region_.split('_')
        capitalized_words = [word.capitalize() if i == 0 else word for i, word in enumerate(words)]
        output_string = ' '.join(capitalized_words)
        words = city_.split()
        capitalized_city = [word.capitalize() for word in words]
        capitalized_string = ' '.join(capitalized_city)
        if room_ == None:
                r=2
                drop = Member.objects.filter(region__icontains=output_string).filter(city__icontains=capitalized_string).filter(category__icontains='rent').filter(price__gte=price_from_, price__lte=price_to_)
        else:
                r=3
                drop = Member.objects.filter(region__icontains=output_string).filter(city__icontains=capitalized_string).filter(rooms=room_).filter(category__icontains='rent').filter(price__gte=price_from_, price__lte=price_to_)
        return render (request=request, template_name="rent.html", context={"member":drop})
    member = Member.objects.all().order_by('-date')
    return render (request=request, template_name="rent.html", context={"member":member})

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def user(request):
    if request.user.is_authenticated:
        username = request.user.username

        member = Member.objects.all().filter(username= username).order_by('-date')
        return render (request=request, template_name="user.html", context={"member":member})
    else:
        return HttpResponse("Hello, guest! Please login to continue")
    
def boss(request):
    username = request.user.username
    if username == 'kofiadukpo':
        
        member = Member.objects.all().order_by('-date')
        return render (request=request, template_name="boss.html", context={"member":member})
    else:
        return HttpResponse("Hello, guest! Please login to continue")

def delete_record(request, record_id):
    record = get_object_or_404(Member, pk=record_id)
    record.delete()
    return redirect('user') 

def approve_record(request, record_id):
    record = get_object_or_404(Member, pk=record_id)
    record.active= '1'
    record.save()
    return redirect('user') 

def user_form(request):
    
    
    if request.user.is_authenticated:
         usernamed = request.user.username
    if request.method == 'POST':
        cat = request.POST['category']
        rent_from = request.POST['availability_from']
        rent_to = request.POST['availability_to']
        city = request.POST['district']
        region = request.POST['regional']
        facility = request.POST['item_p']
        period = request.POST['period']
        maxtime = request.POST['maxtime']
        form = memberf(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.date = datetime.today()
            event.username = usernamed
            words = region.split('_')
            capitalized_words = [word.capitalize() if i == 0 else word for i, word in enumerate(words)]
            output_string = ' '.join(capitalized_words)
            words = city.split()
            capitalized_city = [word.capitalize() for word in words]
            capitalized_string = ' '.join(capitalized_city)
            event.region = output_string
            event.city = capitalized_string
            event.availability_to = rent_to
            event.availability_from = rent_from
            event.category=cat
            event.period = period
            event.period_number = maxtime
            event.facility = facility
            form.save()
            return HttpResponseRedirect(reverse('user'))
    else:
        form = memberf()
    
    return render(request, 'userinput.html', {'form': form})

def update(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('edituser.html')
  context = {
    'object': mymember,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  price = request.POST['price']
  title = request.POST['title']
  region = request.POST['regional']
  city = request.POST['city']
  description = request.POST['description']
  size = request.POST['size']
  contact = request.POST['contact']
  dp = request.FILES['dp']
  pic1 = request.FILES['pic1']
  pic2 = request.FILES['pic2']
  pic3 = request.FILES['pic3']
  pic4 = request.FILES['pic4']
  pic5 = request.FILES['pic5']
  pic6 = request.FILES['pic6']
  rooms = request.POST['rooms']
  category = request.POST['category']
  bathrooms = request.POST['bathrooms']
  utilities = request.POST['utilities']
  town = request.POST['town']
  availability_from = request.POST['availability_from']
  availability_to = request.POST['availability_to']
  facility = request.POST['item_p']
  period = request.POST['period']
  maxtime = request.POST['maxtime']
  member = Member.objects.get(id=id)
  member.price = price
  member.title = title
  member.region = region
  member.city = city
  member.description=description
  member.size=size
  member.contact=contact
  member.dp = dp
  member.pic1=pic1
  member.pic2=pic2
  member.pic3=pic3
  member.pic4=pic4
  member.pic5=pic5
  member.pic6=pic6
  member.rooms=rooms
  member.bathrooms=bathrooms
  member.category=category
  member.utilities=utilities
  member.availability_from= availability_from
  member.availability_to=availability_to
  member.period=period
  member.period_number=maxtime
  member.facility=facility

  member.save()
  return HttpResponseRedirect(reverse('user'))


