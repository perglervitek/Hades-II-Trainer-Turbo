import tkinter as tk
from tkinter import ttk
import threading
from trainer import EliteTrainer

class EliteGUI:
    def __init__(self):
        self.trainer = EliteTrainer()
        self.root = tk.Tk()
        self.root.title("Hades II Trainer Turbo 1.0.0")
        self.root.geometry("400x550")
        self.root.resizable(False, False)
        self.root.configure(bg="#1a1a2e")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", background="#1a1a2e", foreground="#e0e0e0", font=("Segoe UI", 10))
        style.configure("TButton", font=("Segoe UI", 9, "bold"))

        self.build_ui()

    def build_ui(self):
        header = tk.Label(self.root, text="HADES II TRAINER TURBO", bg="#1a1a2e", fg="#e54777",
                          font=("Segoe UI", 18, "bold"))
        header.pack(pady=10)

        status_frame = tk.Frame(self.root, bg="#16213e")
        status_frame.pack(fill=tk.X, padx=20, pady=5)
        self.status_label = tk.Label(status_frame, text="Status: Not attached", bg="#16213e", fg="#f5f5f5")
        self.status_label.pack(pady=5)

        btn_frame = tk.Frame(self.root, bg="#1a1a2e")
        btn_frame.pack(pady=10)

        self.attach_btn = tk.Button(btn_frame, text="Attach to Game", command=self.attach_game,
                                    bg="#0f3460", fg="white", width=20)
        self.attach_btn.pack(pady=5)

        separator = ttk.Separator(self.root, orient="horizontal")
        separator.pack(fill=tk.X, padx=20, pady=10)

        cheats_frame = tk.Frame(self.root, bg="#1a1a2e")
        cheats_frame.pack(pady=5)

        self.cheat_vars = {}
        cheats_list = [
            ("God Mode", "god_mode"),
            ("Unlimited Health", "unlimited_health"),
            ("Unlimited Mana", "unlimited_mana"),
            ("Max Gold", "max_gold"),
            ("All Resources", "all_resources"),
            ("One-Hit Kill", "one_hit_kill"),
            ("No Cooldowns", "no_cooldowns"),
            ("Speed Hack (2x)", "speed_hack"),
        ]

        for text, key in cheats_list:
            var = tk.BooleanVar()
            self.cheat_vars[key] = var
            cb = tk.Checkbutton(cheats_frame, text=text, variable=var, command=lambda k=key: self.toggle_cheat(k),
                                bg="#1a1a2e", fg="white", selectcolor="#1a1a2e", activebackground="#1a1a2e",
                                font=("Segoe UI", 10))
            cb.pack(anchor=tk.W, padx=30, pady=2)

        self.run_btn = tk.Button(self.root, text="Start Trainer Loop (F1)", command=self.start_loop,
                                 bg="#e54777", fg="white", width=20)
        self.run_btn.pack(pady=15)

        footer = tk.Label(self.root, text="Free cheat for Hades II v1.0.0", bg="#1a1a2e", fg="#aaaaaa")
        footer.pack(side=tk.BOTTOM, pady=10)

    def attach_game(self):
        try:
            self.trainer.attach()
            self.status_label.config(text="Status: Attached to Hades2.exe")
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}")

    def toggle_cheat(self, name):
        self.trainer.toggle_cheat(name)

    def start_loop(self):
        threading.Thread(target=self.trainer.run, daemon=True).start()
        self.status_label.config(text="Status: Trainer loop active")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = EliteGUI()
    app.run()
