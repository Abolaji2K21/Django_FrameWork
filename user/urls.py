
from django.urls import path
from .import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path("api/v1", include("demo.urls")),
    # path("user", include("account.urls"))

    path('register', views.UserRegistration.as_view())

]
