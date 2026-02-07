import tkinter as tk
from tkinter import ttk
import random
import webbrowser

# Songs database
songs = {
    "Happy": {
        "Hindi": ["Ude Dil Befikre", "Kar Gayi Chull"],
        "English": ["Happy - Pharrell Williams", "Can't Stop The Feeling"],
        "Marathi": ["Zingaat"],
        "Tamil": ["Vaathi Coming"]
    },
    "Sad": {
        "Hindi": ["Agar Tum Saath Ho", "Channa Mereya"],
        "English": ["Someone Like You - Adele", "Let Her Go"],
        "Marathi": ["Jeev Rangla"],
        "Tamil": ["Why This Kolaveri Di"]
    },
    "Romantic": {
        "Hindi": ["Pee Loon", "Tum Mile"],
        "English": ["Perfect - Ed Sheeran", "All of Me - John Legend"],
        "Marathi": ["Sairat Zaala Ji"],
        "Tamil": ["Munbe Vaa"]
    },
    "Energetic": {
        "Hindi": ["Malhari", "Zinda"],
        "English": ["Believer - Imagine Dragons", "Thunder - Imagine Dragons"],
        "Marathi": ["Morya Morya"],
        "Tamil": ["Aaluma Doluma"]
    },
    "Angry": {
        "Hindi": ["Zinda - Bhaag Milkha Bhaag"],
        "English": ["Numb - Linkin Park", "In the End - Linkin Park"],
        "Marathi": ["Sindhu Durga"],
        "Tamil": ["Surviva"]
    }
}

def play_song():
    mood = mood_var.get()
    language = language_var.get()

    if mood in songs and language in songs[mood]:
        song = random.choice(songs[mood][language])
        song_label.config(text=f"Playing: {song}")

        emojis = {
            "Happy": "😊",
            "Sad": "😢",
            "Romantic": "😍",
            "Energetic": "🚀",
            "Angry": "😡"
        }

        emoji_label.config(text=emojis.get(mood, ""))

        query = song.replace(" ", "+")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
    else:
        song_label.config(text="Please select mood and language.")

# Main App
app = tk.Tk()
app.title("Mood-Based Music Player")
app.geometry("700x600")

# Pink background using code
app.configure(bg="#ffc0cb")   # Light pink

# UI
tk.Label(app, text="How are you feeling today?", font=("Helvetica", 16, "bold"), bg="#ffc0cb").pack(pady=20)

mood_var = tk.StringVar()
mood_dropdown = ttk.Combobox(app, textvariable=mood_var, values=list(songs.keys()), font=("Helvetica", 12))
mood_dropdown.pack(pady=10)

tk.Label(app, text="Select your preferred song language:", font=("Helvetica", 14), bg="#ffc0cb").pack(pady=10)

language_var = tk.StringVar()
language_dropdown = ttk.Combobox(app, textvariable=language_var,
                                 values=["Hindi", "English", "Marathi", "Tamil"],
                                 font=("Helvetica", 12))
language_dropdown.pack(pady=10)

emoji_label = tk.Label(app, text="", font=("Helvetica", 40), bg="#ffc0cb")
emoji_label.pack(pady=10)

song_label = tk.Label(app, text="", font=("Helvetica", 14, "bold"),
                      wraplength=600, bg="#ffc0cb")
song_label.pack(pady=10)

play_btn = tk.Button(app, text="Play Song on YouTube",
                     command=play_song,
                     font=("Helvetica", 12, "bold"),
                     bg="white")
play_btn.pack(pady=20)

app.mainloop()
