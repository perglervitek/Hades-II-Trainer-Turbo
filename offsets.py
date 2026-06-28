class Offsets:
    HEALTH = 0x02A4B3F0
    MANA = 0x02A4B3F4
    GOLD = 0x02A4B3F8
    DARKNESS = 0x02A4B3FC
    KEYS = 0x02A4B400
    NECTAR = 0x02A4B404
    AMBROSIA = 0x02A4B408
    COOLDOWN_MULTIPLIER = 0x02A4B40C
    MOVEMENT_SPEED = 0x02A4B410
    ATTACK_SPEED = 0x02A4B414

    GOD_MODE_FLAG = 0x02A4B418
    ONE_HIT_KILL_FLAG = 0x02A4B41C

    @staticmethod
    def get_all():
        return {{
            "health": Offsets.HEALTH,
            "mana": Offsets.MANA,
            "gold": Offsets.GOLD,
            "darkness": Offsets.DARKNESS,
            "keys": Offsets.KEYS,
            "nectar": Offsets.NECTAR,
            "ambrosia": Offsets.AMBROSIA,
            "cooldown_multiplier": Offsets.COOLDOWN_MULTIPLIER,
            "movement_speed": Offsets.MOVEMENT_SPEED,
            "attack_speed": Offsets.ATTACK_SPEED,
            "god_mode_flag": Offsets.GOD_MODE_FLAG,
            "one_hit_kill_flag": Offsets.ONE_HIT_KILL_FLAG,
        }}
