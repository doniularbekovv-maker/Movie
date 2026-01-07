from .models import (UserProfile, Director, Country,
                     Actor, Genre, Movie, MovieLanguages,
                     Moments, Rating, Favorite, FavoriteMovie,
                     History)
from .serializers import (UserPileSerializer, CountySerializer, CountyDetailSerializers,
                       DirectorSerializer, DirectorDetailSerializer, ActorSerializer,
                       GenreSerializer, MovieListSerializer, MovieDetailSerializer,
                       RatingSerializer, FavoriteSerializer,
                       FavoriteMovieSerializer, HistorySerializer, MovieLanguagesSerializer, MomentsSerializer, ActorDetailSerializer)
from rest_framework import viewsets, generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MovieFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from .pagination import MoviePagination
from .porminssions import CheckStatus, RatingPermission


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserPileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)



class CountryListAPIView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountySerializer


class CountryDetailAPIView(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountyDetailSerializers


class DirectorListAPIView(generics.ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class DirectorDetailAPIView(generics.ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorDetailSerializer

class ActorListAPIView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorDetailAPIView(generics.RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializer


class GenreListAPIView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDetailAPIView(generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class MovieListAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = MovieFilter
    search_fields = ['movie_name']
    ordering_fields = ['year']
    pagination_class = MoviePagination
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]


class MovieDetailAPIView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
    permissions_classes = [CheckStatus]

class MovieLanguagesViewSer(viewsets.ModelViewSet):
    queryset = MovieLanguages.objects.all()
    serializer_class = MovieLanguagesSerializer


class MomentsViewSer(viewsets.ModelViewSet):
    queryset = Moments.objects.all()
    serializer_class = MomentsSerializer


class RatingViewSer(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class FavoriteViewSer(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permissions_classes = [RatingPermission]


class FavoriteMovieViewSer(viewsets.ModelViewSet):
    queryset = FavoriteMovie.objects.all()
    serializer_class = FavoriteMovieSerializer


class HistoryViewSer(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
