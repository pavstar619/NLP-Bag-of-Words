# import statments
import numpy
import re

'''
Tokenize each the sentences, example
Input : "John likes to watch movies. Mary likes movies too"
Ouput : "John","likes","to","watch","movies","Mary","likes","movies","too"
'''
# STEP 2: APPLY TOKENIZE TO ALL SETENCES
def tokenize(sentences):
    words = []
    for sentence in sentences:
        w = word_extraction(sentence)
        words.extend(w)
        
    words = sorted(list(set(words)))
    return words

# STEP 1: REMOVE STOP WORDS FROM SETENCE
def word_extraction(sentence):
    ignore = ['a', "the", "is"]
    words = re.sub("[^\w]", " ",  sentence).split()
    cleaned_text = [w.lower() for w in words if w not in ignore]
    return cleaned_text    

# STEP 3: BUILD VOCAB AND GEN VECTORS
def generate_bow(allsentences):    
    vocab = tokenize(allsentences)
    print("Word List for Document \n{0} \n".format(vocab))

    for sentence in allsentences:
        words = word_extraction(sentence)
        bag_vector = numpy.zeros(len(vocab))
        for w in words:
            for i,word in enumerate(vocab):
                if word == w: 
                    bag_vector[i] += 1
                    
        print("{0} \n{1}\n".format(sentence,numpy.array(bag_vector)))


""" allsentences = ["Joe waited for the train", "The train was late", "Mary and Samantha took the bus", 
            "I looked for Mary and Samantha at the bus station", 
            "Mary and Samantha arrived at the bus station early but waited until noon for the bus"] """

""" INPUT ANY SENTENCE """
 # creating an empty list 
lst = [] 
  
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
  
# iterating till the range 
for i in range(0, n): 
    ele = input()
  
    lst.append(ele) # adding the element 
      
#print(lst) 
allsentences = lst

generate_bow(allsentences)