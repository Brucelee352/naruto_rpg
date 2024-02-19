class Ninja:
    def __init__(self, name, HP, chakra, specialty, kekki_genkai):
        self.name = name
        self.HP = HP
        self.chakra = chakra 
        self.specialty = specialty
        self.kekki_genkai = kekki_genkai 
        
    def describe(self):
        if self.kekki_genkai is None:
            print(f'{self.name} does not have a Kekki Genkai!')
        else:
            print(f'Kekki Genkai: {self.kekki_genkai}')
        return f'Name: {self.name}, HP: {self.HP}, Chakra: {self.chakra}, Specialty: {self.specialty}'

class Jutsu:
    def __init__(self, release, users, jutsu_name, damage, chakra_cost):
        self.release = release
        self.users = users
        self.jutsu_name = jutsu_name
        self.damage = damage
        self.chakra_cost = chakra_cost
              
    def jutsu_info(self):
        print(f'Jutsu Name: {self.jutsu_name}')
        print(f'User: {self.users}')
        print(f'This jutsu is a {self.release} style technique!')
        print(f'Damage: {self.damage} points')
        print(f'Chakra Cost: {self.chakra_cost} points')

# Ninjas
naruto = Ninja(name = 'Naruto Uzumaki', HP = 12000, chakra = 50000, specialty = 'Wind', kekki_genkai = None)
sasuke = Ninja(name = 'Sasuke Uchiha', HP = 8000, chakra = 10000, specialty = 'Fire', kekki_genkai = 'Sharingan')
sakura = Ninja(name = 'Sakura Haruno', HP = 5000, chakra = 5000, specialty = 'Genjutsu', kekki_genkai = None)
kakashi = Ninja(name = 'Kakashi Hatake', HP = 10000, chakra = 18000, specialty = 'Lightning', kekki_genkai = 'Sharingan')


#Jutsu
rasengan = Jutsu(release = 'Wind', users = ['Naruto Uzumaki', 'Minato Namikaze', 'Kakashi Hatake', 'Jiraya'], jutsu_name = 'Rasengan', damage = 5000, chakra_cost = 2000)
shadow_clone = Jutsu(release = None, users = ['Naruto Uzumaki', 'Kakashi Hatake', 'Itachi Uchiha'], jutsu_name = 'Kage Bushin no Jutsu', damage = 0, chakra_cost = 500 * int(5))
great_fireball = Jutsu(release = 'Fire', users = ['Sasuke Uchiha', 'Itachi Uchiha'], jutsu_name = 'Goukyakku no Jutsu', damage = 2000, chakra_cost = 1000)
chidori = Jutsu(release = 'Lightning', users = 'Sasuke Uchiha', jutsu_name = 'Chidori', damage = 4500, chakra_cost = 4000)
raikiri = Jutsu(release = 'Lightning', users = 'Kakashi Hatake', jutsu_name = 'Raikiri', damage = 7000, chakra_cost = 3000)


