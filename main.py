from surprise import Reader
from surprise import Dataset
from surprise import KNNBasic
from surprise.model_selection import cross_validate

FILE_PATH = 'User_Friend_Mutual2.txt'

# 读取数据
reader = Reader(line_format='user item rating', sep=' ', rating_scale =(0,1))
data = Dataset.load_from_file(FILE_PATH, reader=reader)

# 使用算法
algo = KNNBasic()

cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
