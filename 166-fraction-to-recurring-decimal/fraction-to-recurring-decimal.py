class Solution:
    def fractionToDecimal(self, numerator, denominator):
        # Handle zero numerator
        if numerator == 0:
            return "0"

        result = []

        # Handle sign
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")

        numerator = abs(numerator)
        denominator = abs(denominator)

        # Integer part
        integer_part = numerator // denominator
        result.append(str(integer_part))

        remainder = numerator % denominator
        if remainder == 0:
            return "".join(result)

        result.append(".")

        remainder_map = {}  # remainder -> position in result

        while remainder != 0:
            if remainder in remainder_map:
                idx = remainder_map[remainder]
                result.insert(idx, "(")
                result.append(")")
                break

            remainder_map[remainder] = len(result)
            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator

        return "".join(result)
