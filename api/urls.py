from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from .views import CategoryCourseViewSet

router = DefaultRouter() # добавляет вывод /api/ с markdown
#router = SimpleRouter() # ничего не добавляет
router.register('category', CategoryCourseViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls))
    
] 
#urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
