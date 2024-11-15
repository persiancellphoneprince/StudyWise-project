from django.shortcuts import render, get_object_or_404, redirect
from .models import Subject, Offer, Favourite
from django.contrib.auth import login, authenticate, logout
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm

def home_page(request):
    subjects = Subject.objects.all()[:5]
    offers = Offer.objects.all().order_by('-created_at')[:4]

    context = {
        'subjects': subjects,
        'offers': offers
    }

    return render(request, "./home.html", context)

def offers_page(request):
    offers = Offer.objects.all().order_by('-created_at')
    context = {
        'offers': offers
    }
    return render(request,"./offers.html", context)

def subjects_page(request):
    subjects = Subject.objects.all()
    context = {
        'subjects': subjects
    }
    return render(request,"./subjects.html", context)

def favourites_page(request):
    favourites = Favourite.objects.all()
    context = {
        'favourites': favourites,
    }

    return render(request, "./favourites.html", context)

def offer_detail_page(request, pk):
    offer = get_object_or_404(Offer, pk=pk)
    context = {
        'offer': offer
    }
    return render(request, './offer_detail.html', context)

def favourite_detail_page(request, pk):
    favourite = get_object_or_404(Favourite, pk=pk)  # Изменили модель на Favourite
    context = {
        'favourite': favourite
    }
    return render(request, './favourite_detail.html', context)

def offers_by_subject_page(request, slug):
    subject = get_object_or_404(Subject, slug=slug)
    offers = Offer.objects.filter(subject=subject) 
    context = {
        'subject' : subject,
        'offers' : offers
    }
    return render(request, "./offers_by_subject.html", context)

def sign_up_page(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect ("login_page")
    else:
        form = NewUserForm()
    context = {
        'form' : form
    }
    return render(request, "./sign_up.html", context)

def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')  # Исправлена ошибка с cleaned_data
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_page')
    else:
        form = AuthenticationForm()

    context = {
        'form': form
    }
    return render(request, "./login.html", context)


def logout_action(request):
    logout(request)
    return redirect('home_page')