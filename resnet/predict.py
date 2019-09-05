from keras.models import load_model
from resnet import train
from keras.utils import np_utils

import cv2
import time

X_test, y_test, file_names, category_names = train.load_test_data("../test/")
y_test = np_utils.to_categorical(y_test, 11)
model = load_model('../MCD_ResNet_model')

predict_ans = {}
for i in range(len(file_names)):
	category_predict = model.predict(X_test[i].reshape((1, 100, 100, 1))).argmax()
	category_true = y_test[i].argmax()

	if category_predict != category_true:
		predict_ans[file_names[i]] = category_names[category_predict]
		cv2.imwrite('./true/' + file_names[i] + '.jpg', X_test[i].reshape(100, 100))
		time.sleep(2)
	else:
		cv2.imwrite("./false/" + file_names[i] + '.jpg', X_test[i].reshape(100, 100))
		time.sleep(2)

print(len(y_test))
print(len(predict_ans))

with open('../predict.txt', 'w') as f:
	f.write('True_answer\tPredict_answer\n')
	for key, value in predict_ans.items():
		f.write(key + '\t' + value + '\n')
