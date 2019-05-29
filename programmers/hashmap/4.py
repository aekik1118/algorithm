from collections import defaultdict

def solution(genres, plays):
    answer = []
    play_count_genre = defaultdict(int)
    songs_genre = defaultdict(list)

    for index, tmp in enumerate(zip(genres,plays)):
        genre, play_count = tmp[0], tmp[1]
        play_count_genre[genre] += play_count
        songs_genre[genre].append((-play_count,index))

    genres_sorted = sorted(play_count_genre.items(), key=lambda x:x[1], reverse=True)

    for g,_ in genres_sorted:
        answer.extend([index for _,index in sorted(songs_genre[g])[:2]])

    return answer

g = ["classic", "pop", "classic", "classic", "pop"]
p = [500, 600, 150, 800, 2500]
print(solution(g,p))