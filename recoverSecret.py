
# STILL WORKING

from collections import OrderedDict
def recoverSecret1(t):
    d = {
        t[0][0]: {min: 1000, max: 1000},
        t[0][1]: {min: 2000, max: 2000},
        t[0][2]: {min: 3000, max: 3000},
    }
    #loop over remaining triplets
    for i in range(1,len(t)):
        # loop over each el in triplet
        for j in range(3):
            # if not found, add to unknown before
            
            # if el is found in d
            #take all unknown before & set max to found min -1 
            # take all unknown after & set min to found max + 1
            





import re

def recoverSecret1(triplets):
    secret = "".join(triplets[0]) 
    
    
    for i in range(1,len(triplets)): 
        secret = re.sub(triplets[i][0] + triplets[i][2] ,"".join(triplets[i]), secret)
        if secret[0] == triplets[i][1]:
            secret = triplets[i][0] + secret
        if secret[0] == triplets[i][2]:
            secret = triplets[i][0:2] + secret
        if secret[-1] == triplets[i][1]:
            secret += triplets[i][2]
        if secret[-1] == triplets[i][0]:
            secret +=  triplets[i][1:2] 
    return secret
    
triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]
triplets2 = [
  ['a','d','e'],
  ['b','c','e'],
  ['a','c','d'],
  ['a','b','d']
]
print(recoverSecret1(triplets2))