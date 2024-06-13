from abc import ABC, abstractmethod

class MusicPlayer(ABC):
    def __init__(self):
        pass 

    @abstractmethod
    def play_song(self):
        pass
    
    def next_song(self):
        pass
    
    @abstractmethod
    def pause_song(self):
        pass

    
    def upload_song(self):
        pass

    
    def remove_song(self):
        pass

    @abstractmethod
    def update_song_listbox(self):
        pass

    @abstractmethod
    def update_song_label(self):
        pass

    @abstractmethod
    def volume(self, x):
        pass

    
 