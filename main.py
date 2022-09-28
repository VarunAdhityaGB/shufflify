import tkinter as tk
from tkinter import font
from tkinter.font import BOLD
import tkinter.ttk as ttk
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = ' playlist-modify-public playlist-read-private'
my_username = 'l6pii8uua3baeavix82fbffl7'
token = SpotifyOAuth(scope=scope, username=my_username)
spotify = spotipy.Spotify(auth_manager=token)

def create_playlist(name, desc):
    '''Give the Name of the playlist and a short description.'''
    spotify.user_playlist_create(user=my_username, public=True, description=desc, name=name)


def get_playlist():
    '''returns a list and a dictionary'''
    d_nory = {}
    ls = []
    data = spotify.current_user_playlists()
    for i in data['items']:
        d_nory[i['name']] = i['id']
    for i in d_nory:
        ls.append(i)
    return ls, d_nory

play_list, play_dict = get_playlist()


root = tk.Tk()
root.title("Shufflify")
root.config(bg='#1b345c')
root.geometry("800x150")
#root.overrideredirect(True)

'''def move_app(e):
    root.geometry(f"+{e.x_root}+{e.y_root}")

def close_app(e):
    root.quit()
    root.destroy()'''

def shuffle():
    def get_id(pl_nme):
        print(play_dict[pl_nme])

    p_name = playlist_menu.get()
    p_id = play_dict[p_name]
    song_d = (spotify.playlist_tracks(playlist_id=p_id))['items']


    for i in song_d:
        print(i['track']['uri'])


'''#custom title bar
tt_bar = tk.Frame(root, bg="#1b345c", relief='flat')  # flat groove raised ride solid sunken
tt_bar.pack(fill = 'x', expand=1,anchor=tk.N)

tt_bar.bind("<B1-Motion>", move_app)

tt_lbl = tk.Label(tt_bar, text="Shufflify", bg="#1b345c", fg="white", font=('', 14, BOLD))
tt_lbl.pack(side=tk.LEFT,pady=2)

close_lbl = tk.Label(tt_bar, text="  X  ", bg = "#1b345c", fg="white", relief="raised", bd = 0, font = ("",14))
close_lbl.pack(side=tk.RIGHT, pady=4) 
close_lbl.bind('<Button-1>', close_app)'''

main_frm = tk.Frame(root,bg='#1b345c') 
main_frm.pack(anchor=tk.CENTER)

playlist_menu = ttk.Combobox(main_frm, values=play_list, font=("", 14), background="#1b345c", width=50)
playlist_lbl = tk.Label(main_frm, text="Playlists", font=("", 15, BOLD), background="#1b345c")
playlist_lbl.grid(row=0, column=0, padx=10, pady=10)
playlist_menu.grid(row=0, column=1, padx=10, pady=10)

shf_btn = ttk.Button(main_frm, text = "Shuffle", command=shuffle)
shf_btn.grid(row=1, column=0, columnspan=2, pady=25)


 
root.mainloop()