from django.conf.urls import url
from .views import ChatView

urlpatterns = [
    url(r'send/', view=ChatView.as_view()),
]