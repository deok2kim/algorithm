def solution(m, musicinfos):
    m = m.replace('A#', 'H').replace('C#', 'I').replace('D#', 'J').replace('F#', 'K').replace('G#', 'L')
    # print(m)
    music_dict = {}
    for info in musicinfos:
        info = info.split(',')
        start, end, title, lyrics = info[0], info[1], info[2], info[3]

        h1, m1 = start.split(':')
        h2, m2 = end.split(':')
        time = (int(h2) - int(h1)) * 60 + (int(m2) - int(m1))
        lyrics = lyrics.replace('A#', 'H').replace('C#', 'I').replace('D#', 'J').replace('F#', 'K').replace('G#', 'L')
        song = lyrics * (time // len(lyrics)) + lyrics[:time % len(lyrics)]
        music_dict[song] = title


    result = None
    for song in music_dict.keys():
        if m in song:
            if result == None:
                result = song
            else:
                if len(result) < len(song):
                    result = song
    if result != None:
        return music_dict[result]
    else:
        return "(None)"