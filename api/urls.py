from django.urls import path, include
from rest_framework.routers import DefaultRouter  # , SimpleRouter
from .views import CategoryCourseViewSet, CourseViewSet, ScUserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()  # добавляет вывод /api/ с markdown
# router = SimpleRouter() # ничего не добавляет
router.register('category', CategoryCourseViewSet, basename='category')
router.register('course', CourseViewSet, basename='course')
router.register('user', ScUserViewSet, basename='user')
# router.register('category/<int:pk>', CategoryCourseViewSet, basename='model')
# router.register('course', CourseViewSet)                     # 1 вариант
# router.register('course', CourseViewSet, basename='model')   # 2 вариант
# # 3 вариант
# router.register('auth-token', CustomAuthToken.as_view(), basename='model')


app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
