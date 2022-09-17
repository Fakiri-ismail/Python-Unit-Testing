from unittest import TestCase, main
from program import add, get_data


class TestClacul(TestCase):
    """ the function name must start with 'test_' """
    
    # Positive Test
    def test_add(self):
        self.assertEqual(add(24, 43), 67)

    # Negative Test
    def test_add_string_input(self):
        self.assertEqual(add("Fakiri", 3), "Error: Invalid input")

    # Testing Error
    def test_add_None(self):
        with self.assertRaises(TypeError):
            add(None, None)

    # Fail Test
    def test_get_data(self):
        if not get_data(None):
            self.fail("No Data")


#main()