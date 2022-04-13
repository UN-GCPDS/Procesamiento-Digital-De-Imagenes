"""Train siamese network

Usage:
    train.py [--epochs EPOCHS --batch_size BATCH_SIZE]

Options:
    --epochs EPOCHS             Number of epochs. [default: 10]
    --batch_size BATHC_SIZE     Batch size. [default: 32]

"""
from docopt import docopt


from tensorflow.keras.losses import BinaryCrossentropy
from tensorflow.keras.metrics import BinaryAccuracy
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.callbacks import ModelCheckpoint

import matplotlib.pyplot as plt 

from model import build_siamese_model
from dataset import get_data 


def main(epochs=10,batch_size=32):
    
    train,test = get_data()
    input_shape = train[0].shape[-3:]

    model = build_siamese_model(input_shape=input_shape)

    model.compile(loss=BinaryCrossentropy(),
                 optimizer=RMSprop(),
                 metrics=[BinaryAccuracy()])


    model_checkpoint_callback = ModelCheckpoint(
                                            filepath='model.h5',
                                            save_weights_only=False,
                                            monitor='val_binary_accuracy',
                                            mode='max',
                                            save_best_only=True)

    imagesA = train[0][:,0]
    imagesB = train[0][:,1]
    labels = train[1]
    history = model.fit((imagesA,imagesB),labels,
                        validation_split=0.2,
                        batch_size=batch_size,
                        epochs=epochs,
                        callbacks=[model_checkpoint_callback])


    imagesA = test[0][:,0]
    imagesB = test[0][:,1]
    labels = test[1]
    evaluate = model.evaluate((imagesA,imagesB),labels)

    loss = history.history['loss']
    binary_accuracy = history.history['binary_accuracy']

    val_loss = history.history['val_loss']
    val_binary_accuracy = history.history['val_binary_accuracy']

    plt.figure(figsize=(20,10))
    plt.suptitle(f'Binary accuracy on test: {evaluate[1]:0.2f}')
    plt.subplot(121)
    plt.plot(loss)
    plt.plot(val_loss)
    plt.legend(['loss','val loss'])

    plt.subplot(122)
    plt.plot(binary_accuracy)
    plt.plot(val_binary_accuracy)
    plt.legend(['binary accuracy','val binary accuracy'])
    plt.savefig('TrainingResults.png')
    plt.show()
    

if __name__ == "__main__":
    arguments = docopt(__doc__)
    epochs = int(arguments['--epochs'])
    batch_size = int(arguments['--batch_size'])
    main(epochs,batch_size)
