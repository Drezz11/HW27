
from django.urls import path

from ads.views import CatListCreateView, CategoryDerailView

urlpatterns = [
    path('', CatListCreateView.as_view()),
    path('<int:pk>', CategoryDerailView.as_view())
]