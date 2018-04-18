import pandas as pd
import numpy as np
rows_amount = 5727
df = pd.read_csv('UserID_FriendID.txt', header=0, sep=' ')
df = np.array(df)
df = df.tolist()

result = []

for row in df:
    if row[1] >= rows_amount:
        result.append([row[1],row[0]])

df.extend(result)

write = pd.DataFrame(data=df,columns=['User_ID','Friend_ID'])
write.to_csv('Square.txt', index=False, sep=' ')