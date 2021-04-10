from nltk import NaiveBayesClassifier as nbc
from pythainlp.tokenize import word_tokenize
import codecs
from itertools import chain


# pos.txt
with codecs.open('NoomFuuProject/Sentiment/pos.txt', 'r', "utf-8") as f:
  lines = f.readlines()
listpos=[e.strip() for e in lines]
del lines
f.close() # ปิดไฟล์
# neg.txt
with codecs.open('NoomFuuProject/Sentiment/neg.txt', 'r', "utf-8") as f:
  lines = f.readlines()
listneg=[e.strip() for e in lines]
del lines
f.close() # ปิดไฟล์


pos1=['pos']*len(listpos)
neg1=['neg']*len(listneg)
training_data = list(zip(listpos,pos1)) + list(zip(listneg,neg1)) 

vocabulary = set(chain(*[word_tokenize(i[0].lower()) for i in training_data]))
feature_set = [({i:(i in word_tokenize(sentence.lower())) for i in vocabulary},tag) for sentence, tag in training_data]

classifier = nbc.train(feature_set)

print('start')

def useSentiment(Message):
  while True:
      # test_sentence = input('\nข้อความ : ')
      featurized_test_sentence = {i:(i in word_tokenize(Message.lower())) for i in vocabulary}
      print("test_sent:",Message)
      print("tag:",classifier.classify(featurized_test_sentence)) # ใช้โมเดลที่ train ประมวลผล
      break

while True:
  Message = input('\nข้อความ : ')
  useSentiment(Message)
