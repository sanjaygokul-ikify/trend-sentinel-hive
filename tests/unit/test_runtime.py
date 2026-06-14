import unittest
from packages.utils.logging import setup_logging

class TestRuntime(unittest.TestCase):
    def test_setup_logging(self):
        setup_logging(level='INFO')
        self.assertEqual(logging.getLogger().level, logging.INFO)

if __name__ == '__main__':
    unittest.main()