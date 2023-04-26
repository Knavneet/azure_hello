import tkinter as tk
import pyttsx3
import tkinter as tk
from tkinter import ttk
import time

def mantra_meditation():
    # Create a new window for the mantra meditation feature
    mantra_window = tk.Toplevel(root)
    mantra_window.title("Mantra Meditation")
    mantra_window.geometry("400x300")

    # Add a label for the mantra meditation instructions
    instructions_label = tk.Label(mantra_window, text="Sit in a comfortable position and close your eyes. Repeat the mantra 'Om' silently to yourself, focusing on the sound and vibration. If your mind wanders, gently bring it back to the mantra. Continue for 10-20 minutes.")
    instructions_label.pack(pady=20)

    # Add a timer for the meditation session
    duration = 600  # 10 minutes in seconds
    timer_label = tk.Label(mantra_window, text=f"Remaining time: {duration//60}:{duration%60:02d}", font=("Helvetica", 18))
    timer_label.pack(pady=10)

    # Add a progress bar to show the user how much time has elapsed
    progress_bar = ttk.Progressbar(mantra_window, orient="horizontal", mode="determinate", length=300)
    progress_bar.pack(pady=10)

    # Set up text-to-speech engine
    engine = pyttsx3.init()

    # Define a function to speak the meditation instructions and start the timer
    def start_meditation():
        nonlocal duration
        engine.say("Welcome to mantra meditation. Please sit in a comfortable position and close your eyes.")
        engine.say("Repeat the mantra 'Om' silently to yourself, focusing on the sound and vibration.")
        engine.say("If your mind wanders, gently bring it back to the mantra.")
        engine.say("Continue for 10 to 20 minutes.")
        engine.runAndWait()

        count_down()

    # Define a function to count down the timer and update the progress bar
    def count_down():
        nonlocal duration
        elapsed_time = 600 - duration
        timer_label.config(text=f"Remaining time: {duration//60}:{duration%60:02d}")
        if duration > 0:
            duration -= 1
            progress_bar["value"] = (elapsed_time / 600) * 100
            progress_bar.update()
            mantra_window.after(1000, count_down)
        else:
            engine.say("Your meditation session is now complete.")
            engine.runAndWait()

    # Start the meditation session when the user clicks the "Start" button
    start_button = tk.Button(mantra_window, text="Start", command=start_meditation)
    start_button.pack(pady=10)

    # Add a button to close the window
    close_button = tk.Button(mantra_window, text="Close", command=mantra_window.destroy)
    close_button.pack(pady=10)



# Create the main window
root = tk.Tk()

# Set the window title and size
root.title("Indian Spirituality App")
root.geometry("800x600")

# Add a label for the app title
title_label = tk.Label(root, text="Indian Spirituality App", font=("Helvetica", 24))
title_label.pack(pady=50)

# Add buttons for each feature of the app
mantra_button = tk.Button(root, text="Mantra Meditation", command=mantra_meditation)
mantra_button.pack(pady=10)

yoga_button = tk.Button(root, text="Yoga")
yoga_button.pack(pady=10)

astrology_button = tk.Button(root, text="Astrology")
astrology_button.pack(pady=10)

bhakti_button = tk.Button(root, text="Bhakti Music")
bhakti_button.pack(pady=10)

puja_button = tk.Button(root, text="Puja")
puja_button.pack(pady=10)

ayurveda_button = tk.Button(root, text="Ayurveda")
ayurveda_button.pack(pady=10)

sacred_text_button = tk.Button(root, text="Sacred Texts")
sacred_text_button.pack(pady=10)

temple_button = tk.Button(root, text="Temple Locator")
temple_button.pack(pady=10)

meditation_button = tk.Button(root, text="Meditation Timer")
meditation_button.pack(pady=10)

community_button = tk.Button(root, text="Spiritual Community")
community_button.pack(pady=10)

# Start the main event loop
root.mainloop()
