from django.urls import path, include

# from .views import add_item, remove_item
from . import views


# urlpatterns = [path("addItemToCart/", add_item), path("removeItem/", remove_item)]
urlpatterns = [
    path("test/", views.detail),

]
