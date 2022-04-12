from tensorflow.keras.models import load_model 
from model import uclidean_distance

model = load_model('model.h5',custom_objects={'Cosine_Distance':uclidean_distance})

