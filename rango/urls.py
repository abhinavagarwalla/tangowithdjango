
from django.conf.urls import patterns,url
from django.views.generic import TemplateView

from rango import views

urlpatterns = patterns('',
                url(r'^$',TemplateView.as_view(template_name='index.html')),
                url(r'^data$',TemplateView.as_view(template_name='data.html')),
                url(r'^data1$',TemplateView.as_view(template_name='data1.html')),
                url(r'^data2$',TemplateView.as_view(template_name='data2.html')),

            )