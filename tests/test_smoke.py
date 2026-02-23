import unittest

from rpg.game import Game


class TestSmoke(unittest.TestCase):
    def test_start_message(self):
        self.assertIn("RPG Surreal", Game().start_message())


if __name__ == "__main__":
    unittest.main()
