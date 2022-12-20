from django.http import HttpResponse
from django.shortcuts import render

from home.models import UserProfile, Setting


# Create your views here.

def index(request):
    if(request.user.id == None):
        return render(request, 'user_profile.html')
    else:
        user = UserProfile.objects.get(user_id=request.user.id)
        settings = Setting.objects.filter(pk=0)
        context = {'user': user,
               'settings': settings}
        return render(request, 'user_profile.html', context)
