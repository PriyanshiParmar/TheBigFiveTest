from unicodedata import name
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('testpage1', views.testpage1, name='testpage1'),
    path('testpage2', views.testpage2, name='testpage2'),
    path('testpage3', views.testpage3, name='testpage3'),
    path('testpage4', views.testpage4, name='testpage4'),
    path('testpage5', views.testpage5, name='testpage5'),
    path('finalSubmit', views.finalSubmit, name='finalSubmit'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('contactus',views.contactus,name='contactus'),
    path('process1', views.process1, name='process1'),
    path('addResponse', views.addResponse, name='addResponse'),
    # path('process2', views.process2, name='process2'),
    path('process2/<flag>', views.process2, name='process2'),
    path('process3/<flag>', views.process3, name='process3'),
    path('process4/<flag>', views.process4, name='process4'),
    path('process5/<flag>', views.process5, name='process5'),
    # path('modelGeneration', views.modelGeneration, name=views.modelGeneration),
]