import numpy as np
import CollaborativeFiltering as CF
import csv

def read_data(input_file):
    index = []
    for line in input_file:
        index.append(line.strip('\n'))
    return index

def make_prediction(business_index_file, user_index_file, rating_file, test_file):
    #read file
    business_index = read_data(business_index_file)
    user_index = read_data(user_index_file)
    rating_matrix = np.genfromtxt(rating_file, delimiter = ',', dtype = int)
    test_pair = np.genfromtxt(test_file, delimiter = ',', dtype = str)[1:]
    review_id = test_pair[:,2]
    test_pair = test_pair[:,:2] 
    print "start training"
    cf = CF.CF()
    cf.fit(rating_matrix)
    print "finish training!"
    result = cf.predict(test_pair, business_index, user_index)
    print "finish predicting and begin output the result"
    header = ["review_id", "Stars"]
    with open("submission.csv", "wb") as submission_object:
        submission_writer = csv.writer(submission_object)
        rowId = 0
        submission_writer.writerow(header)
        for item in result:
            predict_rating = item[0]
            if predict_rating > 5.0:
                predict_rating = 5.0
            if predict_rating < 1.0:
                predict_rating = 1.0
            submission_writer.writerow([review_id[rowId], predict_rating])
            rowId = rowId + 1
    ##np.savetxt('submission.csv', result, delimiter = ',', fmt = '%f')
    
def main():
    business_index_file = open("business_index.txt", "r")
    user_index_file = open("user_index.txt", "r")
    rating_file = open("rating_matrix.csv", "r")
    test_file = open("review_test.csv", "r")
    make_prediction(business_index_file, user_index_file, rating_file, test_file)
    business_index_file.close()
    user_index_file.close()
    rating_file.close()
    test_file.close()


if __name__ == '__main__':
    main()
