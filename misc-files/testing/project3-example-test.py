import unittest
from character import *
from item import *

class TestCharacter(unittest.TestCase):
    def setUpClass():
        Item.load_conditions()
        Item.load_items()

    def test_priest_nodamage(self):
        c = Priest('billben')
        m = Monster('The Electric Critter')
        health_before = c.health
        damage = c.take_damage(m)
        health_after = c.health
        self.assertEqual(health_before, health_after)

    def test_monster_death(self):
        m = Monster('blah')
        m.health = -1

if __name__ == '__main__':
    unittest.main()
