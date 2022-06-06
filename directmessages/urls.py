from django.urls import path
from . import views 
from .views import MessageCreateView, InboxListView


urlpatterns = [
    path('new/<username>', MessageCreateView.as_view(), name='message-form'),
    path('inbox/', InboxListView.as_view(), name='inbox-list'),
]
