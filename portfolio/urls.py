from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'portfolio'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^customer_list/$', views.customer_list, name='customer_list'),
    url(r'^customer/create/$', views.customer_new, name='customer_new'),
    url(r'^customer/(?P<pk>\d+)/delete/$', views.customer_delete, name='customer_delete'),
    url(r'^customer/(?P<pk>\d+)/edit/', views.customer_edit, name='customer_edit'),
    # url(r'^customer/(?P<pk>\d+)/portfolio/$', views.portfolio, name='portfolio'),
    url(r'^investment_list/$', views.investment_list, name='investment_list'),
    url(r'^investment/(?P<pk>\d+)/delete/$', views.investment_delete, name='investment_delete'),
    url(r'^investment/(?P<pk>\d+)/edit/$', views.investment_edit, name='investment_edit'),
    url(r'^investment/create/$', views.investment_new, name='investment_new'),
    url(r'^stock_list/$', views.stock_list, name='stock_list'),
    url(r'^stock/(?P<pk>\d+)/delete/$', views.stock_delete, name='stock_delete'),
    url(r'^stock/(?P<pk>\d+)/edit/$', views.stock_edit, name='stock_edit'),
    url(r'^stock/create/$', views.stock_new, name='stock_new'),

]
