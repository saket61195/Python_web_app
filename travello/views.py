from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):

    dest1=Destination()
    dest1.name='Mumbai'
    dest1.desc='city never sleep'
    dest1.img='destination_1.jpg'
    dest1.price=1100
    dest1.offer=False

    dest2=Destination()
    dest2.name='hydrabad'
    dest2.desc='briyani'
    dest2.img='destination_2.jpg'
    dest2.price=800
    dest2.offer=True

    dest3=Destination()
    dest3.name='bihar'
    dest3.desc='littti'
    dest3.img='destination_3.jpg'
    dest3.price=900
    dest3.offer=False

    dests = [dest1,dest2,dest3]
    return render(request,'index.html',{'dests':dests })