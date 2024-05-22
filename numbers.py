class DataTypes:
    def __init__(self):
        self.num1 = 5
        self.num2 = 3
        self.float1 = 3.14
        self.float2 = 2.71

    def integers(self):

        """ADDITION"""
        addition = self.num1 + self.num2
        print(addition)

        """SUBTRACTION"""
        subtract = self.num1 - self.num2
        print(subtract)

        """MULTIPLY"""
        multiply = self.num1 * self.num2
        print(multiply)

        """DIVISION"""
        divide = self.num1 / self.num2

        """SET DECIMAL PLACES"""
        print(f"{divide:.2f}")

        return addition, subtract, multiply, divide

    def floats(self):
        """FLOAT OPERATIONS"""
        sum_floats = self.float1 + self.float2
        diff_floats = self.float1 - self.float2
        product_floats = self.float1 * self.float2

        print(f"Sum of floats: {sum_floats:.2f}")
        print(f"Difference of floats: {diff_floats:.2f}")
        print(f"Product of floats: {product_floats:.2f}")

    def strings(self):
        """STRING OPERATIONS"""
        str1 = "Hello"
        str2 = "World"

        concat_str = str1 + " " + str2
        repeat_str = str1 * 3

        print(f"Concatenated string: {concat_str}")
        print(f"Repeated string: {repeat_str}")

    def booleans(self):
        """BOOLEAN OPERATIONS"""
        bool1 = True
        bool2 = False

        and_result = bool1 and bool2
        or_result = bool1 or bool2
        not_result = not bool1

        print(f"AND result: {and_result}")
        print(f"OR result: {or_result}")
        print(f"NOT result: {not_result}")

    def type_conversion(self):

        """ This method demonstrates type conversion between integers, floats, and strings """

        int_to_float = float(self.num1)
        float_to_int = int(self.float1)
        int_to_str = str(self.num2)
        str_to_int = int("10")

        print(f"Integer to float: {int_to_float}")
        print(f"Float to integer: {float_to_int}")
        print(f"Integer to string: {int_to_str}")
        print(f"String to integer: {str_to_int}")


"""Create an instance of the DataTypes class"""

data = DataTypes()

""" Call the respective methods to demonstrate operations on different data types"""
data.integers()
data.floats()
data.strings()
data.booleans()
data.type_conversion()