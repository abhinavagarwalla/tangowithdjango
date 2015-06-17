from django.shortcuts import render
from django.shortcuts import render_to_response
from django.conf import settings
from django.template import RequestContext
from models import Category
# Create your views here.

def index(request):
    category_list = Category.objects.all()
    context_dict = {'categories': category_list}

    # Render the response and send it back!
    return render(request, 'index.html', context_dict)

def category(request, category_name):
    context_dict = {}
    context_dict['imgpath'] = category_name

    f = open(settings.STATIC_PATH + '/TO/' + category_name + '.txt').read()
    g = open(settings.STATIC_PATH + '/SauvolaTO/' + category_name + '.txt').read()
    context_dict['TOoutput'] = f
    context_dict['Sauvolaoutput'] = g

    return render(request, 'category.html', context_dict)
