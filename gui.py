import tkinter as tk
from tkinter import ttk
import time
import threading
import webbrowser  # Voor het openen van de website

# Maak het hoofdvenster
root = tk.Tk()
root.title("Antivirus Programma")

# Maak het venster kleiner en center het op het scherm
window_width = 400
window_height = 300

# Bereken de positie van het venster om het te centreren
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)

root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
root.configure(bg="#2C3E50")  # Hoofdkleur instellen

# Stijl instellen
style = ttk.Style()
style.configure("Rounded.TButton", font=("Arial", 12), padding=10, borderwidth=0, relief="flat")
style.map("Rounded.TButton", foreground=[("active", "black")])

def create_rounded_button(parent, text, command=None):
    return tk.Button(parent, text=text, font=("Arial", 12), bg="white", fg="black",
                     relief="flat", bd=0, padx=20, pady=10, cursor="hand2",
                     highlightthickness=2, highlightbackground="#BDC3C7", highlightcolor="#AAB7B8",
                     command=command)

# Functie om een nieuw venster te openen voor de scan
def open_scan_window():
    scan_button.config(state=tk.DISABLED)  # De knop uitschakelen tijdens de scan

    # Nieuw venster maken met dezelfde achtergrondkleur
    scan_window = tk.Toplevel(root)
    scan_window.title("Scan in uitvoering...")
    scan_window.configure(bg="#2C3E50")  # Zelfde kleur als hoofdvenster

    # Nep-terminal weergave (zwart achtergrond met groene tekst)
    log_text = tk.Text(scan_window, height=10, width=60, bg="black", fg="green", font=("Courier", 10))
    log_text.pack(pady=10)

    # Voortgangsbalk
    progress_bar = ttk.Progressbar(scan_window, orient="horizontal", length=400, mode="determinate")
    progress_bar.pack(pady=10)

    # Functie voor de scan simuleren
    def fake_scan():
        log_messages = [
            "Scan gestart...",
            "System32 wordt gecontroleerd...",
            "Verdachte bestanden worden geanalyseerd...",
            "C:\\Gebruikers\\Documenten wordt gescand...",
            "Malware niet gedetecteerd!",
            "Scan voltooid!"
        ]

        for i, msg in enumerate(log_messages):
            time.sleep(1.5)
            log_text.insert(tk.END, msg + "\n")
            log_text.see(tk.END)
            progress_bar["value"] += 100 / len(log_messages)
            scan_window.update_idletasks()

        scan_button.config(state=tk.NORMAL)  # De knop weer inschakelen

        # Voeg de Done en Lees Meer knoppen toe
        button_frame = tk.Frame(scan_window, bg="#2C3E50")  # Frame voor de knoppen
        button_frame.pack(pady=10)

        done_button = create_rounded_button(button_frame, "Done", command=scan_window.destroy)
        done_button.pack(side="left", padx=10)  # Plaats naast elkaar (side="left")

        # Functie om de website te openen
        def open_website():
            webbrowser.open("https://www.example.com")  # Pas de URL aan naar de gewenste website

        lees_meer_button = create_rounded_button(button_frame, "Lees Meer", command=open_website)
        lees_meer_button.pack(side="left", padx=10)  # Plaats naast elkaar (side="left")

        # Pas de grootte van het venster aan de inhoud aan
        scan_window.update_idletasks()  # Zorg ervoor dat de inhoud volledig is geladen
        scan_window.geometry(f"{scan_window.winfo_width()}x{scan_window.winfo_height()}")

    threading.Thread(target=fake_scan, daemon=True).start()

# Functie om de website te openen in het hoofdvenster
def open_main_website():
    webbrowser.open("https://www.example.com")  # Pas de URL aan naar de gewenste website

# Voeg een label toe
label = tk.Label(root, text="Welkom bij je Antivirus Programma!", font=("Arial", 16, "bold"), fg="white", bg="#2C3E50")
label.pack(pady=10)

# Voeg een knop toe voor de scanfunctie
scan_button = create_rounded_button(root, "Voer Scan Uit", command=open_scan_window)
scan_button.pack(pady=10)

# Voeg de derde Lees Meer knop toe in het hoofdvenster
lees_meer_button_main = create_rounded_button(root, "Lees Meer", command=open_main_website)
lees_meer_button_main.pack(pady=10)

# Voeg een knop toe om het programma te verlaten
exit_button = create_rounded_button(root, "Afsluiten", command=root.quit)
exit_button.pack(pady=10)

# Start de GUI
root.mainloop()
