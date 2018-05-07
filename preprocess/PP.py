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
        row = read(filename)
        df = df.append(row,ignore_index=True)            # 注意append后要传回
    return df


def split(subject, amount, null_reserved):
    """从url中分离出user_ID与friend_ID"""

    # 合并数据
    merged = merge(subject, amount)
    # 截取 ID (分要不要空值两种情况)
    df = [['博主ID','好友ID']]
    for index,row in merged.iterrows():
        if row[1]==row[1]:                           # 如果好友ID非空 （由于特性NaN不等于NaN，判断是否等于自身等价于判断是否为空）
            df.append( [row[0][49:],row[1][49:]] )      # 截取ID并存入数组
        else:
            if null_reserved:                        # 如果要保留空值
                df.append( [row[0][49:],-1] )           # 截取ID、空缺处赋为-1
    # 写出文件
    df = pd.DataFrame(data=df)
    write(df,'Data/Friend/Result/Raw/' + subject + '.csv')


def count(subject):
    """对每位user的好友个数进行计数"""
    # 读取数据
    df = read('Data/Friend/Result/Raw/' + subject + '.csv')
    # 初始化参数
    current = df.iloc[0,0]                  # current 表示当前正在计数的 user_ID
    count = 1
    result = [['博主ID','好友数']]
    # 计数
    for index,row in df.iterrows():
        if row[0]==current:                 # 若 ID 无变化则继续计数
            count += 1
        else:
            result.append([current,count])  # 若 ID 变化，保存上一ID信息，并转换为下一ID
            current = row[0]
            if row[1] == -1:
                count = 0
            else:
                count = 1
    # 写出文件
    df = pd.DataFrame(data=result)
    write(df,'Data/Friend/Result/Count/' + subject + '.csv')