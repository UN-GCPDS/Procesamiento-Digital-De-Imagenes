from tensorflow.keras.models import load_model 
from model import uclidean_distance


from dataset import get_data 
train,test = get_data()

model = load_model('model.h5',custom_objects={'Cosine_Distance':uclidean_distance})

imagesA = test[0][:,0]
imagesB = test[0][:,1]
labels = test[1]
evaluate = model.evaluate((imagesA,imagesB),labels)