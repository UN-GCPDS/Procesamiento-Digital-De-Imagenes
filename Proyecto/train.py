from tensorflow.keras.losses import BinaryCrossentropy
from tensorflow.keras.metrics import BinaryAccuracy
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint

from model import build_siamese_model
from dataset import get_data 


def main():
    model = build_siamese_model(input_shape=(28,28,1))

    
    train,test = get_data()

    model.compile(loss=BinaryCrossentropy(),
                 optimizer=Adam(),
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
                        batch_size=1,
                        epochs=10,
                        callbacks=[model_checkpoint_callback])


    imagesA = test[0][:,0]
    imagesB = test[0][:,1]
    labels = test[1]
    evaluate = model.evaluate((imagesA,imagesB),labels)


                

if __name__ == "__main__":
    main()
