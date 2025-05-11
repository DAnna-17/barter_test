from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from rest_framework import viewsets, permissions
from django.contrib.auth.decorators import login_required

from api.serializers import AdSerializer, ExchangeProposalSerializer

from .forms import NewAdForm, OfferBarter, EditAdForm, FilterForm
from .models import Ad, ExchangeProposal



@login_required(login_url='login')
def lk_page(request):
    if request.method == "POST":
        form = NewAdForm(request.POST)

        if form.is_valid():

            u_title = form.cleaned_data.get("title")
            u_desc = form.cleaned_data.get("description")
            u_cat = form.cleaned_data.get("category")
            u_cond = form.cleaned_data.get("condition")

            print(u_cat)

            result = Ad(title=u_title, description=u_desc, category=u_cat, condition=u_cond, user_id=request.user.id)
            result.save()

            return HttpResponseRedirect("/")

    else:
        form = NewAdForm()

        y_ads = Ad.objects.filter(user_id=request.user.id)
        print(request.user.id)

    return render(request, "lk_page.html", {"form": form, "your_ads": y_ads})


@login_required(login_url='login')
def delete_ad(request, ad_id):
    task = Ad.objects.get(id=ad_id)
    task.delete()

    return redirect('/')

@login_required(login_url='login')
def accept_off(request, off_id):
    off = ExchangeProposal.objects.get(id=off_id)
    off.status = 1
    off.save()

    return redirect('/offers')

@login_required(login_url='login')
def deny_off(request, off_id):
    off = ExchangeProposal.objects.get(id=off_id)
    off.status = -1
    off.save()

    return redirect('/offers')


@login_required(login_url='login')
def ads_page(request):

    ads = Ad.objects.exclude(user_id=request.user.id)

    if request.method == "POST":

        form = OfferBarter(request.user, request.POST)
        form1 = FilterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/all')
        if form1.is_valid():
            ads = ads.filter(condition=form1.cleaned_data.get("condition"), title__contains=form1.cleaned_data.get("title"),
                             category=form1.cleaned_data.get("category"))
    else:
        form = OfferBarter(request.user)
        form1 = FilterForm()


    return render(request, "ads_page.html", {"available_ads": ads, "form": form, "form1": form1})


@login_required(login_url='login')
def offers_page(request):
    off_ads = ExchangeProposal.objects.filter(ad_receiver__user=request.user.id)

    return render(request, "offers_page.html", {"offered_ads": off_ads})


@login_required(login_url='login')
def edit_ad(request, ad_id):
    ad = Ad.objects.get(id=ad_id)
    if request.method == "POST":
        form = EditAdForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            form.save()
            return redirect('ad_list')
    else:
        form = EditAdForm(ad_id, request.POST)
    return render(request, 'edit_ad.html', {'form': form, 'ad': ad})