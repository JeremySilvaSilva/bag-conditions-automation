from django.shortcuts import render
from app.builder.models import (
    Factor
)
from .values import Factor_values
from django.core.paginator import Paginator

def index(request):
    values = Factor_values.factor_all
    factor = Factor.objects.values(*values).order_by('id')
    paginator = Paginator(factor,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'home/index.html',context)

