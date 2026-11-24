import unittest

from PIL.PdfParser import pdf_repr

from src.prey_predator_sim.species import Creature


class TestCreature(unittest.TestCase):

    def test_probability_smaller_than_zero(self):

        with self.subTest(msg='p_death < 0'):
            test_creature = Creature(p_death=-3, p_reproduce=0.3)
            self.assertEqual(test_creature.p_death, 0.0)

        with self.subTest(msg='p_reproduce < 0'):
            test_creature = Creature(p_death=0.2, p_reproduce=-4)
            self.assertEqual(test_creature.p_reproduce, 0.0)

    def test_probability_greater_than_one(self):

        with self.subTest(msg='p_death > 1'):
            test_creature = Creature(p_death=2, p_reproduce=0.3)
            self.assertEqual(test_creature.p_death, 1.0)

        with self.subTest(msg='p_reproduce > 1'):
            test_creature = Creature(p_death=0.2, p_reproduce=7)
            self.assertEqual(test_creature.p_reproduce, 1.0)

    def test_probability_descriptor(self):

        p_death = 0.1
        p_reproduce = 0.3

        test_creature = Creature(p_death=p_death, p_reproduce=p_reproduce)

        with self.subTest(msg='p_death (setter, getter)'):
            self.assertEqual(test_creature.p_death, p_death)

        with self.subTest(msg='p_reproduce (setter, getter)'):
            self.assertEqual(test_creature.p_reproduce, p_reproduce)
