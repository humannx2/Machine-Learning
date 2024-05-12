import numpy as np
import pandas as pd

data=pd.read_csv("C:/Users/adiva/OneDrive/Documents/Finding S Algo.csv")
# print(data)

attributes=np.array(data)[:,:-1] #-1 removes the headings of the labels
# print(attributes)
target=np.array(data)[:,-1]
# print(target)

def train(rows, target):
    for i, value in enumerate(target):
        # print(i,value)
        if value == "Yes":
            specific_hypo=rows[i].copy() #it is the array of the attributes of the first positive target, in this case the first row
            # print(specific_hypo)
            break

    for i,value in enumerate(rows):
        if target[i]=="Yes":
            for x in range (len(specific_hypo)):
                # print(value) #value is an array of attributes calculated above
                # print(value[x])
                if value[x]!=specific_hypo[x]:
                    specific_hypo[x]="?"
                else:
                    pass
    return specific_hypo

print("The General Hypothesis is",train(attributes,target))