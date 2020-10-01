from rest_framework import routers

from .views import *


router = routers.DefaultRouter()

router.register('books', BookViewSet, basename='books')
router.register('films', FilmViewSet, basename='films')
router.register('musics', MusicViewSet, basename='musics')
