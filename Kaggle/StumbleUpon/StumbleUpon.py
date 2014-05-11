import numpy as np
import pandas as pd
from sklearn import linear_model as lm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
from sklearn import cross_validation as cv
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer

#WordNet stemming
class data_process:
    def __init__(self):
        self.wnl = WordNetLemmatizer()
    def __call__(self, doc):
        return [self.wnl.lemmatize(t) for t in word_tokenize(doc)] 

#get training and test data from file
def get_data(train_file, test_file):
    train_data = np.array(pd.read_table(train_file, delimiter="\t"))[:,(2, -1)]
    test_data = np.array(pd.read_table(test_file, delimiter="\t"))[:,(1, 2)]
    return train_data, test_data

#Cross validation to find the best model and vectorization method
def cross_validation(train_data):
    tfidf_vectorizer = TfidfVectorizer(tokenizer=data_process(), min_df=3, strip_accents='unicode', analyzer='word', ngram_range=(1, 2), use_idf=1, smooth_idf=1, norm='l1')
    classifier = lm.LogisticRegression(penalty='l2', dual=True)
    train_Y, train_data = train_data[:,1], train_data[:,0]
    score = []
    kf = cv.KFold(len(train_Y), n_folds=10, indices=False)
    for train, test in kf:
        x_train_cv, y_train_cv, x_test_cv, y_test_cv = train_data[train], train_Y[train], train_data[test], train_Y[test]
        x_train_cv = tfidf_vectorizer.fit_transform(x_train_cv)
        x_test_cv = tfidf_vectorizer.transform(x_test_cv)
        classifier.fit(x_train_cv, y_train_cv)
        prediction = classifier.predict_proba(x_test_cv)[:,1]
        fpr, tpr, thresholds = metrics.roc_curve(y_test_cv, prediction, pos_label=1)
        auc = metrics.auc(fpr, tpr)
        score.append(auc)
    print "10 Fold Cross Validation ROC: %f" % np.array(score).mean()
    return TfidfVectorizer(tokenizer=data_process(), min_df=3, strip_accents='unicode', analyzer='word', ngram_range=(1, 2), use_idf=1, smooth_idf=1, norm='l1'), lm.LogisticRegression(penalty='l2', dual=True)

#apply the best algorithms to the test set and output the result
def run(train_data, test_data):
    vectorizer, classifier = cross_validation(train_data)
    train_Y, train_data = train_data[:,1], train_data[:,0]
    urlid, test_data = test_data[:,0], test_data[:,1]
    train_data = vectorizer.fit_transform(train_data)
    test_data = vectorizer.transform(test_data)
    classifier.fit(train_data, train_Y)
    prediction_prob = classifier.predict_proba(test_data)[:,1]
    result = pd.DataFrame(np.column_stack((urlid, prediction_prob)), columns=['urlid', 'label'])
    result.to_csv("test.csv", index=False)

#main function
def main():
    train_file, test_file = "train.tsv", "test.tsv"
    train_data, test_data = get_data(train_file, test_file)
    run(train_data, test_data)

if __name__ == '__main__':
    main()
