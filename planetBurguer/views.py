from django.shortcuts import render

# Create your views here.
def burguerindex(request):
    return render(request,'index.html')