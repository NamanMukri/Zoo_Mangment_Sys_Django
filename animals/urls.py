from django.urls import path
from . import views

urlpatterns=[
path('mammals/', views.mammals, name="mammals"),
path('mammals/<str:name>', views.mammal, name="mammals"),
path('birds/', views.birds, name="birds"),
path('birds/<str:name>', views.bird, name="birds"),
path('fishes/', views.fishes, name="fishes"),
path('fishes/<str:species>', views.fish, name="fishes"),
]
