class A:
    def __contains__(self, str):
        print('hello')

ach = {('killed monster', 'combo_king', 'explorer'), ('killed monster', 'found treasure', 'leveled up', 'treasure_seeker', 'boss_hunter', 'killed monster'), ('leveled up', 'treasure_seeker'), ('found treasure',)}
print(len({ach}))


