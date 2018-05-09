from tools.IO import *


def merge(datatype,subject, amount):
    """读取多个单份文件，并合并返回"""
    # datatype 对应 friend 数据和 atricle 数据两种情况
    if datatype == 'f':
        datatype = 'Friend'
    elif datatype == 'a':
        datatype = 'Article'
    # 生成存放结构
    df = pd.DataFrame()
    # 对于被分成的每一份
    for i in range(1, amount + 1):
        # 指定根路径
        root = 'Data/' + datatype + '/Source/' + subject + '/'
        # 指定单份路径p;
        if amount == 1:
            filename = root + subject + '.csv'
        else:
            filename = root + subject + '(' + str(i) + ').csv'
        # 批量读取数据
        row = read(filename)
        df = df.append(row,ignore_index=True)            # 注意append后要传回
    return df


def split_f(subject, amount, null_reserved):
    """从url中分离出user_ID与friend_ID"""

    # 合并数据
    merged = merge('f',subject, amount)
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


def count_f(subject):
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


def split_a(subject,amount,year):
    """从url中分离出user_ID与article_ID，同时清洗并提取需要的数据"""
    # 合并数据
    merged = merge('a', subject, amount)
    # 定义存放列表
    url = []                                                    # 存放未截断的 user_ID，article_ID
    user_ids = []                                               # 存放未截断的 user_ID
    article_ids = []                                            # 存放未截断的 article_ID
    index_of_target = []                                          # 存放时间为指定年份的数据行
    # 数据清洗
    for index,row in merged.iterrows():
        # 阅读次数
        if row[1]==row[1]:
            row[1] = row[1][3:-4]
        # 文章时间（挑选出属于指定年份的行号）
        if row[2]==row[2]:
            if row[2][:4] == str(year):
                index_of_target.append(index)
        # 系统标签、用户标签（如果系统标签不存在，则将个人标签修正为系统标签）
        if row[4]!=row[4]:
            row[4] = row[3]
            row[3] = None
        # 分割用户ID、文章ID
        if row[7].find('-')!=-1:
            url = row[7][31:-5].split('-')
            user_ids.append(url[0])
            article_ids.append(url[1])
        else:
            user_ids.append(-1)
            article_ids.append(-1)
        # 删除正文尾部转载声明
        if row[6] == row[6]:
            if row[6].rfind('转载本文请') != -1:
                index = row[6].rindex('转载本文请')
                row[6] = row[6][:index]
    # 弹出 url 列，添加 User_ID，Article_ID 列
    merged.pop('页面网址')
    merged['博主ID'] = user_ids
    merged['文章ID'] = article_ids
    # 通过之前存入的index数组，提取出需要的数据行
    df = pd.DataFrame(columns=["标题", "阅读次数", "时间", "个人分类", "系统分类", "标签", "正文", "博主ID", "文章ID",])
    for index in index_of_target:
        df = df.append(merged.ix[index:index])               # 注意要将append后的数据传回
    # 写出数据
    write(df,'Data/Article/Result/Raw/' + subject + '.csv',header=True)


def count_a(subject):
    """对有博文的user进行博文篇数计数"""
    # 读取数据
    df = read('Data/Article/Result/Raw/' + subject + '.csv')
    # 定义存放列表
    result = [['博主ID', '博文数']]
    # 计数
    for user in df['博主ID'].unique():
        result.append([user,to_list(df['博主ID']).count(user)])
    # 写出文件
    df = pd.DataFrame(data=result)
    write(df,'Data/Article/Result/Count/' + subject + '.csv')
