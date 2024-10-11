import tkinter as tk
from tkinter import filedialog
from ffpyplayer.player import MediaPlayer
import pygame

class MediaPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Audio and Video Player")
        self.root.geometry("500x400")

        pygame.mixer.init()


        self.open_audio_button = tk.Button(root, text="Open Audio", command=self.open_audio)
        self.open_audio_button.pack(pady=10)

        self.play_audio_button = tk.Button(root, text="Play Audio", command=self.play_audio, state=tk.DISABLED)
        self.play_audio_button.pack(pady=10)

        self.stop_audio_button = tk.Button(root, text="Stop Audio", command=self.stop_audio, state=tk.DISABLED)
        self.stop_audio_button.pack(pady=10)

        self.open_video_button = tk.Button(root, text="Open Video", command=self.open_video)
        self.open_video_button.pack(pady=10)

        self.play_video_button = tk.Button(root, text="Play Video", command=self.play_video, state=tk.DISABLED)
        self.play_video_button.pack(pady=10)

        self.video_label = tk.Label(root)
        self.video_label.pack(pady=10)

 
        self.audio_file = None
        self.video_file = None
        self.video_player = None

    def open_audio(self):
        self.audio_file = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
        if self.audio_file:
            self.play_audio_button.config(state=tk.NORMAL)
            self.stop_audio_button.config(state=tk.NORMAL)

    def play_audio(self):
        if self.audio_file:
            pygame.mixer.music.load(self.audio_file)
            pygame.mixer.music.play()

    def stop_audio(self):
        pygame.mixer.music.stop()

    def open_video(self):
        self.video_file = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.avi")])
        if self.video_file:
            self.play_video_button.config(state=tk.NORMAL)

    def play_video(self):
        if self.video_file:
            self.video_player = MediaPlayer(self.video_file)
            self.update_video_frame()

    def update_video_frame(self):
        if self.video_player:
            frame, val = self.video_player.get_frame()
            if val != 'eof' and frame is not None:
                img, t = frame
                img = img.to_image()
                img_tk = tk.PhotoImage(img)
                self.video_label.config(image=img_tk)
                self.video_label.image = img_tk
            self.root.after(20, self.update_video_frame)


if __name__ == "__main__":
    root = tk.Tk()
    app = MediaPlayerApp(root)
    root.mainloop()