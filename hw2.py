import requests
import re
import matplotlib.pyplot as plt
import numpy as np
from apikey import apikey

STATUS_GOOD = 200

def lyrics_word_count_easy(artist, song, phrase):
    r = requests.get("https://api.lyrics.ovh/v1/{artist}/{song}".format(artist=artist, song=song))
    if r.status_code != STATUS_GOOD:
    	return -1
    lyrics = r.json()['lyrics']
    return len(re.findall(phrase, lyrics.lower()))

def lyrics_word_count(artist, phrase):
	musixmatch_rooturl = "http://api.musixmatch.com/ws/1.1/"
	
	r = requests.get(musixmatch_rooturl + "artist.search?q_artist={}&apikey={}".format(artist, apikey['Musixmatch']))
	if r.status_code != STATUS_GOOD: return -1
	artist_id = r.json()['message']['body']['artist_list'][0]['artist']['artist_id']

	r2 = requests.get(musixmatch_rooturl + "artist.albums.get?artist_id={}&apikey={}".format(artist_id, apikey['Musixmatch']))
	if r2.status_code != STATUS_GOOD: return -1
	albums = [album['album']['album_id'] for album in r2.json()['message']['body']['album_list']]

	track_titles = []
	for album_id in albums:
		r3 = requests.get(musixmatch_rooturl + "album.tracks.get?album_id={}&apikey={}".format(album_id, apikey['Musixmatch']))
		if r3.status_code == STATUS_GOOD:
			for track in r3.json()['message']['body']['track_list']:
				track_titles.append(track['track']['track_name'])

	total_count = 0
	for track in track_titles:
		r4 = requests.get("https://api.lyrics.ovh/v1/{artist}/{song}".format(artist=artist, song=track))
		if r.status_code == STATUS_GOOD:
			lyrics = r4.json()['lyrics']
			total_count += len(re.findall(phrase, lyrics.lower()))
	return total_count

def visualize():
    x = np.array([ 0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10., 11., 12., 13., 14., 15., 16., 17., 18., 19., 20., 21., 22., 23., 24., 25., 26., 27., 28., 29.])
    y = np.array([ 0., 25., 27., 4., -22., -28., -8., 19., 29., 12., -16., -29., -16., 12., 29., 19., -8., -28., -22., 4., 27., 25., -0., -25., -27., -3., 22., 28., 8., -19.])
    plt.subplot(2, 1, 1)
    plt.plot(x, y, '-')
    plt.title('LineGraph')

    plt.subplot(2, 2, 3)
    plt.hist([x, y])
    plt.title('Histogram')

    plt.subplot(2, 2, 4)
    plt.scatter(x, y)
    plt.title('Scatter')

    return plt.show()
