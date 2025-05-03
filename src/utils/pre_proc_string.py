import pandas as pd
import re # lib de regex

class csvDataProcessor:
    def __init__(self, column_data: dict, img_coordinates: list):
        self.column_data = column_data
        self.coordinates = img_coordinates
        self.img_data_coord = self.map_data_to_coordinates(self.column_data, self.coordinates)

    def map_data_to_coordinates(self, csv_line_dict: dict, field_coordinates: list) -> dict:
        try:
            result_dict = {} # {'dado1': [(x1,y1), (x2,y2), ... (xn,yn)], 'daodo2': ...}
            
            # TODO: passar colunas por parâmetro para excluir essa computação a mais
            fields_list = list(csv_line_dict.keys()) # colunas 
            
            if "numero_ficha" not in fields_list:
                print(f"Aviso: Campo 'numero_ficha' não encontrado no dicionário")
                return {}
                
            start_index = fields_list.index("numero_ficha")

            filtered_fields = fields_list[start_index:]
            
            if len(filtered_fields) > len(field_coordinates):
                print(f"Aviso: Mais campos ({len(filtered_fields)}) do que coordenadas ({len(field_coordinates)})")
            
            coord_index = 0
            
            for field in filtered_fields:
                value = csv_line_dict[field]

                if pd.isna(value) or value == "nan" or value == "" or value is None:
                    coord_index += 1
                    continue
                    
                if not isinstance(value, str):
                    value = str(value)

                if self.checkNumber(value) and field != 'numero_ficha':
                    value = value.split('.')[0]
                    
                    coord_index, result_dict = self.string_process(value, result_dict, field_coordinates, coord_index)
                    continue

                
                if self.checkDate(value) and field != 'numero_ficha':
                     year, month, day = value.split('-')
                     coord_index, result_dict = self.string_process(day, result_dict, field_coordinates, coord_index)

                     coord_index, result_dict = self.string_process(month, result_dict, field_coordinates, coord_index)

                     coord_index, result_dict = self.string_process(year, result_dict, field_coordinates, coord_index)
                     continue
                if coord_index < len(field_coordinates):

                    if field in ['uf_notificacao', 'uf_residencia_p', 'uf']:
                        coord_index, result_dict = self.string_process(value, result_dict, field_coordinates, coord_index)
                        continue
                    if value in result_dict:
                        result_dict[value].append(field_coordinates[coord_index])
                    else:
                        result_dict[value] = [field_coordinates[coord_index]]
                    
                    coord_index += 1
                else:
                    # print(f"Aviso: Sem coordenadas suficientes para o campo '{field}'")
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
    
    def string_process(self, value, result_dict, field_coordinates, coord_index):
        for digit in value:
            if coord_index < len(field_coordinates):
                if digit in result_dict:
                    result_dict[digit].append(field_coordinates[coord_index])
                else:
                    result_dict[digit] = [field_coordinates[coord_index]]
                
                coord_index += 1
        
        return (coord_index, result_dict)