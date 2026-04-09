# 1) Given a list of songs and its runtime pair ,write  a function to return a pair of songs whose runtime sum up to exactly 7 min
# e.g Song_runtime_list = [("Hotel California", "3:40"),("Numb", "3:20"),( "Payphone" , "5:20"),( "Atlantis" , "7:20")] 
# Output  : ["Hotel California", "Numb"]

def find_song_pair(song_runtime_list):
    target = 7 * 60
    seen = {}

    for song, time_str in song_runtime_list:
        m, s = map(int, time_str.split(":"))
        total_sec = m * 60 + s
        remaining = target - total_sec

        if remaining in seen:
            return [seen[remaining], song]

        seen[total_sec] = song

    return []

print(find_song_pair(Song_runtime_list))

##############################################################################################################################################################
# 2)  Find the most occurrence element from the list and return a dict with that element as key and no. of occurrence as value
# input = ['a', 'b', 'c', 'd', 'c']
# output = {'c': 2}

input = ['a', 'b', 'c', 'd', 'c']
d = {}

for item in input:
    if item in d:
        d[item] += 1
    else:
        d[item] = 1
        
cnt = 0
elem = None

for key, value in d.items():
    if value > cnt:
        cnt = value
        elem = key

print({elem: cnt})
