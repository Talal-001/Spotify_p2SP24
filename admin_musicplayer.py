import tkinter as tk
from tkinter import ttk, ACTIVE, END
import pygame
import os
from playlist import Playlist
from music_player import MusicPlayer
from login_window import LoginWindow

pygame.init()
pygame.mixer.init()

class AdminmusicPlayer(MusicPlayer):
    def __init__(self, root):
        self.root = root
        self.root.title("Spotify-like Music Player")
        self.root.geometry("800x500")
        self.root.configure(bg="teal")

        self.playlist = Playlist()
        self.current_song_index = 0

        self.song_listbox = tk.Listbox(self.root,bg="black",fg="white",selectbackground="gray",selectforeground="green", selectmode=tk.SINGLE, width=90, height=22, font=("KOEEYA", 12))
        self.song_listbox.pack(pady=20, padx=20)
        self.update_song_listbox()

        self.remove_button = ttk.Button(self.root, text="Remove Song ⛔", command=self.remove_song, style="TButton")
        self.remove_button.pack(side=tk.LEFT, padx=10)

        self.play_button = ttk.Button(self.root, text=" Play song ▶️ ", command=self.play_song, style="TButton")
        self.play_button.pack(side=tk.LEFT, padx=10)

        self.prev_button = ttk.Button(self.root, text=" Prev song ◀| ", command=self.prev_song, style="TButton")
        self.prev_button.pack(side=tk.LEFT, padx=10)

        self.next_button = ttk.Button(self.root, text=" Next song ▶| ", command=self.next_song, style="TButton")
        self.next_button.pack(side=tk.LEFT, padx=10)

        self.pause_button = ttk.Button(self.root, text= "pause song ⏸️", command=self.pause_song, style="TButton")
        self.pause_button.pack(side=tk.LEFT, padx=10)

        self.upload_button = ttk.Button(self.root, text="Upload Song 🎵", command=self.upload_song, style="TButton")
        self.upload_button.pack(side=tk.LEFT, padx=10)

        self.volume_slider = ttk.Scale(self.root, from_=0.0, to=1.0, orient=tk.HORIZONTAL, length=200, command=self.volume)
        self.volume_slider.set(0.5)
        self.volume_slider.pack(padx=10, side=tk.LEFT)

        self.exit_button = ttk.Button(self.root, text="exit", command=self.exit, style="TButton")
        self.exit_button.pack(side=tk.LEFT, padx=10)

        pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)
        self.root.after(100, self.check_for_song_end)

    def check_for_song_end(self):
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT + 1:
                self.next_song()
        self.root.after(100, self.check_for_song_end)

    def play_song(self):
        if self.playlist.songs:
            selected_song = self.song_listbox.get(ACTIVE)
            all_songs = self.song_listbox.get(0, END)
            self.current_song_index = all_songs.index(selected_song)

            song_file_path = self.playlist.songs[self.current_song_index].file_path
            pygame.mixer.music.load(song_file_path)
            pygame.mixer.music.play()
            pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)
            self.update_song_label()

    def next_song(self):
        if self.playlist.songs:
            self.current_song_index = (self.current_song_index + 1) % len(self.playlist.songs)
            self.song_listbox.selection_clear(0, END)
            self.song_listbox.selection_set(self.current_song_index)
            self.song_listbox.activate(self.current_song_index)
            self.song_listbox.see(self.current_song_index)
            self.play_song()

    def prev_song(self):
        if self.playlist.songs:
            self.current_song_index = (self.current_song_index - 1) % len(self.playlist.songs)
            self.song_listbox.selection_clear(0, END)
            self.song_listbox.selection_set(self.current_song_index)
            self.song_listbox.activate(self.current_song_index)
            self.song_listbox.see(self.current_song_index)
            self.play_song()
    def pause_song(self):
        pygame.mixer.music.pause()

    def volume(self, x):
        pygame.mixer.music.set_volume(self.volume_slider.get())

    def upload_song(self):
        self.playlist.upload_song()
        self.update_song_listbox()

    def remove_song(self):
        selected_index = self.song_listbox.curselection()
        if selected_index:
            self.playlist.remove_song(selected_index[0])
            self.update_song_label()
            self.update_song_listbox()

    def update_song_listbox(self):
        self.song_listbox.delete(0, tk.END)
        for i, song in enumerate(self.playlist.songs):
            self.song_listbox.insert(tk.END, f"{i+1}. {song.title}")

    def update_song_label(self):
        if self.playlist.songs:
            current_song = os.path.basename(self.playlist.songs[self.current_song_index].file_path)
            self.song_listbox.selection_clear(0, tk.END)
            self.song_listbox.selection_set(self.current_song_index)
            self.song_listbox.see(self.current_song_index)

    def exit(self):
        self.root.destroy()
        pygame.mixer.music.stop()
        self.root = tk.Tk()
        LoginWindow(self.root)
        self.root.mainloop()
