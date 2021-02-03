from django_filters import rest_framework as filters

from blog.models import Post


class PostsFilter(filters.FilterSet):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    publish_year_min = filters.NumberFilter(
        field_name='publish',
        lookup_expr='year__gte',
        label='publish_year_min',
    )
    publish_year_max = filters.NumberFilter(
        field_name='publish',
        lookup_expr='year__lte',
        label='publish_year_max',
    )
    publish_month_min = filters.NumberFilter(
        field_name='publish',
        lookup_expr='month__gte',
        label='publish_month_min',
    )
    publish_month_max = filters.NumberFilter(
        field_name='publish',
        lookup_expr='month__lte',
        label='publish_month_max',
    )
    publish_day_min = filters.NumberFilter(
        field_name='publish',
        lookup_expr='day__gte',
        label='publish_day_min',
    )
    publish_day_max = filters.NumberFilter(
        field_name='publish',
        lookup_expr='day__lte',
        label='publish_day_max',
    )
    author = filters.CharFilter(
        field_name='author__username',
        lookup_expr='exact',
    )
    status = filters.ChoiceFilter(choices=STATUS_CHOICES, )

    class Meta:
        model = Post
        fields = ('status', 'author',)
