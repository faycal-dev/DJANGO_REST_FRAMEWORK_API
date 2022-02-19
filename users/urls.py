from django.urls import path
from .views import CustomUserCreate, BlacklistTokenView


urlpatterns = [
    path('create/', CustomUserCreate.as_view(), name="create_user"),
    path('logout/', BlacklistTokenView.as_view(), name="create_user"),
]
