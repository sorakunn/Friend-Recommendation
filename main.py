from preprocess.PP import *

merge()




# from tools.IO import read
# from surprise import Reader
# from surprise import Dataset
# from surprise import KNNBasic
# from surprise.model_selection import KFold
# from evaluation import PR
#
# FILE_PATH= 'Data/Friend/Result/User_Friend_Mutual3.txt'
# # 读取数据
# reader = Reader(line_format='user item rating', sep=' ', rating_scale =(0,1))
# data = Dataset.load_from_df(read(FILE_PATH), reader=reader)
#
# kf = KFold(n_splits=5)
# # 使用算法
# algo = KNNBasic()
# for trainset, testset in kf.split(data):
#     algo.fit(trainset)
#     predictions = algo.test(testset)
#     precisions, recalls = PR.precision_recall_at_k(predictions, k=5, threshold=4)
#     # Precision and recall can then be averaged over all users
#     print(sum(prec for prec in precisions.values()) / len(precisions))
#     print(sum(rec for rec in recalls.values()) / len(recalls))