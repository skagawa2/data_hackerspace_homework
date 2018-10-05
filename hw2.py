import requests
import re
import matplotlib.pyplot as plt
import numpy as np


def lyrics_word_count_easy(artist, song, phrase):
    r = requests.get("https://api.lyrics.ovh/v1/{artist}/{song}".format(artist=artist, song=song))
    if r.status_code != 200:
    	return -1
    lyrics = r.json()['lyrics']
    return len(re.findall(phrase, lyrics.lower()))

def lyrics_word_count(artist, phrase):
    pass

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
