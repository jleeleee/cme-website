from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url('^$', TemplateView.as_view(template_name='pages/index.html')),
    url('^join/tutors$', TemplateView.as_view(template_name='pages/join/tutors.html')),
    url('^join/students$', TemplateView.as_view(template_name='pages/join/students.html')),
    url('^join/donate$', TemplateView.as_view(template_name='pages/join/donate.html')),
    url('^about/directors$', TemplateView.as_view(template_name='pages/about/directors.html')),
    url('^about/story$', TemplateView.as_view(template_name='pages/about/story.html')),
    url('^information/curriculum$', TemplateView.as_view(template_name='pages/information/curriculum.html')),
    url('^information/general$', TemplateView.as_view(template_name='pages/information/general.html')),
    url('^activities/gallery$', TemplateView.as_view(template_name='pages/activities/gallery.html')),
    url('^activities/news$', TemplateView.as_view(template_name='pages/activities/news.html')),
    url('^contact$', TemplateView.as_view(template_name='pages/contact.html')),
    url('^services/performances$', TemplateView.as_view(template_name='pages/services/performances.html')),
    url('^services/tutors$', TemplateView.as_view(template_name='pages/services/tutors.html')),
    url('^services/structure$', TemplateView.as_view(template_name='pages/services/structure.html')),

]
