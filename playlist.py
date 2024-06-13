from song import Song

class Playlist:
    def __init__(self):
        self.songs = []
        self.filename = "playlist.txt"
        self.load_playlist()

    def add_song(self, song):
        self.songs.append(song)
        self.save_playlist()

    def remove_song(self, index):
        if 0 <= index < len(self.songs):
            del self.songs[index]
            self.save_playlist()

    def upload_song(self):
        from tkinter import filedialog
        import os
        file_path = filedialog.askopenfilename(title="Select Music File", filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            song_title = os.path.basename(file_path)
            new_song = Song(song_title, file_path)
            self.add_song(new_song)

    def save_playlist(self):
        with open(self.filename, 'w') as f:
            for song in self.songs:
                f.write(f"{song.title},{song.file_path}\n")

    def load_playlist(self):
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    title, file_path = line.strip().split(',')
                    self.songs.append(Song(title, file_path))
        except FileNotFoundError:
            pass