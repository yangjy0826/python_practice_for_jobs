import os
os.environ['KERAS_BACKEND'] = 'tensorflow'
import keras
from keras.datasets import cifar10
import pandas as pd
import densenet
print('DenseNet-Version: %s' % densenet.__version__)

# cifar 10 test acc = 0.8235 L=10 k=25
# model = densenet.DenseNet(input_shape=(32,32,3), nb_classes=10, depth=10, growth_rate=25,
#                           dropout_rate=0.1, bottleneck=False, compression=0.5)
# cifar 10 test acc = 0.8569 L=40 k=12
# model = densenet.DenseNet(input_shape=(32,32,3), nb_classes=10, depth=40, growth_rate=12,
                          # dropout_rate=0.2, bottleneck=False, compression=0.5)

model = densenet.DenseNet(input_shape=(32,32,3), nb_classes=10, depth=100, growth_rate=12,
                          dropout_rate=0.2, bottleneck=True, compression=0.5)
model.summary()
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
# print(y_test.shape)
# print( y_test.shape[0])
# print(y_test[0].shape)
# The data, shuffled and split between train and test sets:
x_train = x_train.astype('float32')/255
x_test = x_test.astype('float32')/255
# Convert class vectors to binary class matrices.
# y_train = keras.utils.to_categorical(y_train, 10)
# y_test = keras.utils.to_categorical(y_test, 10)
# initiate RMSprop optimizer
opt = keras.optimizers.sgd(lr=0.01, decay=1e-4)
model.compile(loss='mse', optimizer=opt, metrics=['accuracy'])

hist = model.fit(x_train, y_train, epochs=40, shuffle=True)
# model.save(model_name)
loss, accuracy = model.evaluate(x_test, y_test)
print(loss, accuracy)