
import pandas as pd


def carregar_dados():
    """
    Carrega dados do arquivo CSV.
    
    Returns:
        pandas.DataFrame: DataFrame com os dados carregados
    """
    caminho = 'dados/'
    df_original = pd.read_csv(caminho + "Table data.csv")

    return df_original


def seconds_to_mmss_float(seconds):
    """
    Converte segundos para formato MM.SS em float.
    
    Args:
        seconds: Tempo em segundos
    
    Returns:
        float: Tempo no formato MM.SS
    """
    minutes = int(seconds) // 60
    sec = int(seconds) % 60
    return float(f"{minutes}.{sec:02d}")

def tratar_dados(df_original):
    """
    Aplica tratamento de dados no DataFrame.
    
    Args:
        df_original (pandas.DataFrame): DataFrame original
    
    Returns:
        pandas.DataFrame: DataFrame tratado
    """
    # Cria cópia e remove primeira linha
    df = df_original.copy()
    df = df.drop(index=0)
    
    # Converte colunas categóricas
    colunas_categoricas = ["Video title"]
    for coluna in colunas_categoricas:
        df[coluna] = df[coluna].astype("category")
    
    # Converte colunas de data
    colunas_data = ["Video publish time"]
    for coluna in colunas_data:
        df[coluna] = pd.to_datetime(df[coluna])
    
    # Converte duração para formato MM.SS
    df["Duration M.S"] = df["Duration"].apply(seconds_to_mmss_float)
    
    # Processa duração média de visualização
    df["Average view duration M.S"] = pd.to_timedelta(df['Average view duration'])
    df['Minutes'] = df['Average view duration M.S'].dt.components['minutes']
    df['Seconds'] = df['Average view duration M.S'].dt.components['seconds']
    df['Average view duration M.S'] = df['Minutes'] + (df['Seconds'] / 100)
    
    # Otimiza tipos de dados float
    colunas_float = df.select_dtypes(include="float64").columns
    for coluna in colunas_float:
        df[coluna] = pd.to_numeric(df[coluna], downcast='float')
    
    # Otimiza tipos de dados int
    colunas_int = df.select_dtypes(include="int64").columns
    for coluna in colunas_int:
        df[coluna] = pd.to_numeric(df[coluna], downcast='integer')
    
    # Remove colunas desnecessárias
    colunas_remover = ["Content", "Duration", "Unique viewers", "Stayed to watch (%)", 
                       "Average views per viewer", "New viewers", "Returning viewers", 
                       "Watch time (hours)", "Average view duration", "Minutes", "Seconds"]
    df = df.drop(colunas_remover, axis=1)
    
    return df

def salvar_dados(df, caminho="dados/df_final.csv"):
    """
    Salva o DataFrame em um arquivo CSV.
    
    Args:
        df (pandas.DataFrame): DataFrame a ser salvo
        caminho (str): Caminho onde salvar o arquivo. Default: "dados/df_final.csv"
    
    Returns:
        None
    """
    df.to_csv(caminho, index=False)
    print(f"Dados salvos em: {caminho}")

if __name__ == "__main__":
    df_original = carregar_dados()
    df_tratado = tratar_dados(df_original)
    salvar_dados(df_tratado)
    print(df_tratado.head())
    print("\nInfo do DataFrame tratado:")
    print(df_tratado.info())