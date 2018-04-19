import pandas as pd
import os

def read(filename):
    # 获取根路径
    current = os.path.dirname(__file__)
    parrent = os.path.dirname(current)
    # 使用 pandas 进行读取
    path = parrent + '/' + filename
    df = pd.read_csv(path, header=0, sep=' ')
    return df

def write(df,filename):
    # 获取根路径
    current = os.path.dirname(__file__)
    parrent = os.path.dirname(current)
    # 使用 pandas 进行写出
    path = parrent + '/' + filename
    df.to_csv(path, index=False, sep=' ')