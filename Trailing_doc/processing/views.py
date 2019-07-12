from django.shortcuts import render
from .forms import chk
from .models import *


def index(request):
    pi = personinfo.objects.all().filter(completed=0)[0]
    chklist = checklist_master.objects.filter(chk_type=pi.Brand)
    return render(request,'index.html',{'pi':pi,'chklist':chklist})
