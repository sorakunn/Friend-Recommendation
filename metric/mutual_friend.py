import pandas as pd
import numpy as np
import scipy.sparse as sps
import matplotlib.pyplot as plt
import math

PATH_INPUT = 'Square.txt'

# 读取数据
df = pd.read_csv(PATH_INPUT, sep=' ', header=0, names=['user_id', 'friend_id'])

# 创建关系矩阵
is_friend = [1] * len(df['user_id'])
relation = sps.coo_matrix((is_friend, (df['user_id'], df['friend_id'])))
relation = relation.tocsr()

plt.scatter( df['friend_id'],df['user_id'],0.01)
plt.show()

# 计算共同好友比例
mutual_friend = []
for user in range(0, relation.shape[0]):                                        # 遍历每个用户
    row = relation.getrow(user)
    i, j, v = sps.find(row)
    # 获取用户的直接好友集
    subset_1 = j
    for friend in subset_1:                                                     # 遍历每个直接好友
        col = relation.getcol(friend)
        i, j, v = sps.find(col)
        # 获取用户直接好友的好友集
        subset_2 = i;
        intersection = list(set(subset_1).intersection(set(subset_2)))          # 求交集
        matual = len(intersection) / math.sqrt(len(subset_1) * len(subset_2))   # 共同好友比例
        mutual_friend.append(round(matual,2))

# mutual = sps.coo_matrix(mutual_friend, (df['user_id'], df['friend_id']))
df = np.array(df)
df = df.tolist()
user_ID = []
friend_ID = []
for row in df:
    user_ID.append(row[0])
    friend_ID.append(row[1])
df = list(zip(user_ID,friend_ID,mutual_friend))
df = df[0:5727]

write = pd.DataFrame(data=df,columns=['User_ID','Friend_ID','mutual_friend'])
write.to_csv('User_Friend_Mutual3.txt', index=False, sep=' ')

# Recommender-Systems
# A naive algorithm for recommender system. My graduation project.