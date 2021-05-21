from django.shortcuts import loader, render
from django.http import HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from . import forms
from sympy import pprint, init_printing, simplify


def matrix(request):
    template = loader.get_template('Matrix/Home-page.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


@csrf_protect
def det(request, n):

    cols = int(n)
    form = forms.MatrixForm(n=cols)

    context = {
        'title': 'Determinant',
        'n': n,
        'n_plus_1': str(cols + 1),
        'n_min_1': str(cols - 1),
        'form': form,
    }

    init_printing(use_unicode=True)

    if request.method == 'POST':
        form = forms.MatrixForm(request.POST,n=cols)
        if form.is_valid():
            context['form'] = form
            M = form.GetMatrix()
            context['matrix'] = M
            det = form.GetDet()
            context['det'] = det
        else:
            context['matrix'] = ""
    else:
        context['matrix'] = ""

    return render(request, 'Matrix/Matrix-page.html', context)


def inversa(request, n):
    cols = int(n)
    form = forms.MatrixForm(n=cols)

    context = {
        'title': 'Inversa',
        'n': n,
        'n_plus_1': str(cols + 1),
        'n_min_1': str(cols - 1),
        'form': form,
    }

    init_printing(use_unicode=True)

    if request.method == 'POST':
        form = forms.MatrixForm(request.POST, n=cols)
        if form.is_valid():
            context['form'] = form
            M = form.GetMatrix()
            context['matrix'] = M
            det = form.GetDet()
            if det != 0:
                context['reverse'] = form.GetInversa()
            context['det'] = det
        else:
            context['matrix'] = ""
    else:
        context['matrix'] = ""

    return render(request, 'Matrix/Matrix-page.html', context)

