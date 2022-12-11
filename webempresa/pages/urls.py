from django.urls import path
from . import views
from .views import PageDetailView, PageUpdateView

# urlpatterns = [
#     path('<int:page_id>/<slug:page_slug>/', views.page, name='page'),
# ]

pages_patterns = ([
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
    path('update/<int:pk>/<slug:slug>/', PageUpdateView.as_view(), name='update')
], 'page')
