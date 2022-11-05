from deepface import DeepFace
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf



def returnAvatar(base_image):
  img = tf.image.resize(base_image, (224, 224))
  
  model = tf.keras.models.load_model('Models/HairColorModel')
  color = model.predict(np.array([img]))
  if color[0]>.5: # Blond
    hair = 'Blond'
  else:
    hair = 'Black'

  deepface_obj = DeepFace.analyze(img_path=np.array(img), enforce_detection=False)
  gender = deepface_obj['gender']
  if gender == 'Man':
    gender = 'Short'
  else:
    gender = 'Long'
  if deepface_obj['race']['white'] > deepface_obj['race']['black']:
    race = 'White'
  else:
    race = 'Black'

  avatar = mpimg.imread(str(race)+str(gender)+str(hair)+'.png')
  print(str(race)+str(gender)+str(hair)+'.png')
  return avatar