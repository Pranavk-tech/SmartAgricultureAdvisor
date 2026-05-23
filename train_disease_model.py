from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense

train=ImageDataGenerator(
rescale=1./255
)

dataset=train.flow_from_directory(
"disease_dataset",
target_size=(128,128),
batch_size=32
)

model=Sequential()

model.add(
Conv2D(
32,
(3,3),
activation="relu",
input_shape=(128,128,3)
)
)

model.add(
MaxPooling2D()
)

model.add(
Flatten()
)

model.add(
Dense(
128,
activation="relu"
)
)

model.add(
Dense(
dataset.num_classes,
activation="softmax"
)
)

model.compile(

optimizer="adam",
loss="categorical_crossentropy",
metrics=["accuracy"]

)

model.fit(
dataset,
epochs=5
)

model.save(
"models/disease_model.h5"
)

print(
"Disease model trained"
)