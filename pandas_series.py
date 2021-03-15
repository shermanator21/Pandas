import pandas as pd

grades = pd.Series([87, 100, 94])

print(grades)

same_grade = pd.Series(98.6, range(3))

print(same_grade)

print(grades[0])
grades.count()
grades.mean()
grades.min()
grades.max()
grades.std()

# does all of the above and more
print(grades.describe())

# custom indices
grades = pd.Series([87, 100, 84], index=['Wally', 'Eva', 'Sam'])

print(grades)

# if you initialize a series with a dictionary, its keys become the Series' indices, and its values become the Series' element values
grades = pd.Series({'Wally': 87, 'Eva': 100, 'Sam': 94})

# you can access individual elements via square brackets containing a custom index
print(grades['Eva'])
# 100

print(grades.Wally)
# 87

print(grades.dtype)
# int64

print(grades.values)
# [87 100 94]

# Series of Strings
hardware = pd.Series(['Hammer', 'Saw', 'Wrench'])

'''0 Hammer
    1 Saw
    2 Wrench
    dtype: object'''

answer = hardware.str.contains('a')

print(answer)

hardware_upper = hardware.str.upper()

print(hardware_upper)
