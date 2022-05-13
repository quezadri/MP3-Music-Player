from tkinter import *
import tkinter as tk
from tkinter import filedialog
from pygame import mixer


class MP:
    def __init__(self, win):
        # Create Tkinter window
        win.geometry('200x200')
        win.title('Music Player')
        win.resizable(0, 0)

        # StringVar to change button text later
        self.play_restart = tk.StringVar()
        self.pause_resume = tk.StringVar()
        self.play_restart.set('Play')
        self.pause_resume.set('Pause')

        # Load Button & Position
        load_button = Button(win, text='Load', width=10, font=('Arial', 20), command=self.load)
        load_button.place(x=100, y=40, anchor='center')

        # Play Button & Position
        play_button = Button(win, textvariable=self.play_restart, width=10, font=('Arial', 20), command=self.play)
        play_button.place(x=100, y=80, anchor='center')

        # Pause Button & Position
        pause_button = Button(win, textvariable=self.pause_resume, width=10, font=('Arial', 20), command=self.pause)
        pause_button.place(x=100, y=120, anchor='center')

        # Stop Button & Position
        stop_button = Button(win, text='Stop', width=10, font=('Arial', 20), command=self.stop)
        stop_button.place(x=100, y=160, anchor='center')

        self.music_file = False
        self.playing_state = False

    # Opening MP3 File 
    # Make sure it is a real MP3 file
    def load(self):
        self.music_file = filedialog.askopenfilename()
        print("Loaded: ", self.music_file)
        self.play_restart.set('Play')

    #Play music
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(str(self.music_file))
            mixer.music.play()
            self.playing_state = False
            self.play_restart.set('Restart')
            self.pause_resume.set('Pause')

    #Pause music
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
            self.pause_resume.set('Resume')
        else:
            mixer.music.unpause()
            self.playing_state = False
            self.pause_resume.set('Pause')

    #Stop music
    def stop(self):
        mixer.music.stop()


root = Tk()
MP(root)
root.mainloop()