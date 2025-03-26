from utils import data_holder as dh
from utils import pre_proc_string as pps
from utils import contants as cts

from PIL import Image, ImageDraw, ImageFont

img_path = "../io/records/Botulismo_v5.png"
csv_path = '../io/csv_data/teste_ficha_botulismo.csv'
imagem = Image.open(img_path)
draw = ImageDraw.Draw(imagem)

try:
    font = ImageFont.truetype("arial.ttf", 20)  
except IOError:
    font = ImageFont.load_default()

csv_data_holder = dh.dataHolder(csv_path, 'teste_botulismo')
csv_data_processor = pps.csvDataProcessor(csv_data_holder.column_data, cts.field_coordinates)

for campo, coordenadas_campo in csv_data_processor.img_data_coord.items():
    for pos in coordenadas_campo:
        draw.text(pos, campo, fill="black", font=font)
 
file_name = img_path.strip('/')[-1]

imagem.save(f"../io/filled_records/{file_name}.png")
imagem.show()