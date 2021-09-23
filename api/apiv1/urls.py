from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from .views import 
router = DefaultRouter()
router.register(r'jwt/', obtain_jwt_token.as_view(), basename="JWT_Token")
router.register(r'jwt/refresh/', refresh_jwt_token.as_view(), basename="JWT_Token_Refresh")
router.register(r'jwt/verify/', verify_jwt_token.as_view(), basename="JWT_Token_Verify")

urlpatterns = [path("", include(router.urls))]
