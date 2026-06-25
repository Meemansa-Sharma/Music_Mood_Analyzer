
class Artist:
    def __init__(self,artist_name):
        self.aname=artist_name

class Song:
    def __init__(self,song_name,genre,mood,energy,popularity):
        self.sname=song_name
        self.genre=genre
        self.mood=mood
        self.energy=energy
        self.popularity=popularity

class Api_manager():
    def validate_artist(self,aname):
        pass
    def validate_song(self,sname):
        pass
    def return_info(self,aname,sname):
        pass
        
