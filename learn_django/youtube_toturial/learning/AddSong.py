from music.models import Album,Song
album1 = Album.objects.get(pk=1)
album1.artist
song = Song()
song.album = album1
song.file_type = "mp3"
song.song_title = "I hate my boyfirend"
song.save()
%his -f AddSong.py
%hist -f AddSong.py
