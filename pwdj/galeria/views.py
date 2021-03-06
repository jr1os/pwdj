from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse

from pwdj.galeria.facade import buscar_categorias_com_galeria
from pwdj.galeria.forms import ModelForm


def index(request):
    query_set = buscar_categorias_com_galeria()
    ctx = {
        'categorias': list(query_set)

    }
    return render(request, 'galeria/index.html', context=ctx)


@login_required
def new(request):
    return render(request, 'galeria/galeria_form.html')


@login_required
def create(request):
    # Extraia os dados do request
    form = ModelForm(request.POST)
    # Valide os Inputs
    if not form.is_valid():
        ctx = {'form': form}
        return render(request, 'galeria/galeria_form.html', context=ctx, status=400)
    # Se Válido, salve no banco e redirecione
    form.save()
    return redirect(reverse('galeria:index'))
