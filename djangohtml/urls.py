from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^kpidetails/', 'display_html.views.FileDisplayTable', name = 'FileDisplayTable'),
    url(r'^xunit/', 'display_html.views.XmlFileDisplay', name='XmlFileDisplay'),
    url(r'^kpi/', 'display_html.views.kpi', name='kpi'),
    url(r'^mstest/', 'display_html.views.mstest', name='mstest'),
    url(r'^total/', 'display_html.views.total', name='total'),


]
