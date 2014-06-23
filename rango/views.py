from django.shortcuts import render
from django.shortcuts import render_to_response

from django.template import RequestContext
from models import Category, Page
# Create your views here.
def index(request):
    context = RequestContext(request)
    #context_dict = {'boldmessage':"This is the bol meadd"}
    #category_list = Category.objects.order_by('-views')[:5]
    category_list = Category.objects.order_by('name')[:3]
    context_dict = {'categories': category_list}
    for category in category_list:
        category.url = category.name.replace(' ', '_')

    return render_to_response('index.html', context_dict, context)

def category(request, category_name_url):
    context = RequestContext(request)
    category_name = category_name_url.replace('_', ' ')

    context_dict = {'category_name': category_name}

    try:
        category = Category.objects.get(name=category_name)
        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass

    return render_to_response('category.html', context_dict, context)




