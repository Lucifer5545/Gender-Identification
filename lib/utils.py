import cPickle
import os 
import sys
import csv


def save_model(classifier):
    """
    Saves the previously saved model to a file for later use
    :input:
    classifier: previously trained classifier
    """
    if not os.path.exists('model/'):
        os.mkdir('model')
    filename = 'model/classifier.pkl'
    with open(filename,'wb') as fp:
        cPickle.dump(classifier,fp)
    print 'Model save in Location{0}'.format(filename)


def load_model():
    """
    loads the previously saved model
    :return:Classifier model if present otherwise raise an IOError
    """
    try:
        with open('model/classifier.pkl','rb') as fp:
            classifier = cPickle.load(fp)
    except IOError:
        print 'Saved Model Does not exists'
        sys.exit()
    else:
        return classifier

def preprocess(name):
    """
    Preprocess the input name to extract first name without any Mr|Mrs|Smt|Dr|Er
    :input:
    name: Name input by the user
    :return:
    processed name
    """
    first_name = name.split()[0]
    if '.' in first_name:
        first_name = first_name.split('.')[1]
    return first_name

def feature_extract(x):
    """
    Extract the features from the input name for use with classifier
    :input:
    x:Data to extract features
    :return:
    features:Dictionary of extracted features
    """
    features ={}
    features['len'] = len(x)
    features['first_char'] = x[0]
    features['last_char'] = x[-1]
    features['s_last_char'] = x[-2:]
    return features

def load_csv(file_name):
    """
    Extract data from csv file
    :input:
    file_name: Csv File 
    :return:
    data:list containing extracted data
    """
    data = []
    try:
        with open(train_file,'rb') as fp:
            r = scv.reader(fp)
            for i in r:
                data.append(i)
    except IOError:
        print ' Train file does not exists'
        sys.exit()
    else:
        return data
