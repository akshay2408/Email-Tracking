from django.urls import path, include
# from .tracking import views
# from email_tracking.tracking import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('tracking.urls')),  # create, replied and bounced msg
]
