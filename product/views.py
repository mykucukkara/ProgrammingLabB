from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from product.models import CommentForm, Comment


# Create your views here.
def index(request):
    text = "Product Sayfası"
    return HttpResponse(text)

@login_required(login_url='/login')
def addcomment(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST': #form post edildiyse
        form = CommentForm(request.POST)
        if form.is_valid():
            current_user = request.user
            data = Comment()
            data.user_id = current_user.id
            data.product_id = id
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Yorumunuz başarı ile gönderilmiştir. Teşekkür ederiz.")
            return HttpResponseRedirect(url)
            #return HttpResponse("Kayit islemi basarili")
    messages.error(request, "Kaydedilme işlemi gerçekleştirilemedi. Lütfen kontrol ediniz.")
    return HttpResponseRedirect(url)
    #return HttpResponse("Kaydedilme işlemi gerçekleştirilemedi.")