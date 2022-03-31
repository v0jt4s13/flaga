import random
import pandas as pd
	
def random_question_from_csv(): 

  # Dane
  df = pd.read_csv('data/sample.csv')
    
  # Losowanie pytania
  i = random.choice(range(len(df)))
  this_question = df.loc[i, :]
  question = this_question['question']
  answer = this_question['answer']
  
  return question, answer

#print(random_question_from_csv())