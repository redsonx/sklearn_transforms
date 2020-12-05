from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        
        cleanup_nums = {"koi_pdisposition": {"CANDIDATE": 1, "FALSE POSITIVE": 2}}
        data2 = data.replace(cleanup_nums, inplace=False)
        
        return data2.drop(labels=self.columns, axis='columns')
