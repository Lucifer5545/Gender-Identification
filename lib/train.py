import nltk
import utils


def train(train_file,test_file=None):
    data = utils.load_csv(train_file)
    feature_set = [(utils.feature_extract(i[0]),i[1]) for i in data]
    print 'Training'
    classifier = nltk.NaiveBayesClassifier.train(feature_set)
    utils.save_model(classifier)
    print 'Done Training'
    if test_file:
        data = utils.load_csv(test_file)
    test_feature_set = [(utils.feature_extract(i[0]),i[1]) for i in data]
    print 'Accuracy of model is {0}'.format(nltk.classify.accuracy(classifier,test_feature_set))
    
