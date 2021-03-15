import pandas as pd

grades_dict = {'Wally': [87, 96, 70],
               'Eva': [100, 87, 90],
               'Sam': [94, 77, 90],
               'Katie': [100, 81, 82],
               'Bob': [83, 65, 85]}

print(grades_dict)

grades = pd.DataFrame(grades_dict)

print(grades)

grades.index = ['Test1', 'Test2', 'Test3']

print(grades['Eva'])

print(grades.Sam)

print(grades.loc['Test1'])

# remember this is 0 based index. This gives second column of each row
print(grades.iloc[1])


print(grades.loc['Test1': 'Test3'])

print(grades.iloc[0:2])

print(grades.loc[['Test1', 'Test3']])

print(grades.iloc[0, 2])

# view only Eva and Katie's grades for test1 and test 2

print(grades.loc['Test1': 'Test2', ['Eva', 'Katie']])

print(grades.iloc[0:2, [1, 3]])

above_90 = grades[grades >= 90]

print(above_90)

b_grades = grades[(grades >= 80) & (grades < 90)]

print(b_grades)


# specific value
print(grades.at['Test2', 'Eva'])

print(grades.iat[1, 1])

grades.at['Test2', 'Eva'] = 100

print(grades)

print(grades.describe())

pd.set_option('precision', 2)

print(grades.describe())

# tests as columns
print(grades.T.describe())

print(grades.T.mean())

grades.sort_index(ascending=False)

print(grades)

grades.sort_index(axis=1)

print(grades)

grades.sort_values(by='Test1', axis=1, ascending=False)

print(grades)

grades.T.sort_values(by='Test1', ascending=False)

print(grades)
