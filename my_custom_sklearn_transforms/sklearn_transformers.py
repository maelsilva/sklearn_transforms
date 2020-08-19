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
    def __init__(self, columns):
        self.columns = columns
        
    def fit(self, X, y):
        return self
    
    def transform(self, X, y):
        mean_for_ok = 7.0
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        print(self)
        data = X.copy()
        data.loc[(data["PERFIL"] == "DIFICULDADE") & (data["REPROVACOES_DE"] == 0), "REPROVACOES_DE"] = 1
        data.loc[(data["PERFIL"] == "DIFICULDADE") & (data["REPROVACOES_EM"] == 0), "REPROVACOES_EM"] = 1
        data.loc[(data["PERFIL"] == "DIFICULDADE") & (data["REPROVACOES_MF"] == 0), "REPROVACOES_MF"] = 1
        data.loc[(data["PERFIL"] == "DIFICULDADE") & (data["REPROVACOES_GO"] == 0), "REPROVACOES_GO"] = 1
        data.loc[(data["PERFIL"] == "EXATAS") & (data["REPROVACOES_MF"] == 0) & (data["NOTA_MF"] < mean_for_ok), "REPROVACOES_MF"] = 1
        data.loc[(data["PERFIL"] == "EXATAS") & (data["REPROVACOES_EM"] == 0) & (data["NOTA_EM"] < mean_for_ok), "REPROVACOES_EM"] = 1
        data.loc[(data["PERFIL"] == "HUMANAS") & (data["REPROVACOES_DE"] == 0) & (data["NOTA_DE"] < mean_for_ok), "REPROVACOES_DE"] = 1
        data.loc[(data["PERFIL"] == "HUMANAS") & (data["REPROVACOES_GO"] == 0) & (data["NOTA_GO"] < mean_for_ok), "REPROVACOES_EM"] = 1
        data.loc[(df_data_1["PERFIL"] == "EXCELENTE") & (data["NOTA_DE"] == 0), "NOTA_DE"] = 10
        data.loc[(df_data_1["PERFIL"] == "EXCELENTE") & (data["NOTA_EM"] == 0), "NOTA_EM"] = 10
        data.loc[(df_data_1["PERFIL"] == "EXCELENTE") & (data["NOTA_MF"] == 0), "NOTA_MF"] = 10
        data.loc[(df_data_1["PERFIL"] == "EXCELENTE") & (data["NOTA_GO"] == 0), "NOTA_GO"] = 10
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data