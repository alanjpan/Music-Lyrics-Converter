# -*- coding: utf-8 -*-
"""
Created on Wed Feb 6 15:23:19 2019

@author: Alan Jerry Pan, CPA, CSC
@affiliation: Shanghai Jiaotong University

Program used to extract lyrics and convert them into data tables for automatic lyric generation.

Suggested citation as computer software for reference:
Pan, Alan J. (2019). Music Lyrics Converter [Computer software]. Github repository <https://github.com/alanjpan/Music-Lyrics-Converter>

Note this software's license is GNU GPLv3.
"""

import os
import random

filepath = "C:/Users/alanp/Desktop/transition.txt"
lyric_initial1 = []
lyric_final1 = []
lyricschain1 = {}

word = ""
with open(filepath) as file_object:
    for line in file_object.readlines():
        for letter in line:
            if word != "" and letter == " ":
                word += letter
            else:
                lyric_final1.append(word)
                break
        word = ""
        for letter in line:
            if letter != " ":
                word += letter
            else:
                lyric_initial1.append(word)
                break

        index = 1
        words = line.split()
        for word in words[index:]:
            key = words[index-1]
            if key in lyricschain1:
                lyricschain1[key].append(word)
            else:
                lyricschain1[key] = [word]
            index += 1
while "\n" in lyric_final1:
    lyric_final1.remove("\n")
while "" in lyric_final1:
    lyric_final1.remove("")

with open("C:/Users/alanp/Desktop/lyricsarray.txt", "w") as file:
    file.write(str(lyric_initial1))
    file.write("\n")
    file.write("\n")
    file.write(str(lyric_final1))
    file.write("\n")
    file.write("\n")
    file.write(str(lyricschain1))


def generate_lyrics(count):
    global message
    word1 = random.choice(lyric_initial1)
    message = ""
    message = word1.capitalize()

    word2 = ""
    while not (len(message.split(' ')) > count) or (word1 in lyric_final1):
        try:
            word2 = random.choice(lyricschain1[word1])
        except:
            word2 = random.choice(lyric_final1)

        word1 = word2
        message += ' ' + word2
    print(message)


