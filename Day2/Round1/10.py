# A mystical Gryphon only appears in a leap year. A year is a leap year if it's divisible by 4, BUT NOT if it's divisible by 100, UNLESS it's ALSO divisible by 400. Given a year, will you see a 'GRYPHON SIGHTING' or have a 'QUIET YEAR'?

year = int(input("Year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("GRYPHON SIGHTING")
else:
    print("QUIET YEAR")
