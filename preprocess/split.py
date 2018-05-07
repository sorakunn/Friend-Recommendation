from tools.PP import *

# 指定参数
subject = '管理科学'                             # 数据集名称
amount = 4                                      # 数据集个数
null_reserved = True                            # 是否保留空值

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