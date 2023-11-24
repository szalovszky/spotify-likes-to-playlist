import spotipy
from spotipy.oauth2 import SpotifyOAuth
from math import ceil
import more_itertools as mit
import base64

SPOTIFY_PLAYLIST_LIMIT = 10000
SPOTIFY_API_TRACK_COUNT_LIMIT = 50
SPOTIFY_API_PLAYLIST_TRACK_COUNT_LIMIT = 100

playlist_image = None

scope = "user-library-read playlist-modify-private ugc-image-upload"

print('Authenticating...', end='\r')
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
user = sp.current_user()
print(f'Authenticated as {user["display_name"]} ({user["id"]})')

likes = []
liked_length = -1


def print_progress(message: str):
    percentage = 0
    if len(likes) != 0 and liked_length != 0 and liked_length != -1:
        percentage = len(likes) / liked_length
    print(f'[{round(percentage * 100)}%] {message}', end='\r')


def get_saved_tracks(page: int):
    results = sp.current_user_saved_tracks(
        limit=SPOTIFY_API_TRACK_COUNT_LIMIT, offset=page*SPOTIFY_API_TRACK_COUNT_LIMIT)
    global liked_length
    print_progress(
        f'Fetched page {page} out of {ceil(liked_length/SPOTIFY_API_TRACK_COUNT_LIMIT)}, we now have {len(likes)} tracks.')
    if liked_length == -1:
        liked_length = results['total']
    return results


def get_all_tracks():
    print('Fetching liked tracks...')
    page = 0
    while True:
        results = get_saved_tracks(page)
        tracks = results['items']
        global likes, liked_length
        likes.extend(tracks)
        page += 1
        if len(likes) >= liked_length:
            break


if __name__ == '__main__':
    try:
        with open("liked-songs-300.png", "rb") as image_file:
            playlist_image = base64.b64encode(image_file.read())
    except:
        print('Couldn\'t encode image. Continuing without image.')
    get_all_tracks()
    print(
        f'Fetching liked songs successfully finished. Found {len(likes)} tracks.')
    split_likes = list(mit.chunked(
        list(reversed(likes)), SPOTIFY_PLAYLIST_LIMIT))
    print(f'{len(split_likes)} playlists will be created.')
    print('Creating playlists...', end='\r')
    for i in range(len(split_likes)):
        playlist = sp.user_playlist_create(
            user['id'], f'Liked Songs #{i + 1} ({i * SPOTIFY_PLAYLIST_LIMIT} - {(i + 1) * SPOTIFY_PLAYLIST_LIMIT})', public=False)
        if playlist_image != None:
            try:
                sp.playlist_upload_cover_image(playlist['id'], playlist_image)
            except:
                print('Couldn\'t set playlist image. Continuing without image.')
        split_playlist = list(mit.chunked(
            list(reversed(split_likes[i])), SPOTIFY_API_PLAYLIST_TRACK_COUNT_LIMIT))
        for j in range(len(split_playlist)):
            sp.playlist_add_items(
                playlist['id'], [track['track']['id'] for track in split_playlist[j]])
            print(
                f'Created playlist {i+1} of {len(split_likes)} (chunk {j+1} of {len(split_playlist)})', end='\r')
    print(f'Finished creating {len(split_likes)} playlists. Exiting...')
