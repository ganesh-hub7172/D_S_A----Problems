class Solution:
    def convertDateToBinary(self, date):
        year, month, day = date.split('-')
        # Convert each part to integer, then to binary, remove '0b' prefix
        year_bin = bin(int(year))[2:]
        month_bin = bin(int(month))[2:]
        day_bin = bin(int(day))[2:]
        # Concatenate strings using '+'
        return year_bin + '-' + month_bin + '-' + day_bin
