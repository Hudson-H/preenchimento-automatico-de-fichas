import pandas as pd

class dataHolder:
    def __init__(self, csv_path: str, csv_line_id: str):
        self.data = self.load_csv(csv_path)
        self.cols = self.get_csv_cols()
        self.column_data = self.get_csv_line_as_dict(csv_line_id)

    def load_csv(self, csv_path: str) -> pd.DataFrame:
        try:
            return pd.read_csv(csv_path)
        except(FileNotFoundError, pd.errors.ParserError) as e:
            print(f'Erro ao carregar CSV: {e}')
            return []

    def get_csv_cols(self) -> list[str]:
        try:
            return self.data.columns.tolist()
        except AttributeError:
            print('Não foi possível carregar as colunas do CSV')
            return []
    
    def get_csv_line_as_dict(self, csv_line_id: str) -> dict:
        try:
            row = self.data.loc[self.data['nu_notific'] == csv_line_id] # pega uma linha do csv, ou seja, pega os dados de um registro da ficha
            if not row.empty:
                row_data = row.iloc[0] # row tem uma lista com o registro | row[0] tem o registro
                result_dict = {col: str(row_data[col]) for col in self.cols} # {'coluna do csv': 'campo da coluna'}
                
                return result_dict
            
            print('Ficha não encontrada')
            return {}
        
        except Exception as e:
            print(f'Erro ao converter linha para dicionário: {e}')
            return {}