# SISTEMA DE PREENCHIMENTO AUTOMÁTICO DE FICHAS

## Objetivo

O objetivo principal do sistema é preencher fichas de agravos de doenças retiradas do Sistema de Informação de Agravos de Notificação (SINAN) com dados coletados dos registros das fichas do software RedCap.

## planejamento de atividades

- [X] protótipo do sistema que preenche uma ficha
- [] refatoração do código do protótipo (retirar código duplicado, tentar diminuir métodos, etc)
- [] adicionar mais validações aos campos
    - [] validação dos números em idade, código, etc
    - [] validar campos numéricos vazios
- [] implementar coleta de dados do RedCap através da API
    - [] consumir api
    - [] renomear csv dependendo da ficha que foi utilizada
    - [] utilizar dados e apagar csv
- [] planejar criação das fichas em questão de nomenclatura de variáveis, validação de campos, etc
- [] planjear interface no figma
    - [] definir campos
    - [] definir como vai funcionar
- [] estudar streamlit para fazer interface desktop

## como utilizar

- digite o seguinte dentro da pasta _src/_:

```bash
python3 main.py
```

após isso, uma imagem com os campos da ficha preenchidos será aberta.

### Sites
- site para pegar coordenadas do mouse em uma imagem: [mouse tracker](https://www.mobilefish.com/services/record_mouse_coordinates/record_mouse_coordinates.php)
- site do sinan para ver as fichas (acesse o tópico "doenças e agravos"): [sinan](https://portalsinan.saude.gov.br/)

## Estrutura das pastas

```bash
.
├── README.md
├── io
│   ├── csv_data
│   │   ├── FichasDeNotificaoNVEUEM_DataDictionary_2025-02-07.csv
│   │   └── teste_ficha_botulismo.csv
│   ├── filled_records
│   │   └── Botulismo_v5_editada.png
│   └── records
│       └── Botulismo_v5.png
├── relatorio_pacientes_transfundidos.pdf
└── src
    ├── main.py
    └── utils
        ├── contants.py
        ├── data_holder.py
        └── pre_proc_string.py
```

- **io:** pasta que contem os dados de entrada
    - **csv_data:** pasta com os dados exportados do redcap
    - **filled_records:** ficha em png preenchida
    - **records:** ficha em png que será preenchida
- **src:** pasta com os arquivos de código
    - **utils:** arquivos com as principais funções utilizadas pela main
