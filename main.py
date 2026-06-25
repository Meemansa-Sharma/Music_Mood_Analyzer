from classes import Artist, Song, Api_manager
import json
import csv

def user_input(api):
    artname=input("Enter the artist's name: ")
    print(f"Finding {artname} ..... ")
    va=api.validate_artist(artname)
    if (va==False) :
            print(f"Sorry! Artist {artname} Not Found.")
    else:
            print("Found! Fetching albums and singles...")
            artist=Artist(artname)

    sgname= input("Enter your favourite song: ")
    vs=api.validate_song(sgname)
    if (vs==False and not va):
            print(f"Sorry! Song {sgname} Not Found.")
    else:
            print("Found!")

    song=Song(sgname)
    
def display_info():
    pass
def playlist_name():
       pass
def analyse_mood():
       pass
def generate_report():
       pass
def generate_listening_persona():
       pass
def save_preferences():
       pass
def main():
        api=Api_manager()
        user_input(api)


if __name__=="__main__":
    main()