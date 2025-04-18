class Villain:

    def __init__(self, name, health, energy, weapons, shields):
        self.name = name
        self.health = health
        self.energy = energy
        self.weapons = weapons
        self.shields = shields
        self.current_weapon = None
        self.current_shield = None

    def describe(self):
        return f"Name: {self.name}, Health: {self.health}, Energy: {self.energy}"

    def choose_weapon(self):
        try:
            i = 0
            print("Weapon and its stats for", self.name, ":")
            for i in range(len(self.weapons) - 1):
                print(i, "-", self.weapons[i], "\n")
            i += 1
            print(i, "-", self.weapons[len(self.weapons) - 1].name, "\n")
            self.current_weapon = int(input("Choose a weapon: "))
            if self.weapons[self.current_weapon].resources == 0:
                print("You finished your resources. Choose another weapon")
                return self.choose_weapon()
            elif self.weapons[self.current_weapon].energy > self.energy:
                print("You dont have enough energy. Choose another weapon")
                return self.choose_weapon()
            self.energy -= self.weapons[self.current_weapon].energy
            if self.weapons[self.current_weapon].resources != 'INF':
                if self.weapons[self.current_weapon].resources != 0:
                    self.weapons[self.current_weapon].resources -= 1
        except IndexError:
            print("Choose a number in range")
            return self.choose_weapon()
        except ValueError:
            print("Enter numbers only")
            return self.choose_weapon()

    def choose_shield(self):
        try:
            i = 0
            print("Shield and its stats for", self.name, ":")
            for i in range(len(self.shields) - 1):
                print(i, "-", self.shields[i], "\n")
            i += 1
            print(i, "-", self.shields[len(self.shields) - 1].name, "\n")
            self.current_shield = int(input("Choose a shield: "))
            if self.shields[self.current_shield].resources == 0:
                print("You finished your resources. Choose another shield")
                return self.choose_shield()
            elif self.shields[self.current_shield].energy > self.energy:
                print("You dont have enough energy. Choose another shield")
                return self.choose_shield()
            self.energy -= self.shields[self.current_shield].energy
            if self.shields[self.current_shield].resources != 'INF':
                if self.shields[self.current_shield].resources != 0:
                    self.shields[self.current_shield].resources -= 1
        except IndexError:
            print("Choose a number in range")
            return self.choose_shield()
        except ValueError:
            print("Enter numbers only")
            return self.choose_shield()

    def attack(self, enemy):
        if self.weapons[self.current_weapon].name == 'Kalman_Missile':
            enemy.health -= self.weapons[self.current_weapon].damage
        elif enemy.weapons[enemy.current_weapon].name == 'Mega_Magnet':
            enemy.health -= self.weapons[self.current_weapon].damage * 0.8 * (1 - enemy.shields[enemy.current_shield].save)
        else:
            enemy.health -= self.weapons[self.current_weapon].damage * (1 - enemy.shields[enemy.current_shield].save)


class Weapon:

    def __init__(self, name, energy, damage, resources):
        self.name = name
        self.energy = energy
        self.damage = damage
        self.resources = resources

    def __str__(self):
        return f"Name: {self.name}, Energy: {self.energy}, Damage: {self.damage}, Resources: {self.resources}"


class Shield:

    def __init__(self, name, energy, save, resources):
        self.name = name
        self.energy = energy
        self.save = save
        self.resources = resources

    def __str__(self):
        return f"Name: {self.name}, Energy: {self.energy}, Save: {self.save}, Resources: {self.resources}"


Weapons_Gru = [Weapon('Freeze_Gun', 50, 11, 'INF'),
               Weapon('Electric_Prod', 88, 18, 5),
               Weapon('Mega_Magnet', 92, 10, 3),
               Weapon('Kalman_Missile', 120, 20, 1),
               Weapon('Skip', 0, 0, 'INF')]

Shields_Gru = [Shield('Energy_Projected_BarrierGun', 20, 0.4, 'INF'),
               Shield('Selective_Permeability', 50, 0.9, 2),
               Shield('Skip', 0, 0, 'INF')]

Weapons_Vector = [Weapon('Laser_Blasters', 40, 8, 'INF'),
                  Weapon('Plasma_Grenade', 56, 13, 8),
                  Weapon('Sonic_Resonance_Cannon', 100, 22, 3),
                  Weapon('Skip', 0, 0, 'INF')]

Shields_Vector = [Shield('Energy_Net_Trap', 15, 0.32, 'INF'),
                  Shield('Quantum_Deflector', 40, 0.8, 3),
                  Shield('Skip', 0, 0, 'INF')]

Gru = Villain('Gru', 100, 500, Weapons_Gru, Shields_Gru)

Vector = Villain('Vector', 100, 500, Weapons_Vector, Shields_Vector)

print()
print(Gru.describe(), "\n")
print(Vector.describe(), "\n")

print("Fight Begins!!\n")

j = 1

while (Gru.health > 0 and Vector.health > 0) and (Gru.energy > 20 or Vector.energy > 15):
    print("Round", j, "begins\n")

    Gru.choose_weapon()
    print()
    Gru.choose_shield()
    print()
    Vector.choose_weapon()
    print()
    Vector.choose_shield()
    print()

    if Gru.energy > 0:
        Gru.attack(Vector)
    if Vector.energy > 0:
        Vector.attack(Gru)

    print("Round finished\n")
    j += 1

    print(f"Gru's health is {Gru.health:.2f}")
    if Gru.energy <= 0:
        print("Gru's energy is finished")
    else:
        print("Gru's energy is", Gru.energy)
    print(f"Vector's health is {Vector.health:.2f}")
    if Vector.energy <= 0:
        print("Vector's energy is finished")
    else:
        print("Vector's energy is", Vector.energy)

print()
if Gru.health > Vector.health:
    print("Gru is the winner!!")
else:
    print("Vector is the winner!!")
