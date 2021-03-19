'''
Perform the following tasks with pandas Series:

1. Create a Series from the list [7, 11, 13, 17].

2. Create a Series with five elements that are all 100.0.

3. Create a Series with 20 elements that are all random numbers in the range 0 to 100. 
            Use method describe to produce the Series’ basic descriptive statistics.

4. Create a Series called temperatures of the floating-point values 98.6, 98.9, 100.2 and 97.9. 
            Using the index keyword argument, specify the custom indices 'Julie', 'Charlie', 'Sam' and 'Andrea'.

5. Form a dictionary from the names and values in Part (4), then use it to initialize a Series.
'''

import pandas as pd
import numpy as np

# 1.
pandaSeries = pd.Series([7, 11, 13, 17])
print(pandaSeries)

# 2.
pandaSeries2 = pd.Series(100.0, range(5))
print(pandaSeries2)

# 3.
pandaSeries3 = pd.Series(np.random.randint(0, 101, size=20))
print(pandaSeries3)

pandaSeries3.describe()

# 4.
temperatures = pd.Series([98.6, 98.9, 100.2, 97.9], index=[
                         'Julie', 'Charlie', 'Sam', 'Andrea'])

print(temperatures)

# 5.
gradesDict = {'Julie': 98.6, 'Charlie': 98.9, 'Sam': 100.2, 'Andrea': 97.9}

gradesSeries = pd.Series(gradesDict)
print(gradesSeries)
