import pandas as pd

filename= r"C:\Users\USER\Documents\ML Project\ML based PL Prediction\data\CTF_clean.csv"

def Cleaned_data(FilePath:str) -> pd.DataFrame:
    path=pd.read_csv(FilePath)
    return path

df=Cleaned_data(filename)
print(df.head())

