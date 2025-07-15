import random
import tkinter as tk
from tkinter import font

# ----------- DATEN -----------

Characters = [
    "Dwight Fairfield", "Meg Thomas", "Claudette Morel", "Jake Park", "Nea Karlsson",
    "Laurie Strode", "Ace Visconti", "William 'Bill' Overbeck", "Feng Min", "David King",
    "Quentin Smith", "David Tapp", "Kate Denson", "Adam Francis", "Jeff Johansen",
    "Jane Romero", "Ash Williams", "Nancy Wheeler", "Steve Harrington", "Yui Kimura",
    "Zarina Kassir", "Cheryl Mason", "Felix Richter", "Élodie Rakoto", "Yun-Jin Lee",
    "Jill Valentine", "Leon S. Kennedy", "Mikaela Reid", "Jonah Vasquez", "Haddie Kaur",
    "Vittorio Toscano", "Thalita Lyra", "Renato Lyra", "Gabriel Soma", "Nicolas Cage",
    "Ellen Ripley", "Alan Wake", "Sable Ward"
]

Items = ["Toolbox", "Med-Kit", "Flashlight", "Map", "Key", "Firecracker", "Coin"]
YesNo = ["Yes", "No"]

Perks = [
    "Adrenaline", "Aftercare", "Alert", "Ace in the Hole", "Any Means Necessary", "Appraisal",
    "Autodidact", "Autonomous Ally", "Baby-Sitter", "Bardic Inspiration", "Buckle Up",
    "Boon: Circle of Healing", "Boon: Exponential", "Boon: Illuminating", "Boon: Leading",
    "Boon: Shadow Step", "Bond", "Blood Pact", "Blood Rush", "Blink", "Bitter Murmur",
    "Blind Faith", "Deliverance", "Déjà Vu", "Detectives Hunch", "Diversion", "Dark Sense",
    "Deadline", "Decisive Strike", "Deep Faith", "Overcome", "Exultation", "Fast Track",
    "Finesse", "Fixated", "Flashbang", "Fogwise", "For the People", "Friendly Competition",
    "Heads Up", "Head On", "Healing Vigil", "Hope", "Hyperfocus", "Inner Strength",
    "Kindred", "Leader", "Left Behind", "Level Headed", "Lightning Strikes", "Lightweight",
    "Low Profile", "Lucky Break", "Lucky Star", "Lithe", "Made for This", "Made to Last",
    "Mettle of Man", "Mirrored Illusion", "Moment of Glory", "No Mither", "No One Left Behind",
    "Object of Obsession", "Open-Handed", "Pharmacy", "Plunderer's Instinct", "Poised",
    "Plot Twist", "Power Struggle", "Premonition", "Prove Thyself", "Quick & Quiet",
    "Quick Gambit", "Reassurance", "Reactive Healing", "Resilience", "Residual Manifest",
    "Self-Care", "Slippery Meat", "Small Game", "Solidarity", "Spine Chill", "Sprint Burst",
    "Streetwise", "Surge", "Teamwork: Collective Stealth", "Teamwork: Power of Two",
    "Tenacity", "This Is Not Happening", "Up the Ante", "Vigil", "We're Gonna Live Forever",
    "Wiretap", "Windows of Opportunity", "Witching Hour", "Wound Treats", "Wrong Direction"
]

# ----------- FUNKTIONEN -----------

def round_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [
        x1+radius, y1,
        x2-radius, y1,
        x2, y1,
        x2, y1+radius,
        x2, y2-radius,
        x2, y2,
        x2-radius, y2,
        x1+radius, y2,
        x1, y2,
        x1, y2-radius,
        x1, y1+radius,
        x1, y1,
    ]
    return canvas.create_polygon(points, smooth=True, **kwargs)

# ----------- HAUPT-APP -----------

