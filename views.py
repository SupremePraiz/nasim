from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


from .models import Profile
from .forms import ProfileForm

# Create your views here.
class IndexView(TemplateView):
   template_name ="account/index.html"

class AboutView(TemplateView):
    template_name ="account/about.html"

class NewsView(TemplateView):
    template_name ="account/news.html"

class ContactView(TemplateView):
    template_name ="account/contact.html"

class ApplyView(TemplateView):
    template_name ="account/apply.html"



class DashboardView(LoginRequiredMixin,TemplateView):
    template_name = "account/dashboard.html"
    login_url = "/login/"


class ProfileUpdateView(SuccessMessageMixin,UpdateView):
    template_name = "account/update_profile.html"
    model = Profile
    form_class = ProfileForm
    success_url = "/dashboard/"
    success_message = "profile updated successfully"


class ProfileDeleteView(DeleteView):
    template_name = "account/profile_delete.html"
    model = Profile
    context_object_name = "profile"
    success_url = "/login/"


    

# class ProfileCreateView(TemplateView):
#     template_name = "account/create_profile.html"
#     form_class = ProfileForm
#     success_url = "/dashbord/"



# def dashboard(request):
#     context = Profile.objects.all()
#     form =  ProfileForm()
#     if request.method =="POST":
#         form = ProfileForm(request.POST or None)
#         if form.is_valid():
#             form.save()

#         return HttpResponseRedirect("/")
#     return render(request,"account/dashboard.html",{"form":form})