from django.shortcuts import render
from datetime import datetime
# Create your views here.
def filters(request):
    d={'data':'hiA HOW ARE you','dt':datetime.now(),'c':1}
    return render(request,'filters.html',d)