from .models import (UserProfile, Country, Director,
                     Actor, Genre, Movie, MovieLanguages,
                     Moments, Rating, Favorite, FavoriteMovie,
                     History)
from rest_framework import serializers


class UserPileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserPileRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name']


class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'country_name']


class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['director_name']



class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'genre_name']


class MovieListSerializer(serializers.ModelSerializer):
    year = serializers.DateField(format='%Y')
    country = CountySerializer(many=True)
    genre = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'movie_image', 'movie_name', 'year',
                  'country', 'genre', 'status_movie']

class ActorDetailSerializer(serializers.ModelSerializer):
    actor_movie = MovieListSerializer(many=True, read_only=True)
    class Meta:
        model = Actor
        fields = ['actor_name', 'bio', 'age', 'actor_image', 'actor_movie']

class GenreDetailSerializer(serializers.ModelSerializer):
    genre_movie = MovieListSerializer(many=True, read_only=True)
    class Meta:
        model = Genre
        fields = ['genre_name', 'genre_movie']

class CountyDetailSerializers(serializers.ModelSerializer):
    country_movie = MovieListSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['country_name', 'country_movie']

class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = ['director_name']



class MomentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = ['movie_moments']

class MovieLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['language', 'video']

class RatingSerializer(serializers.ModelSerializer):
    user = UserPileRatingSerializer()
    created_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M')

    class Meta:
        model = Rating
        fields = ['id', 'user', 'parent', 'stars', 'text', 'created_date']


class MovieDetailSerializer(serializers.ModelSerializer):
    year = serializers.DateField(format('%d-%m-%Y'))
    country = CountySerializer(many=True)
    director = DirectorSerializer(many=True)
    actor = ActorSerializer(many=True)
    genre = GenreSerializer(many=True)
    movie_frames = MomentsSerializer(many=True, read_only=True)
    movie_videos = MovieLanguagesSerializer(many=True, read_only=True)
    movie_ratings = RatingSerializer(many=True, read_only=True)
    get_avg_rating = serializers.SerializerMethodField()
    get_count_people = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['movie_name', 'year', 'country', 'director', 'actor', 'genre',
                  'types', 'movie_time', 'movie_image', 'movie_trailer', 'description',
                  'status_movie', 'movie_frames', 'movie_videos', 'get_avg_rating', 'get_count_people',
                  'movie_ratings',]

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()


    def get_count_people(self, obj):
        return obj.get_count_people()




class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class FavoriteMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'

