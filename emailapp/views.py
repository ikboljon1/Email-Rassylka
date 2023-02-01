from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from emailapp.models import Subscriber, Template 

def home_view(request): 
 subscribers = Subscriber.objects.all() 
 template_list = Template.objects.all()
 if request.method == "POST": 
  if 'subscribe' in request.POST:
   name = request.POST.get("name")
   email = request.POST.get("email")
   birthdate = request.POST.get("birthdate")
   Subscriber.objects.create(name=name, email=email, birthdate=birthdate)
  elif "change_template" in request.POST: 
   template_id = request.POST.get("template_id") 
   template = Template.objects.get(id = template_id) 
   template.variables = request.POST.get("variables")
 
 return render(request, 'index.html', { 
  'subscribers': subscribers, 
  'template_list': template_list
 })