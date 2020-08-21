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
        return data.drop(labels=self.columns, axis='columns')


class UpdateData(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        mean_for_ok = 7.0
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        data.loc[
            (data["PERFIL"] == "EXATAS") 
            & (((data["REPROVACOES_MF"] == 0) | (data["REPROVACOES_MF"].empty)) & ((data["NOTA_MF"] < mean_for_ok) | (data["NOTA_MF"].empty))) 
            , "REPROVACOES_MF"
        ] = 1
        data.loc[
            (data["PERFIL"] == "EXATAS") 
            & (((data["REPROVACOES_EM"] == 0) | (data["REPROVACOES_EM"].empty)) & ((data["NOTA_EM"] < mean_for_ok) | (data["NOTA_EM"].empty))) 
            , "REPROVACOES_EM"
        ] = 1
        data.loc[
            (data["PERFIL"] == "HUMANAS") 
            & (((data["REPROVACOES_DE"] == 0) | (data["REPROVACOES_DE"].empty)) & ((data["NOTA_DE"] < mean_for_ok) | (data["NOTA_DE"].empty))) 
            , "REPROVACOES_DE"
        ] = 1
        data.loc[
            (data["PERFIL"] == "HUMANAS") 
            & (((data["REPROVACOES_GO"] == 0) | (data["REPROVACOES_GO"].empty)) & ((data["NOTA_GO"] == mean_for_ok) | (data["NOTA_GO"].empty)))
            , "REPROVACOES_GO"
        ] = 1
        data.loc[
            (data["PERFIL"] == "EXATAS") 
            & (((data["NOTA_MF"] == 0) | (data["NOTA_MF"].empty))) 
            , "NOTA_MF"
        ] = 5
        data.loc[
            (data["PERFIL"] == "EXATAS") 
            & (((data["NOTA_EM"] == 0) | (data["NOTA_EM"].empty))) 
            , "NOTA_EM"
        ] = 5
        data.loc[
            (data["PERFIL"] == "HUMANAS") 
            & (((data["NOTA_DE"] == 0) | (data["NOTA_DE"].empty))) 
            , "NOTA_DE"
        ] = 5
        data.loc[
            (data["PERFIL"] == "HUMANAS") 
            & (((data["NOTA_GO"] == 0) | (data["NOTA_GO"].empty)))
            , "NOTA_GO"
        ] = 5
        data.loc[
            (data["PERFIL"] == "EXCELENTE") 
            & (((data["NOTA_DE"] == 0) | (data["NOTA_DE"].empty))) 
            , "NOTA_DE"
        ] = 8
        data.loc[
            (data["PERFIL"] == "EXCELENTE") 
            & (((data["NOTA_EM"] == 0) | (data["NOTA_EM"].empty))) 
            , "NOTA_EM"
        ] = 8
        data.loc[
            (data["PERFIL"] == "EXCELENTE") 
            & (((data["NOTA_MF"] == 0) | (data["NOTA_MF"].empty))) 
            , "NOTA_MF"
        ] = 8
        data.loc[
            (data["PERFIL"] == "EXCELENTE") 
            & (((data["NOTA_GO"] == 0) | (data["NOTA_GO"].empty))) 
            , "NOTA_GO"
        ] = 8
        data.loc[
            (data["PERFIL"] == "EXCELENTE") 
            & (((data["NOTA_DE"] == 0) | (data["NOTA_DE"].empty))) 
            , "NOTA_DE"
        ] = 10
        data.loc[
            (data["PERFIL"] == "EXCELENTE") 
            & (((data["NOTA_EM"] == 0) | (data["NOTA_EM"].empty))) 
            , "NOTA_EM"
        ] = 10
        data.loc[
            (data["PERFIL"] == "EXCELENTE") 
            & (((data["NOTA_MF"] == 0) | (data["NOTA_MF"].empty))) 
            , "NOTA_MF"
        ] = 10
        data.loc[
            (data["PERFIL"] == "EXCELENTE") 
            & (((data["NOTA_GO"] == 0) | (data["NOTA_GO"].empty))) 
            , "NOTA_GO"
        ] = 10
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data