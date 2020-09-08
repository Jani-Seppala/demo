from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelformset_factory
from django.http import HttpResponse
from .models import Tulokset, Osallistujat, Veikkaukset
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from . import forms


def index(request):
    tulokset_list = Tulokset.objects.order_by()
    context = {'tulokset_list': tulokset_list}
    print(tulokset_list)
    print(context)
    return render(request, 'futis/index.html', context)


def pistetilanne(request):
    # osallistujat_list = Osallistujat.objects.order_by()[:5]
    osallistujat_list = Osallistujat.objects.all()
    context = {'osallistujat_list': osallistujat_list}
    # output = ', '.join([o.osallistuja for o in osallistujat_list])
    print(osallistujat_list)

    return render(request, 'futis/pistetilanne.html', context)


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/futis')
    else:
        form = UserCreationForm()

    return render(request, 'futis/register.html', context={'form': form})


def luo_veikkaus(request):
    uusi_veikkaus = forms.VeikkauksetModelForm()
    if request.method == 'POST':
        uusi_veikkaus = forms.VeikkauksetModelForm(request.POST)
        if uusi_veikkaus.is_valid():
            uusi_veikkaus.save()
            return redirect('/futis')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'futis/index.html'}}">reload</a>""")
    else:
        print(uusi_veikkaus)
        print(type(uusi_veikkaus))
        return render(request, 'futis/luo_veikkaus.html', {'uusi_veikkaus_form': uusi_veikkaus})


def luo_veikkaus_beta(request):
    # AuthorFormSet = modelformset_factory(Author, fields=('name', 'title'))
    VeikkauksetFormSet = modelformset_factory(Veikkaukset, fields='__all__')
    if request.method == 'POST':
        formset = VeikkauksetFormSet(request.POST, request.FILES)
        # formset = VeikkauksetFormSet(request.POST, request.FILES, queryset=Veikkaukset.objects.filter(osallistujat__startswith='K'))
        if formset.is_valid():
            formset.save()
            return redirect('/futis')
    else:
        # formset = VeikkauksetFormSet(queryset=Veikkaukset.objects.filter(osallistujat__startswith='K'))
        formset = VeikkauksetFormSet()
    return render(request, 'futis/luo_veikkaus_beta.html', {'formset': formset})


def veikkaukset(request, pk):
    # veikkauksetdetailview_list = Veikkaukset.objects.all()
    # veikkauksetdetailview_list = Veikkaukset.objects.osallistujat.get(pk=id)
    # veikkauksetdetailview_list = Veikkaukset.objects.get(osallistujat_id=id)
    veikkaus_query = Veikkaukset.objects.filter(osallistujat_id=pk)
    context = {'veikkaus_query': veikkaus_query}
    return render(request, 'futis/veikkaus.html', context)
