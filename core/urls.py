
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("blog.urls")),
    path('api/', include("blog_api.urls")),
    path('api-auth/',include("rest_framework.urls")),
    path('user/',include("users.urls")),
    path('chat/',include("chat.urls")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('docs/',include_docs_urls(title="my docs")),
    path('schema/', get_schema_view(title="my schema",description="here is my description",version="1.0.0"), name='schema'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

