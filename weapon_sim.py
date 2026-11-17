import time
import random

class Weapons:
    def __init__(self, ammo, fire_rate, reload_time, max_ammo, recoil_pattern=None):
        self.ammo = ammo
        self.fire_rate = fire_rate
        self.last_shot = 0
        self.reload_time = reload_time
        self.max_ammo = max_ammo
        self.recoil_pattern = recoil_pattern or [(0,0)]
        self.shot_count = 0
        self.current_x = 0
        self.current_y = 0

    def reload(self):
        while True:
            r = input("Press R to reload: ").lower().strip()
            if r == "r":
                print("Reloading...")
                time.sleep(self.reload_time)
                self.ammo = self.max_ammo
                print("Done")
                print(f"Ammo: {self.ammo}")
                break
            else:
                print("Invalid input")
                
    def shoot(self):
        now = time.time()

        if now - self.last_shot < self.fire_rate:
            print("WAIT")
            return

        if self.ammo <= 0:
            print("Out of ammo")
            self.reload()
            return

        self.recover_recoil(now - self.last_shot)
        
        pattern_index = self.shot_count % len(self.recoil_pattern)
        base_x, base_y = self.recoil_pattern[pattern_index]

        jitter_x = random.uniform(-0.05, 0.05)
        jitter_y = random.uniform(-0.05, 0.05)

        self.current_x += base_x + jitter_x
        self.current_y += base_y + jitter_y

        self.shot_count += 1
        self.ammo -= 1
        self.last_shot = now

        print(f"Ammo: {self.ammo} | Recoil X: {self.current_x:.2f}, Y: {self.current_y:.2f}")

    def enter(self):
        while True:
            action = input("Press Enter to shoot (e to go back to menu) ").lower().strip()
            if action == "":
                self.shoot()
            elif action == "e":
                print(f"Recoil X: {self.current_x:.2f}, Y: {self.current_y:.2f}")
                break
            else:
                print("Invalid Input")
    
    def recover_recoil(self, elapsed):
        factor = 0.5 ** elapsed
        self.current_x *= factor
        self.current_y *= factor

class Pistol(Weapons):
    pass
class Glock17(Pistol):
    def __init__(self):
        super().__init__(ammo=17, fire_rate=0.15, reload_time=1.2, max_ammo=17, recoil_pattern=[(0,0.3),(0.05,0.35),(-0.05,0.3),(0,0.3)])
class Deagle(Pistol):
    def __init__(self):
        super().__init__(ammo=7, fire_rate=0.4, reload_time=1.8, max_ammo=7, recoil_pattern=[(0,1.0),(0.1,1.1),(-0.1,1.0),(0,1.05)])
class Revolver(Pistol):
    def __init__(self):
        super().__init__(ammo=6, fire_rate=0.6, reload_time=2, max_ammo=6, recoil_pattern=[(0,0.8),(0.15,0.85),(-0.15,0.8),(0,0.8)])

class AR(Weapons):
    pass
class M4(AR):
    def __init__(self):
        super().__init__(ammo=30, fire_rate=0.1, reload_time=2, max_ammo=30, recoil_pattern=[(0,0.2),(-0.03,0.25),(-0.05,0.2),(-0.05,0.2)])
class AK47(AR):
    def __init__(self):
        super().__init__(ammo=30, fire_rate=0.12, reload_time=2.1, max_ammo=30, recoil_pattern=[(0,0.25),(0.05,0.3),(0.1,0.25),(0.15,0.25)])
class Scar(AR):
    def __init__(self):
        super().__init__(ammo=20, fire_rate=0.13, reload_time=2.4, max_ammo=20, recoil_pattern=[(0,0.3),(0.08,0.4),(-0.06,0.38),(0.04,0.4)])

class Sniper(Weapons):
    pass
class Barrett50(Sniper):
    def __init__(self):
        super().__init__(ammo=1, fire_rate=1.5, reload_time=3.5, max_ammo=1, recoil_pattern=[(0,4.0)])
class HuntingRifle(Sniper):
    def __init__(self):
        super().__init__(ammo=1, fire_rate=1.0, reload_time=2.8, max_ammo=1, recoil_pattern=[(0,1.0)])

WEAPON_CATEGORIES = {
    "Pistols":{
        "1":("Glock 17", Glock17),
        "2":("Deagle", Deagle),
        "3":("Revolver", Revolver)
    },

   "ARs":{
        "1":("M4", M4),
        "2":("AK47", AK47),
        "3":("Scar", Scar)
    },

    "Snipers":{
        "1":("Barrett .50", Barrett50),
        "2":("Hunting Rifle", HuntingRifle)
    }
}

def pick_weapons(category_name):
    category = WEAPON_CATEGORIES[category_name]

    while True:
        print(f"Select from {category_name}:")
        for key, (weapon_name, _) in category.items():
            print(f"{key}. {weapon_name}")
        print("b. Back")

        choice = input("Pick: ").lower().strip()

        if choice == "b":
            return

        if choice in category:
            weapon_name, weapon_class = category[choice]
            weapon = weapon_class()
            print(f"Selected: {weapon_name}")
            weapon.enter()
            return
        else:
            print("Invalid choice")

def main_menu():
    while True:
        print("Select a Category")
        print("1. Pistols")
        print("2. ARs")
        print("3. Snipers")
        print("q. Quit")
        pick = input("Your choice: ").strip().lower()

        match pick:
            case "1": pick_weapons("Pistols")
            case "2": pick_weapons("ARs")
            case "3": pick_weapons("Snipers")
            case "q": 
                print("Closing")
                return
            case _:
                print("Invalid")

if __name__ == "__main__":
    main_menu()