# the informal evaluation: read from opt of inference script and calculate acc
# jxu

import json
# from compute_eer import compute_eer
# from sklearn.metrics import top_k_accuracy_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import recall_score
# import numpy as np

path_infer = './data/test_infer.json'

with open(path_infer, 'r') as handle:
    data = [json.loads(line) for line in handle]

    labels = ['s1', 's2', 's3']

    y_true = []
    y_pred = []

    for d in data:
        y_true.append(d['label'])
        y_pred.append(d['infer'])

    # print(y_true)
    # print(y_pred)

    # acc
    acc = accuracy_score(y_true, y_pred)
    print(f'accuracy: {acc}')

    # F1 score
    f1_macro = f1_score(y_true, y_pred, average='macro')
    print(f'macro f1 score: {f1_macro}')

    # top 1 acc
    # top_1_acc = top_k_accuracy_score(y_true, y_score, k=1)
    # print(f'top 1 accuracy: {top_1_acc}')

    print()
    print('======== per class ========')
    print()

    print(labels)

    # F1 score per class
    f1_per_class = f1_score(y_true, y_pred, labels=labels, average=None)
    print(f'f1 score per class: {f1_per_class}')

    # recall per class (is the same as accuracy per class in multi-classifation scenerio)
    recall = recall_score(y_true, y_pred, labels=labels, average=None)
    print(f'recall score/acc per class: {recall}')

    # acc per class
    # matrix = confusion_matrix(y_true, y_pred)
    # acc_per_class = matrix.diagonal()/matrix.sum(axis=1)
    # print(f'acc per class: {acc_per_class}')
