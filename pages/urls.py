from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url('^$', TemplateView.as_view(template_name='pages/index.html')),
    url('^join/tutors$', TemplateView.as_view(template_name='pages/join/tutors.html'))
]
