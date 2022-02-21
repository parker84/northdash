from turtle import pos
import pandas as pd

class TestSuite():

    def __init__(self, unique_cols:list) -> None:
        """
        Args:
            unique_cols (list): unique column set for the table
        """
        self.unique_cols = unique_cols
    
    def test_for_unique_column_set(self, df:pd.DataFrame):
        nrows = df.shape[0]
        n_unique_rows = df[self.unique_cols].drop_duplicates().shape[0]
        assert nrows == n_unique_rows, f"you have non unique rows in your unique cols: {self.unique_cols}"

    def test_for_nulls(self, df:pd.DataFrame, non_null_cols:list):
        nulls_per_col = df[non_null_cols].isnull().sum(axis=0)
        assert nulls_per_col.sum() == 0, f"you have nulls in non_null_cols: {nulls_per_col}"

    def test_for_holes(self, df:pd.DataFrame):
        """Test to see if all combinations of the unique column set exist.

        Args:
            df (pd.DataFrame): table we're testing
        """
        possible_combos = 1
        nrows = df.shape[0]
        for col in self.unique_cols:
            n_unique_vals = df[col].unique().shape[0]
            possible_combos *= n_unique_vals
        assert possible_combos == nrows, f"not all possible combos ({possible_combos}) exist, only {nrows}"




    