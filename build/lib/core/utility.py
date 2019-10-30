"""
Docstring for custom DataFrame Utility functions -

These classes are designed to contain helpful built-in functions
for automating the more mundane processes common for data
science.
"""
import pandas as pd


class Utility:
    """
    Main Utility class. Object will hold methods for common functions
    used during data exploration and cleaning.
    """

    def __init__(self, dataframe):
        """
        Construct class Utility. Define core attributes:

        1. dataframe - The dataframe attribute is the dataframe
        specified in the parameter. It must be a pandas dataframe
        in order for most other functions to work, or python will
        raise an error.

        2. rows - Does return the shape of the dataframe's rows (length)

        3. cols - Does return the shape of the datatrames's columns (length)
        """

        self.dataframe = dataframe
        self.rows = dataframe.shape[0]
        self.cols = dataframe.shape[1]

    def null_count(self, column=None):
        """
        Null count method for the Utility class. Get count of nulls in
        dataframe. Contains just 1 attribute:

        1. nulls - Use pandas methods for counting nulls in the dataframe.
        If 'dataframe' is not a pandas dataframe object, will raise and error.
        2. If column is not supplied, returns all column null counts. Otherwise,
        returns null counts from specified column. Raise if column does not 
        exist.
        """
        if column == None:
            self.nulls = self.dataframe.isnull().sum()
            return self.nulls
        if column != None:
            self.nulls = self.dataframe[column].isnull().sum()
            return self.nulls

    def add_col(self, name, data):
        """
        Method to add a column to dataframe. Takes existing dataframe
        and mutates the object by reference.

        Key to note that to avoid
        making changes to the dataframe object passed into the class,
        you should make a copy of the dataframe to inspect the changes.
        """

        self.dataframe[name] = pd.Series(data)
        return self.dataframe

    def describe_all(self):
        """
        Method to get and print a description for every column in the
        dataframe.
        """

        for col in self.dataframe.columns:
            print('Description for',col)
            print(self.dataframe[col].describe())
            print(' ')
