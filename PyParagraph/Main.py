
# coding: utf-8

# In[10]:


import os
import re


# In[11]:


hitchhiker_snow = os.path.join("raw_data","HitchhikersSnow.txt")


# In[17]:


with open(hitchhiker_snow, 'r') as snowdoc:
    snowdoc=snowdoc.read()
    print(snowdoc)


# In[19]:


# count instances of sentences
sentence_count= snowdoc.count(".")+snowdoc.count("!")+snowdoc.count("?")
print(sentence_count)


# In[23]:


# break up words and remove non-letter characters
paragraph= re.split(" ",snowdoc)
print(paragraph)
# count number of words
word_count= len(paragraph)

# count number of letters in all words
word_len= 0
for word in paragraph:
    word_len= word_len + len(word)
    
print(word_count)
print(word_len)


# In[27]:


sentence_end= ("?","!",".")
punctuation=(",","\"","\'","/",";","-","&")
word_len= 0
word_count= 0
sentence_count= 0

for character in snowdoc:
    if character==" " and word_count !=0: # end of word
        word_count= wordcount+1

    elif character in sentence_end: # end of sentence
        sentence_count= sentence_count+1
        word_count= wordcount+1

    elif character in sentence_end != true:
        if character in puncuation:
            next
        else:
            word_len = word_len+1
        
    


# In[24]:


print("Approximate Word Count: "+ str(word_count))
print("Approximate Sentence Count: "+ str(sentence_count))
print("Average Letter Count: "+ str(word_len/word_count))
print("Average Sentence Length: "+ str(word_count/sentence_count))


# In[ ]:


hitchhiker_snow.close()

