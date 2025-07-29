import re
import pandas as pd
from quotes_scroll.enum_models import ConfigGeneral


class DataFactory:

    """ Fuente principal para controlar la data no refinada """
    
    def __init__(self, **kwargs):
        self.spider = kwargs.get('spider')

    def process_data(self):
        data_processor = DataProcessor(spider=self.spider)
        data_processor.process_data()


class DataProcessor:

    """ Procesamiento de los datos en formato json """
    
    def __init__(self, **kwargs):
        self.spider = kwargs.get('spider')

    def process_data(self):
        df = self._get_dataframe(ConfigGeneral.EXTRACTOR_DOCUMENT_NAME_PATH.value)
        data_refiner = DataRefiner(spider=self.spider)
        df_output = data_refiner.refine_data(df)
        data_exporter = DataExporter(spider=self.spider)
        data_exporter.export_data(df_output)

    def _get_dataframe(self, document_path: str) -> pd.DataFrame:
        df = pd.read_json(document_path)
        return df
    

class DataRefiner:

    """ Refinar o manipular la informacion de que sea necesaria """

    def __init__(self, **kwargs):
        self.spider = kwargs.get('spider')

    def refine_data(self, df: pd.DataFrame) -> pd.DataFrame:
        
        data_cleaner = DataCleaner(spider=self.spider)
        df = data_cleaner.clean_data(df)
        
        # Expandir listas de tags en filas separadas
        df = df.explode('quotes_tag').reset_index(drop=True)
        df['quotes_tag'] = df['quotes_tag'].apply(str.strip)
        
        # Ordenar por fecha de nacimiento (mayor a menor)
        df = df.sort_values('born_date', ascending=True).reset_index(drop=True)
        
        return df.fillna('').drop_duplicates()


class DataCleaner:

    """ Generar limpieza o transformacion de datos a su equivalente correspondiente """

    def __init__(self, **kwargs):
        self.spider = kwargs.get('spider')
        self.columns = [
            "author_name",
            "born_date",
            "death_date",
            "born_location",
            "author_description",
            "quote",
            "quotes_tag",
            "author_goodreads_link",
        ]

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        df['author_name'] = df['quotes_author_name'].apply(self._clean_special_lines)
        df['born_date'] = pd.to_datetime(df['goodreads_born_date'], format='%B %d, %Y', errors="coerce").fillna('')
        df['death_date'] = pd.to_datetime(df['goodreads_death_date'], format='%B %d, %Y', errors="coerce").fillna('')
        df['born_location'] = df['goodreads_born_location'].apply(self._clean_special_lines)
        df['author_description'] = df['goodreads_description'].apply(self._clean_special_lines)
        df['quote'] = df['quotes_text'].apply(self._clean_special_lines)
        df['quotes_tag'] = df['quotes_tags']
        df['author_goodreads_link'] = df['quotes_author_goodreads_link']
        return df[self.columns]
    
    def _clean_special_lines(self, data: str) -> str:
        data = re.sub(r'\n|\t', ' ', data)
        data = re.sub(r'\s{2,}', ' ', data)
        data = re.sub(r'\"|ˈ', '\'', data)
        data = re.sub(r'–', '-', data)
        return data.strip()
    

class DataExporter:

    """ Exportar la data del dataframe a un archivo csv """

    def __init__(self, **kwargs):
        self.spider = kwargs.get('spider')
    
    def export_data(self, df: pd.DataFrame):
        df.to_csv(
            ConfigGeneral.REFINE_DOCUMENT_NAME_PATH.value,
            index=False,
            encoding='utf-8',
        )
