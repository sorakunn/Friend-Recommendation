import pandas as pd
import numpy as np
import os


def read(path):
    """读取某一路径的csv格式数据文件"""
    # 获取根路径
    current = os.path.dirname(__file__)
    parrent = os.path.dirname(current)
    # 使用 pandas 进行读取
    path = parrent + '/' + path
    df = pd.read_csv(path, header=0)
    return df


def write(df, path,header=False):
    # 获取根路径
    current = os.path.dirname(__file__)
    parrent = os.path.dirname(current)
    # 使用 pandas 进行写出
    path = parrent + '/' + path
    df.to_csv(path, index=False, header=header)

def to_list(dataframe):
    df = np.array(dataframe)  # np.ndarray()
    df = df.tolist()  # list
    return df



