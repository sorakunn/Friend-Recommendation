import csv
import pandas as pd

NAME = '生命科学'
AMOUNT = 6;

NULLRESERVED = False;
COLUMN_1 = 'User_ID'
COLUMN_2 = 'Friend_ID'

# 定义存放列表
Blogger_UID = []
Friend_UID = []

for i in range(1,AMOUNT+1):
    # 指定路径
    if AMOUNT == 1:
        path_input = NAME +'.csv'
    else:
        path_input = NAME + '(' + str(i) + ').csv'
    # 读取数据
    with open(path_input, encoding='utf-8') as f1:
        reader = csv.reader(f1)
        reader = list(reader)[1:]

    # 截取、分组存放(分要不要空值两种情况)
        for row in reader:
            if row[1][49:]:
                Blogger_UID.append(row[0][49:])
                Friend_UID.append(row[1][49:])
            else:
                if NULLRESERVED:
                    Blogger_UID.append(row[0][49:])
                    Friend_UID.append(-1)
    # 合成为一个数据集
    UnindexData = list(zip(Blogger_UID, Friend_UID))

# 写出数据
df = pd.DataFrame(data = UnindexData, columns=[COLUMN_1, COLUMN_2])
if NULLRESERVED:
    df.to_csv(NAME+'_空值.txt', index=False, header=False,sep=' ')
else:
    df.to_csv(NAME+'_非空.txt', index=False, header=False,sep=' ')

# 读取数据
header = ['user_id', 'friend_id']
df = pd.read_csv(NAME+'_非空.txt', sep=' ', names=header)

# 重新打上索引

# 创建unique_user数组
unique_users = list(df.user_id.unique())
# 为user打上索引
temp = df['user_id'][0]
uid = 0
users = []
for user in df['user_id']:
    if user == temp:
        users.append(uid)
    else:
        temp = user
        uid += 1
        users.append(uid)

# 创建unique_friend数组
unique_friend = list(df.friend_id.unique())
for friend in unique_friend:
    if friend in unique_users:
        unique_friend.remove(friend)
print(len(unique_friend))
# 为friend打上索引
fid = len(unique_users)
friends = []
for friend in df['friend_id']:
    if friend in unique_users:
        friends.append(unique_users.index(friend))
    else:
        friends.append(fid+unique_friend.index(friend))

# 合成为一个数据集
IndexData = list(zip(users,friends))

# 写出数据
df = pd.DataFrame(data=IndexData, columns=[COLUMN_1, COLUMN_2])
df.to_csv(NAME + '_最终数据.txt', index=False, header=False, sep=' ')