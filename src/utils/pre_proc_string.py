import pandas as pd
import re # lib de regex

class csvDataProcessor:
    def __init__(self, column_data: dict, img_coordinates: list):
        self.column_data = column_data
        self.coordinates = img_coordinates
        self.img_data_coord = self.map_data_to_coordinates(self.column_data, self.coordinates)

    def map_data_to_coordinates(self, csv_line_dict: dict, field_coordinates: list) -> dict:
        try:
            # Inicializa dicionário resultado
            result_dict = {}
            
            # Encontra índice do campo inicial (numero_ficha)
            fields_list = list(csv_line_dict.keys())
            
            if "numero_ficha" not in fields_list:
                print(f"Aviso: Campo 'numero_ficha' não encontrado no dicionário")
                return {}
                
            start_index = fields_list.index("numero_ficha")
            
            # Cria lista de campos a partir do campo numero_ficha
            filtered_fields = fields_list[start_index:]
            
            # Verifica se temos coordenadas suficientes
            if len(filtered_fields) > len(field_coordinates):
                print(f"Aviso: Mais campos ({len(filtered_fields)}) do que coordenadas ({len(field_coordinates)})")
            
            # Itera pelos campos filtrados
            coord_index = 0  # Índice para acompanhar a posição nas coordenadas
            
            for field in filtered_fields:
                value = csv_line_dict[field]

                # Ignora valores NaN, vazios ou None
                if pd.isna(value) or value == "nan" or value == "" or value is None:
                    coord_index += 1
                    continue
                    
                # Converte para string caso seja um número ou outro tipo
                if not isinstance(value, str):
                    value = str(value)

                if self.checkNumber(value) and field != 'numero_ficha':
                    value = value.split('.')[0]
                    for digit in value:
                        if coord_index < len(field_coordinates):
                            if digit in result_dict:
                                result_dict[digit].append(field_coordinates[coord_index])
                            else:
                                result_dict[digit] = [field_coordinates[coord_index]]
                            
                            coord_index += 1
                    continue

                
                if self.checkDate(value) and field != 'numero_ficha':
                     year, month, day = value.split('-')
                     for digit in day:
                        if coord_index < len(field_coordinates):
                            if digit in result_dict:
                                result_dict[digit].append(field_coordinates[coord_index])
                            else:
                                result_dict[digit] = [field_coordinates[coord_index]]
                            
                            coord_index += 1
                     for digit in month:
                        if coord_index < len(field_coordinates):
                            if digit in result_dict:
                                result_dict[digit].append(field_coordinates[coord_index])
                            else:
                                result_dict[digit] = [field_coordinates[coord_index]]
                            
                            coord_index += 1
                     for digit in year:
                        if coord_index < len(field_coordinates):
                            if digit in result_dict:
                                result_dict[digit].append(field_coordinates[coord_index])
                            else:
                                result_dict[digit] = [field_coordinates[coord_index]]
                            
                            coord_index += 1
                     continue
                # Se o índice estiver dentro dos limites da lista de coordenadas
                if coord_index < len(field_coordinates):
                    # Se o valor já existe no dicionário resultado, adiciona a coordenada à lista

                    if field in ['uf_notificacao', 'uf_residencia_p', 'uf']:
                        for letter in value:
                            if coord_index < len(field_coordinates):
                                if letter in result_dict:
                                    result_dict[letter].append(field_coordinates[coord_index])
                                else:
                                    result_dict[letter] = [field_coordinates[coord_index]]
                                coord_index += 1
                        continue
                    if value in result_dict:
                        result_dict[value].append(field_coordinates[coord_index])
                    # Senão, cria uma nova entrada com o valor e sua coordenada
                    else:
                        result_dict[value] = [field_coordinates[coord_index]]
                    
                    # Incrementa o índice das coordenadas
                    coord_index += 1
                else:
                    print(f"Aviso: Sem coordenadas suficientes para o campo '{field}'")
                    break
            
            return result_dict
            
        except Exception as e:
            print(f"Erro ao mapear dados para coordenadas: {e}")
            import traceback
            traceback.print_exc()
            return {}
        
    def checkNumber(self, data: str) -> bool:
        return bool(re.match(r"^\d+(\.\d+)?$", data))
    
    def checkDate(self, data: str) -> bool:
        return bool(re.match(r"^\d{4}-\d{2}-\d{2}$", data))