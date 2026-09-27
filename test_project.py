import unittest
from rvrm import reverse, remove
from sf import sliceFront, sliceBack

class TestEncryptionModules(unittest.TestCase):

    def test_reverse(self):
        """Test if the string is accurately reversed."""
        self.assertEqual(reverse("hello"), "olleh")
        self.assertEqual(reverse("1234"), "4321")

    def test_remove(self):
        """Test if 4 characters are removed from both ends."""
        self.assertEqual(remove("1234CORE5678"), "CORE")

    def test_sliceFront(self):
        """Test accurate front slicing for even and odd lengths."""
        self.assertEqual(sliceFront("even"), "ev")
        self.assertEqual(sliceFront("hello"), "hel")

    def test_sliceBack(self):
        """Test accurate back slicing for even and odd lengths."""
        self.assertEqual(sliceBack("even"), "en")
        self.assertEqual(sliceBack("hello"), "lo")

if __name__ == '__main__':
    unittest.main()