class DBDRandomizer(tk.Tk):
    def __init__(self):
        super().__init__()

        # --- Fenster Setup ---
        self.title("Dead by Daylight Randomizer")
        self.geometry("900x400")
        self.resizable(False, False)

        # --- Fonts ---
        self.title_font = font.Font(family="Helvetica", size=16, weight="bold")
        self.text_font = font.Font(family="Helvetica", size=12)

        # --- Darkmode Flag ---
        self.dark_mode = False

        # --- Canvas für Hintergrund ---
        self.canvas = tk.Canvas(self, bg="#f0f0f5", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True, padx=20, pady=20)

        # Hintergrundkarte mit abgerundeten Ecken
        self.bg_card = round_rectangle(self.canvas, 20, 20, 880, 380, radius=25, fill="white", outline="")

        # Frame für Inhalt
        self.frame = tk.Frame(self.canvas, bg="white")
        self.frame.place(x=40, y=40, width=840, height=320)

        # --- Variablen für dynamische Inhalte ---
        self.character_var = tk.StringVar()
        self.items_var = tk.StringVar()
        self.item_choice_var = tk.StringVar()
        self.perks_var = tk.StringVar()
        self.backup_var = tk.StringVar()

        # --- Layout aufbauen ---
        self.build_layout()

        # --- Erstes Würfeln ---
        self.roll()

    def build_layout(self):
        # Character
        char_frame = tk.Frame(self.frame, bg="white")
        char_frame.grid(row=0, column=0, sticky="nw", padx=10, pady=10)
        tk.Label(char_frame, text="Character:", font=self.title_font, bg="white").pack(anchor="w")
        tk.Label(char_frame, textvariable=self.character_var, font=self.text_font, bg="white").pack(anchor="w")

        # Items
        item_frame = tk.Frame(self.frame, bg="white")
        item_frame.grid(row=0, column=1, sticky="nw", padx=10, pady=10)
        tk.Label(item_frame, text="Items:", font=self.title_font, bg="white").pack(anchor="w")
        tk.Label(item_frame, textvariable=self.items_var, font=self.text_font, bg="white").pack(anchor="w")
        tk.Label(item_frame, textvariable=self.item_choice_var, font=self.text_font, bg="white").pack(anchor="w", pady=(5,0))

        # Perks
        perk_frame = tk.Frame(self.frame, bg="white")
        perk_frame.grid(row=0, column=2, sticky="nw", padx=10, pady=10)
        tk.Label(perk_frame, text="Perks:", font=self.title_font, bg="white").pack(anchor="w")
        tk.Label(perk_frame, textvariable=self.perks_var, font=self.text_font, bg="white", justify="left").pack(anchor="w")

        # Backup Perks
        backup_frame = tk.Frame(self.frame, bg="white")
        backup_frame.grid(row=0, column=3, sticky="nw", padx=10, pady=10)
        tk.Label(backup_frame, text="Backup Perks:", font=self.title_font, bg="white").pack(anchor="w")
        tk.Label(backup_frame, textvariable=self.backup_var, font=self.text_font, bg="white", justify="left").pack(anchor="w")

        # Random Button
        self.roll_button = tk.Button(self.frame, text="Random", font=self.title_font, bg="#007aff", fg="white",
                                     activebackground="#0051a8", activeforeground="white", bd=0, padx=20, pady=10,
                                     command=self.roll)
        self.roll_button.grid(row=1, column=0, columnspan=4, pady=20, sticky="ew")

        # Dark Mode Toggle Button
        self.dark_mode_button = tk.Button(self.frame, text="Toggle Dark Mode", font=self.title_font,
                                          bg="#444", fg="white", bd=0, padx=15, pady=7,
                                          command=self.toggle_dark_mode)
        self.dark_mode_button.grid(row=2, column=0, columnspan=4, pady=5, sticky="ew")

        self.frame.grid_columnconfigure((0,1,2,3), weight=1)
        self.frame.grid_rowconfigure(0, weight=1)

    def roll(self):
        # --- Charakter wählen ---
        character = random.choice(Characters)
        self.character_var.set(character)

        # --- Item Ja/Nein ---
        has_item = random.choice(YesNo)
        self.items_var.set(has_item)

        if has_item == "Yes":
            random_item = random.choice(Items)
            self.item_choice_var.set(random_item)
        else:
            self.item_choice_var.set("None")

        # --- Perks wählen ---
        n = min(4, len(Perks))
        perks_selected = random.sample(Perks, n)
        self.perks_var.set("\n".join(perks_selected))

        backup_selected = random.sample(Perks, n)
        self.backup_var.set("\n".join(backup_selected))

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode

        if self.dark_mode:
            # Dark mode Farben
            bg = "#121212"
            fg = "#eeeeee"
            card_bg = "#1e1e1e"
            button_bg = "#0a84ff"
            button_fg = "white"
            button_active_bg = "#0060df"
        else:
            # Light mode Farben (Standard)
            bg = "#f0f0f5"
            fg = "black"
            card_bg = "white"
            button_bg = "#007aff"
            button_fg = "white"
            button_active_bg = "#0051a8"

        # Fenster Hintergrund
        self.configure(bg=bg)
        self.canvas.configure(bg=bg)
        self.canvas.itemconfig(self.bg_card, fill=card_bg)

        # Frame Hintergrund
        self.frame.configure(bg=card_bg)

        # Alle Kinder-Widgets aktualisieren
        for widget in self.frame.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.configure(bg=card_bg)
                for child in widget.winfo_children():
                    if isinstance(child, tk.Label):
                        child.configure(bg=card_bg, fg=fg)
                    if isinstance(child, tk.Button):
                        child.configure(bg=button_bg, fg=button_fg,
                                        activebackground=button_active_bg, activeforeground=button_fg)
            elif isinstance(widget, tk.Button):
                widget.configure(bg=button_bg, fg=button_fg,
                                 activebackground=button_active_bg, activeforeground=button_fg)

        # Labels direkt im frame (Character, Items etc)
        for var_name in [self.character_var, self.items_var, self.item_choice_var, self.perks_var, self.backup_var]:
            # Keine direkte Farbeinstellung möglich für StringVar, wird über Label gesteuert
            pass

if __name__ == "__main__":
    app = DBDRandomizer()
    app.mainloop()
