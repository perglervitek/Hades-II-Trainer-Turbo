import time
import keyboard
from memory import EliteMemory
from offsets import Offsets

class EliteTrainer:
    def __init__(self):
        self.mem = EliteMemory()
        self.active = False
        self.cheats = {
            "god_mode": False,
            "unlimited_health": False,
            "unlimited_mana": False,
            "max_gold": False,
            "all_resources": False,
            "one_hit_kill": False,
            "no_cooldowns": False,
            "speed_hack": False,
        }
        self.speed_multiplier = 2.0

    def attach(self):
        self.mem.connect()
        print("[*] Attached to Hades II")

    def toggle_cheat(self, name):
        self.cheats[name] = not self.cheats[name]
        state = "ON" if self.cheats[name] else "OFF"
        print(f"[>] {name.replace('_', ' ').title()} {state}")

    def apply_god(self):
        flag = 1 if self.cheats["god_mode"] else 0
        self.mem.write_int(Offsets.GOD_MODE_FLAG, flag)

    def apply_health(self):
        if self.cheats["unlimited_health"]:
            max_health = self.mem.read_int(Offsets.HEALTH + 0x4)
            self.mem.write_int(Offsets.HEALTH, max_health)

    def apply_mana(self):
        if self.cheats["unlimited_mana"]:
            max_mana = self.mem.read_int(Offsets.MANA + 0x4)
            self.mem.write_int(Offsets.MANA, max_mana)

    def apply_gold(self):
        if self.cheats["max_gold"]:
            self.mem.write_int(Offsets.GOLD, 999999)

    def apply_resources(self):
        if self.cheats["all_resources"]:
            self.mem.write_int(Offsets.DARKNESS, 99999)
            self.mem.write_int(Offsets.KEYS, 99999)
            self.mem.write_int(Offsets.NECTAR, 99999)
            self.mem.write_int(Offsets.AMBROSIA, 99999)

    def apply_onehit(self):
        flag = 1 if self.cheats["one_hit_kill"] else 0
        self.mem.write_int(Offsets.ONE_HIT_KILL_FLAG, flag)

    def apply_cooldowns(self):
        multiplier = 0.0 if self.cheats["no_cooldowns"] else 1.0
        self.mem.write_float(Offsets.COOLDOWN_MULTIPLIER, multiplier)

    def apply_speed(self):
        if self.cheats["speed_hack"]:
            self.mem.write_float(Offsets.MOVEMENT_SPEED, self.speed_multiplier)
            self.mem.write_float(Offsets.ATTACK_SPEED, self.speed_multiplier)
        else:
            self.mem.write_float(Offsets.MOVEMENT_SPEED, 1.0)
            self.mem.write_float(Offsets.ATTACK_SPEED, 1.0)

    def apply_all(self):
        self.apply_god()
        self.apply_health()
        self.apply_mana()
        self.apply_gold()
        self.apply_resources()
        self.apply_onehit()
        self.apply_cooldowns()
        self.apply_speed()

    def run(self):
        print("[*] Trainer loop started. Press F1 to exit.")
        self.active = True
        while self.active:
            try:
                self.apply_all()
                time.sleep(0.1)
            except Exception as e:
                print(f"[!] Error: {e}")
                break
        print("[*] Trainer stopped")
