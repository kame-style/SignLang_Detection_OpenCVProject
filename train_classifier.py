import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np


def data_length(lst):
    data_len_list=[]
    for item in lst:
        data_len_list.append(len(item)) 
    return data_len_list


def is_homogeneous(lst):
    if not lst:  # Empty list is homogeneous
        return True
    first_type = len(lst[0])
    return all(len(item) == first_type for item in lst)

data= pickle.load(open('./data.pickle', 'rb'))
labels= pickle.load(open('./lables.pickle', 'rb'))

print(is_homogeneous(data))
print(is_homogeneous(labels))
print(data_length(data))
print(data_length(labels))

data = np.asarray(data)
labels = np.asarray(labels)


x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)      ##stratify - split the data in same proportion of labels so we have same proportion of data for every class in train and test


model = RandomForestClassifier()
model.fit(x_train, y_train)

y_predict = model.predict(x_test)

score = accuracy_score(y_predict, y_test)

print('{}% of samples were classified correctly !'.format(score * 100))

# f = open('model.p', 'wb')
# pickle.dump({'model': model}, f)
# f.close()
