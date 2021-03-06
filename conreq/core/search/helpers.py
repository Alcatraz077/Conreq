"""Helpers for Search"""
from conreq.core.tmdb.discovery import TmdbDiscovery


def convert_card_to_tmdb(index, all_results):
    """Attempt to convert Sonarr/Radarr cards to TMDB equivalents."""
    content_discovery = TmdbDiscovery()
    # NOTE: For some reason, overriding values in all_results requires the list and index value.
    # It will NOT work if attempting to change values by reference (ex. card = newCard).

    # Convert Sonarr cards to TMDB
    if all_results[index].__contains__("tvdbId"):
        try:
            tmdb_query = content_discovery.get_by_tvdb_id(all_results[index]["tvdbId"])
            tmdb_result = tmdb_query["tv_results"][0]
            all_results[index] = tmdb_result
        except:
            pass
