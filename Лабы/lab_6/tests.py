from task_1 import DecimalToHexadecimal
import unittest


class TestDecimalToHexadecimal(unittest.TestCase):

    def test_valid_conversion(self):
        converter = DecimalToHexadecimal('0')
        self.assertEqual(converter.convert(), '0')

        converter = DecimalToHexadecimal('16')
        self.assertEqual(converter.convert(), '10')

        converter = DecimalToHexadecimal('255')
        self.assertEqual(converter.convert(), 'FF')

        converter = DecimalToHexadecimal('4095')
        self.assertEqual(converter.convert(), 'FFF')

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            DecimalToHexadecimal('abc')

        with self.assertRaises(ValueError):
            DecimalToHexadecimal('12.5')

        with self.assertRaises(ValueError):
            DecimalToHexadecimal('-123')

        with self.assertRaises(ValueError):
            DecimalToHexadecimal('')

        with self.assertRaises(ValueError):
            DecimalToHexadecimal('12@34')


if __name__ == '__main__':
    unittest.main()
