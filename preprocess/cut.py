from tools.IO import read,write

df = read('Data/Friend/Result/User_Friend_Mutual2.txt')
for index,row in df.iterrows():
    if row[0]>5726:
        num = index
        break
df = df.iloc[:num]
write(df,'Data/Friend/Result/User_Friend_Mutual3.txt')