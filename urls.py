from django.urls import path
from .views import IndexView, AboutView, ContactView,NewsView, ApplyView, DashboardView,ProfileUpdateView, ProfileDeleteView
from django.contrib.auth.views import LoginView, LogoutView
from .import views

app_name = "account"
urlpatterns = [
    path("", IndexView.as_view(), name="home-page"),
    path("login/",LoginView.as_view(template_name="login.html"), name="login-page"),
    path("logout",LogoutView.as_view(), name="logout-page"),
    path("about",AboutView.as_view(), name="about-page"),
    path("news",NewsView.as_view(), name="news-page"),
    path("contact",ContactView.as_view(), name="contact-page"),
    path("apply",ApplyView.as_view(), name="apply-page"),
    path("dashboard/",DashboardView.as_view(), name="dashboard"),
    path("update_profile/<int:pk>",ProfileUpdateView.as_view(), name="update-profile"), 
    path("delete_profile/<int:pk>",ProfileDeleteView.as_view(), name="delete_profile")

]







