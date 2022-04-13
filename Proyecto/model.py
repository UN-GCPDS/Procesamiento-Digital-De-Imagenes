from tensorflow.keras.models import Model
from tensorflow.keras.layers import (Input,
                                    Conv2D,
                                    Dense,
                                    Dropout,
                                    Flatten,
                                    AveragePooling2D,
                                    Rescaling,
                                    Lambda,
                                    BatchNormalization)

import tensorflow.keras.backend as K

def build_sister_model(input_shape,embeddingDim):
    """Return sister model
    """
    input = Input(shape=input_shape)
    x = Rescaling(scale=1./255.)(input)
    x = BatchNormalization()(x)
    x = Conv2D(4,(5,5),activation='relu')(x)
    x = AveragePooling2D(pool_size=(2,2))(x)


    x = Conv2D(16,(5,5),activation='relu')(x)
    x = AveragePooling2D(pool_size=(2,2))(x)
    x = BatchNormalization()(x)

    x = Flatten()(x)
    x = BatchNormalization()(x)
    outputs = Dense(embeddingDim)(x)

    model = Model(input,outputs,name='SharedNetwork')

    return model 


def build_siamese_model(input_shape=(28,28,1),embeddingDim=10):
    """Return siamese model
    """
    imgA = Input(shape=input_shape,name='InputA')
    imgB = Input(shape=input_shape,name='InputB')
    featureExtractor = build_sister_model(input_shape,embeddingDim)
    featA = featureExtractor(imgA)
    featB = featureExtractor(imgB)

    distance = Lambda(uclidean_distance,name='Cosine_Distance')([featA,featB])
    x = BatchNormalization()(distance)
    outputs = Dense(1,activation='sigmoid',name='Output')(x)
    model = Model(inputs=[imgA,imgB],outputs=outputs)

    return model 


def uclidean_distance(vectors):
    (featA,featB) = vectors
    sumSquared = K.sum(K.square(featA-featB),axis=1,keepdims=True)
    return K.sqrt(K.maximum(sumSquared,K.epsilon()))


if __name__ == "__main__":
    from tensorflow.keras.utils import plot_model
    model = build_siamese_model()
    model.summary()
    plot_model(model,to_file='model.png',expand_nested=True,show_shapes=True)