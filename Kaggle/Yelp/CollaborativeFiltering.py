import MatrixFactorization as mf
import numpy as np
import csv

class CF:
    def __init__(self):
        self.Theta = 0
        self.X = 0

    def fit(self, matrix_rating, number_features=20):
        number_business = np.max(matrix_rating[:,0]) + 1 # 11537
        number_user = np.max(matrix_rating[:,1]) + 1 # 45981
        print "business:%d and user:%d" %(number_business, number_user)
        Theta_initial = np.random.rand(number_user, number_features)
        X_initial = np.random.rand(number_business, number_features)
        MF = mf.matrix_factorization(matrix_rating, Theta_initial, X_initial, number_features)
        self.Theta, self.X = MF.training()

    def predict(self, test_pair, business_index, user_index):
        business_train = []
        user_train = []
        business_test = []
        with open("business_train.csv", "rb") as business_train_object:
            business_train_file = csv.reader(business_train_object)
            header = business_train_file.next()
            for line in business_train_file:
                business_train.append([line[0], line[1], float(line[2])])
        with open("business_test.csv", "rb") as business_test_object:
            business_test_file = csv.reader(business_test_object)
            header = business_test_file.next()
            for line in business_test_file:
                business_test.append([line[0], line[1]])
        with open("user_train.csv", "rb") as user_train_object:
            user_train_file = csv.reader(user_train_object)
            header = user_train_file.next()
            for line in user_train_file:
                user_train.append([line[0], float(line[2])])
        #predict on different conditions
        result = np.zeros(shape=(len(test_pair), 1))
        index = 0
        for item in test_pair:
            business_id = item[0]
            user_id = item[1]
            rating = 3.675
            if business_id in business_index and user_id in user_index:
                business_indexNumber = business_index.index(business_id)
                user_indexNumber = user_index.index(user_id)
                rating = np.dot(self.Theta[user_indexNumber,:], self.X[business_indexNumber,:].T)
            elif business_id in business_index:
                for row in business_train:
                    if row[0] == business_id:
                        rating = row[2]
                        break
            elif user_id in user_index:
                for row in user_train:
                    if row[0] == user_id:
                        rating = row[1]
                        break
            else:
                city = ""
                rating_list = []
                for row in business_test:
                    if row[0] == business_id:
                        city = row[1]
                        break
                for row in business_train:
                    if row[1] == city:
                        rating_list.append(row[2])
                if len(rating_list) > 80:
                    rating = np.mean(rating_list)
                else:
                    rating = 3.675
            result[index][0] = rating
            index = index + 1
        return result
        
