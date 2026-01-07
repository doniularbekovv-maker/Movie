from .views import (UserProfileViewSet, CountryListAPIView, CountryDetailAPIView,
                    DirectorListAPIView, DirectorDetailAPIView, ActorListAPIView,
                    ActorDetailAPIView, GenreListAPIView, GenreDetailAPIView,
                    MovieListAPIView, MovieDetailAPIView, MovieLanguagesViewSer,
                    MomentsViewSer, RatingViewSer, FavoriteViewSer,
                    FavoriteMovieViewSer, HistoryViewSer,)
from rest_framework import routers
from django.urls import path, include


router = routers.SimpleRouter()
router.register(r'Users', UserProfileViewSet)
router.register(r'movie_lan', MovieLanguagesViewSer)
router.register(r'moments', MomentsViewSer)
router.register(r'rating', RatingViewSer)
router.register(r'favorites', FavoriteViewSer)
router.register(r'favorite_item', FavoriteMovieViewSer)
router.register(r'history', HistoryViewSer)


urlpatterns =  [
    path('', include(router.urls)),
    path('movie/', MovieListAPIView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailAPIView.as_view(),name='movie_detail'),
    path('country/', CountryListAPIView.as_view(), name='country_list'),
    path('country/<int:pk>/', CountryDetailAPIView.as_view(), name='country_detail'),
    path('director/', DirectorListAPIView.as_view(),name='director_list'),
    path('director/<int:pk>', DirectorDetailAPIView.as_view(), name='director_detail'),
    path('actor/', ActorListAPIView.as_view(),name='actor_list'),
    path('actor/<int:pk>', ActorDetailAPIView.as_view(), name='actor_detail'),
    path('genre/', GenreListAPIView.as_view(),name='genre_list'),
    path('genre/<int:pk>', GenreDetailAPIView.as_view(), name='genre_detail'),

]