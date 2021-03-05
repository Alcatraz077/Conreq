from datetime import datetime, timedelta

from django.utils.text import slugify


def preprocess_filters(preset_filters, slug):
    """Do any preprocessing needed on the filters"""
    processed_filters = {}

    if slug:
        # Slugify all filter names
        for item in preset_filters:
            processed_filters[slugify(item)] = preset_filters[item]

    if processed_filters:
        return processed_filters
    return preset_filters


def combined_filters(filter_name=None, slug=False):
    """These filters are automatically merged into TV and Movies."""
    today = datetime.today()
    preset_filters = {
        "new and loved": {
            "sort_by": "vote_average.desc",
            "vote_count.gte": 50,
            "first_air_date.gte": (today - timedelta(days=365)).strftime(r"%Y-%m-%d"),
            "first_air_date.lte": today.strftime(r"%Y-%m-%d"),
            "primary_release_date.gte": (today - timedelta(days=365)).strftime(
                r"%Y-%m-%d"
            ),
            "primary_release_date.lte": today.strftime(r"%Y-%m-%d"),
            "without_keywords": "10103,161155",
            "with_original_language": "en|ja",
        },
        "all time favorites": {
            "sort_by": "vote_average.desc",
            "vote_count.gte": 1500,
            "without_keywords": "10103,161155",
            "with_original_language": "en|ja",
        },
        "coming soon": {
            "sort_by": "popularity.desc",
            "first_air_date.gte": today.strftime(r"%Y-%m-%d"),
            "first_air_date.lte": (today + timedelta(days=365)).strftime(r"%Y-%m-%d"),
            "primary_release_date.gte": today.strftime(r"%Y-%m-%d"),
            "primary_release_date.lte": (today + timedelta(days=365)).strftime(
                r"%Y-%m-%d"
            ),
            "without_keywords": "10103,161155",
            "with_original_language": "en|ja",
        },
        "top rated": {
            "sort_by": "vote_average.desc",
            "vote_count.gte": 300,
            "without_keywords": "10103,161155",
            "with_original_language": "en|ja",
        },
        "popular": {
            "sort_by": "popularity.desc",
            "without_keywords": "10103,161155",
            "with_original_language": "en|ja",
        },
        "top rated, english only": {
            "sort_by": "vote_average.desc",
            "vote_count.gte": 300,
            "without_keywords": "10103,161155",
            "with_original_language": "en",
        },
        "popular, english only": {
            "sort_by": "popularity.desc",
            "without_keywords": "10103,161155",
            "with_original_language": "en",
        },
        "top rated anime": {
            "sort_by": "vote_average.desc",
            "vote_count.gte": 50,
            "with_genres": 16,
            "with_keywords": 210024,
            "without_keywords": "10103,161155",
            "with_original_language": "ja",
        },
        "popular anime": {
            "sort_by": "popularity.desc",
            "with_genres": 16,
            "with_keywords": 210024,
            "without_keywords": "10103,161155",
            "with_original_language": "ja",
        },
        "family friendly": {
            "sort_by": "popularity.desc",
            "with_original_language": "en",
            "with_genres": 10751,
            "without_genres": "27,53,99,18",
        },
        "action and adventure": {
            "sort_by": "popularity.desc",
            "vote_count.gte": 50,
            "with_genres": 10759,
            "without_keywords": "10103,161155",
            "with_original_language": "en|ja",
        },
        "drama": {
            "sort_by": "popularity.desc",
            "vote_count.gte": 50,
            "with_genres": 18,
            "without_keywords": "10103,161155",
            "with_original_language": "en|ja",
        },
        "mystery": {
            "sort_by": "popularity.desc",
            "vote_count.gte": 50,
            "with_genres": 9648,
            "without_keywords": "10103,161155",
            "with_original_language": "en|ja",
        },
        "comedy": {
            "sort_by": "popularity.desc",
            "vote_count.gte": 50,
            "with_genres": 35,
            "without_keywords": "10103,161155",
            "with_original_language": "en|ja",
        },
        "documentary": {
            "sort_by": "popularity.desc",
            "vote_count.gte": 50,
            "with_genres": 99,
            "without_keywords": "10103,161155",
            "with_original_language": "en|ja",
        },
    }

    preset_filters = preprocess_filters(preset_filters, slug)

    if filter_name:
        return preset_filters[filter_name]
    return preset_filters


def tv_filters(filter_name=None, slug=False):
    """Predefined categories shown for the TV filter modal."""
    today = datetime.today()
    preset_filters = {
        "currently ongoing": {
            "sort_by": "popularity.desc",
            "air_date.gte": (today - timedelta(days=7)).strftime(r"%Y-%m-%d"),
            "air_date.lte": today.strftime(r"%Y-%m-%d"),
            "without_genres": 10763,
            "without_keywords": "10103,161155",
            "with_original_language": "en|ja",
        },
        "airing today": {
            "sort_by": "popularity.desc",
            "air_date.gte": today.strftime(r"%Y-%m-%d"),
            "air_date.lte": today.strftime(r"%Y-%m-%d"),
            "without_genres": 10763,
            "without_keywords": "10103,161155",
            "with_original_language": "en|ja",
        },
        **combined_filters(),
    }

    preset_filters = preprocess_filters(preset_filters, slug)

    if filter_name:
        return preset_filters[filter_name]
    return preset_filters


def movie_filters(filter_name=None, slug=False):
    """Predefined categories shown in the movie filter modal."""
    today = datetime.today()
    preset_filters = {
        "in theaters": {
            "sort_by": "popularity.desc",
            "with_release_type": "2|3",
            "primary_release_date.gte": (today - timedelta(days=150)).strftime(
                r"%Y-%m-%d"
            ),
            "without_keywords": "10103,161155",
            "with_original_language": "en|ja",
        },
        **combined_filters(),
    }

    preset_filters = preprocess_filters(preset_filters, slug)

    if filter_name:
        return preset_filters[filter_name]
    return preset_filters
