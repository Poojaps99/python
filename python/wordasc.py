 
def sortedSentence(Sentence): 
      
     
    words = Sentence.split(" ") 
      
    # Sorting the words 
    words.sort() 
      
    # Making new Sentence by  
    # joining the sorted words 
    newSentence = " ".join(words) 
      
    # Return newSentence 
    return newSentence 
  
# Driver's Code 
  
Sentence = "to learn programming refer geeksforgeeks"
# Print the sortedSentence 
print(sortedSentence(Sentence)) 
  
Sentence = "geeks for geeks"
# Print the sortedSentence 
print(sortedSentence(Sentence)) 

