# Sign2Sound
A sign language recognition system with the ability to get sentence from corpus engine and give audio output.
Keep all the files in same folder and create your own datasets or download the datasets.

Software requirements:
  Jupyter Notebook Code editor,
  Mini-Conda,

Dependencies:
  Python 3.12.8,
  Nvidia CUDA v12.6 GPU,
  Nvidia CUDnn v9.6.0,
  PyTorch v2.5.1 

Libraries/packages:
  PyTorch v2.5.1
  Py-CUDA v12.4.1
  cv2
  os
  numpy
  MediaPipe

# Steps
1. Make sure to download all the files(num.ipynb and added.ipynb is optional)
2. Once done, the train_model.ipynb is loaded with LSTM model with 6 layer, change it or use it according to your needs. But it is recommended to use CNN in future developments or better ones.
3. Open main7.ipynb and run it.
4. In case you to spice up things by adding one more functionality, download the files which is mentioned in step1 as optional.
5. This timme, run added.ipynb, run it and select a respective number 1 or 2 to open numeric calc or sign detector.
6. Boom, enjoy the working.

# NOTE
The current code doesn't have any trained model, so make sure you create your own dataset or download it from various websites like Kaggle, etc., If incase you want to create dataset follow the below steps.
1. Open data_collection.ipynb.
2. There you will find a SIGN variable which u can change the values of it to create more signs.
3. The default is set to 30 frames and colection, meaning you need to show same sign 30 times for few seconds repeatedely. (Painfull process, but works better than already existing dataset).
4. Then its time to preprocess the image to numeric ones, use the preprocess_data.ipynb to preprocess the data.
5. After that, train the model using train_model.ipynb.
6. After training the model, import it in the main7.ipynb. (make sure the model name you exported in train_model.ipynb is matched up)
7. That's it, enjoy!!!
8. BTW, the model can frame sentence and also give audio output.
9. Coming to sentence, in corpus_engine.py, you will fine a variable called sentences, which you can use to add more sentences.

# Working
1. When you show a sign, the model will get the word for that sign and if the corpus engine has a word of that sign in sentence, it will display the entire sentence.
2. Didn't get it? Example below.
3. Show a sign "Great"
4. Scans through corpus and finds "Great work well done" from sentence.
5. Throws the full sentence in output.
6. If incase there are 2 sentence starting with similar word eg.,"Great work well done", "Great wall of China".
7. Then the model will ask for second sign like you should either show the sign "work" or "wall", then it will display entire sentence if the 3rd word in sentence is not same. If its same, the same loop is done.

#Negletable notes
1. I would like to see people use my project to make addons instead of using the same for the final project.
