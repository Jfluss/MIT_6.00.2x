# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 12:03:57 2017

@author: Josh
"""

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    
    playlist = []
    memory = 0
    songs_copy = sorted(songs[1:], key = lambda x: x[2])
    if songs[0][2] > max_size:
        return playlist
    else:
        playlist.append(songs[0][0])
        memory += songs[0][2]
    for i in songs_copy:
        if (memory + i[2]) < max_size:
            playlist.append(i[0])
            memory += i[2]
        else:
            pass
    return playlist