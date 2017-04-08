import argparse
from lib import utils,train


def identify(name):
    classifier = utils.load_model()
    name = utils.preprocess(name)
    print classifier.classify(utils.feature_extract(name))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n','--name',help="Name to be identified")
    parser.add_argument('-t','--train',help="Train new Model",action="store_true")
    parser.add_argument('-trin','--train-file',help="Training file in csv format containing names and gender")
    parser.add_argument('-tein','--test-file', help="test file to check accuracy of trained model")
    args = parser.parse_args()
    if args.train:
        train.train(args.tin,args.tein)
    else:
        identify(args.name)

main()