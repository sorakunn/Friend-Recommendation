import pandas as pd
import os

def read(path):
    """读取某一路径的csv格式数据文件"""
    # 获取根路径
    current = os.path.dirname(__file__)
    parrent = os.path.dirname(current)
    # 使用 pandas 进行读取
    path = parrent + '/' + path
    df = pd.read_csv(path, header=0, sep=' ')
    return df

def write(df, path):
    # 获取根路径
    current = os.path.dirname(__file__)
    parrent = os.path.dirname(current)
    # 使用 pandas 进行写出
    path = parrent + '/' + path
    df.to_csv(path, index=False, sep=' ')





