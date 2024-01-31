from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from .views import CategoryCourseViewSet, CourseViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter() # добавляет вывод /api/ с markdown
#router = SimpleRouter() # ничего не добавляет
router.register('category', CategoryCourseViewSet)
#router.register('course', CourseViewSet)                     # 1 вариант
#router.register('course', CourseViewSet, basename='model')   # 2 вариант
router.register('course', CourseViewSet, basename='model')   # 3 вариант
#router.register('auth-token', CustomAuthToken.as_view(), basename='model')


app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] 
#urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
