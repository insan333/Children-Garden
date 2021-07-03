from django.contrib import admin
from django.urls import path
from .views import Children_Garden1View,MainView,Children_Garden2View,Children_Garden3View,Educator1View,Educator2View,Educator3View,Educator4View,Educator5View,Educator6View,Educator7View,Educator8View,Educator9View

urlpatterns = [
    path("", MainView.as_view(), name="main_wrap"),
    path("garden1/", Children_Garden1View.as_view(), name="children_gardens1"),
    path("garden2/", Children_Garden2View.as_view(), name="children_gardens2"),
    path("garden3/", Children_Garden3View.as_view(), name="children_gardens3"),
    path("educators1/", Educator1View.as_view(), name="educators1"),
    path("educators2/", Educator2View.as_view(), name="educators2"),
    path("educators3/", Educator3View.as_view(), name="educators3"),
    path("educators4/", Educator4View.as_view(), name="educators4"),
    path("educators5/", Educator5View.as_view(), name="educators5"),
    path("educators6/", Educator6View.as_view(), name="educators6"),
    path("educators7/", Educator7View.as_view(), name="educators7"),
    path("educators8/", Educator8View.as_view(), name="educators8"),
    path("educators9/", Educator9View.as_view(), name="educators9"),
]
