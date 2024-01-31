#import unittest and main
# create a class
#test royal flush, straight, 3pair and test game as well

import unittest
from pokerspadegame import main


class MyTestCase(unittest.TestCase):
    def testroyalflush(self):
        self.assertEqual(main.check_royal_flush('S2', 'S3', 'S4'), 0)

    def teststraight(self):
        self.assertEqual(main.check_straight('S3', 'S4', 'S5'), 5)

    def test3pair(self):
        self.assertEqual(main.check_3ofa_kind('S8', 'S8', 'S8'), 8)

    def failteststraight(self):
        self.assertEqual(main.check_straight('S8', 'S5', 'S1'), 0)

    def failteststraight2(self):
        self.assertEqual(main.check_straight('S8', 'S2', 'S3'), 0)

    def failtestroyalflush(self):
        self.assertEqual(main.check_royal_flush('SQ', 'SK', 'SA'), 14)

    def failtest3pair(self):
        self.assertEqual(main.check_3ofa_kind('S3', 'S2', 'S3'), 0)

    def testGame(self):
        self.assertEqual(main.play_cards('S2', 'S3', 'S4', 'SQ', 'SK', "SA"), 1)

    def test2Game(self):
        self.assertEqual(main.play_cards('SQ', 'SK', 'SA', 'S2', 'S3', "S4"), -1)

    def test3Game(self):
        self.assertEqual(main.play_cards('S3', 'S3', 'S3', 'S3', 'S3', "S3"), 0)

