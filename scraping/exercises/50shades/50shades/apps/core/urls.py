from django.conf.urls import patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^exercise/1/$',
        TemplateView.as_view(template_name='core/exercise1.html'),
        name='home'),
)
