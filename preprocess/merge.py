from tools.IO import *

def merge(subject, amount):
    """读取多个单份文件，并合并返回"""
    # 生成存放结构
    df = pd.DataFrame()
    # 对于被分成的每一份
    for i in range(1, amount + 1):
        # 指定根路径
        root = 'Data/Friend/Source/' + subject + '/'
        # 指定单份路径
        if amount == 1:
            filename = root + subject + '.csv'
        else:
            filename = root + subject + '(' + str(i) + ').csv'
        # 批量读取数据
        temp = read(filename)
        df = df.append(temp,ignore_index=True)            #注意append后要传回
    return df