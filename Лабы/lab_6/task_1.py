class DecimalToHexadecimal:
    def __init__(self, decimal_str):
        self.decimal_str = decimal_str
        self._validate()

    def _validate(self):
        if not self.decimal_str or not self.decimal_str.isdigit():
            raise ValueError('Invalid decimal number')

    def decimal_to_int(self):
        return int(self.decimal_str)

    @staticmethod
    def int_to_hexadecimal(decimal_value):
        return hex(decimal_value)[2:].upper()

    def convert(self):
        decimal_value = self.decimal_to_int()
        return self.int_to_hexadecimal(decimal_value)


if __name__ == '__main__':
    decimal_str = input()
    converter = DecimalToHexadecimal(decimal_str)
    hexadecimal_str = converter.convert()
    print(f"Dec: {decimal_str} -> Hex: {hexadecimal_str}")
