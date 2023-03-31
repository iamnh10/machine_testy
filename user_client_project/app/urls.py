from django.urls import path
from .views import CreateUserView,ClientListView, ClientCreateView,ClientDetailView,ProjectCreateView,ProjectListView

urlpatterns = [
    path('', CreateUserView.as_view()),
    path('users/<int:pk>/', CreateUserView.as_view()),
    path('client/', ClientCreateView.as_view()),
    path('clients/', ClientListView.as_view()),
    path('clients/<int:pk>/', ClientDetailView.as_view()),
    path('projects/', ProjectCreateView.as_view()),
    path('projects/assigned/', ProjectListView.as_view()),

]

