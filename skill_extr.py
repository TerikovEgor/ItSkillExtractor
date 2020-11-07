import pickle
import re
import dawg

splitter = re.compile('[ \.\?\!\:\;\-\"\'\,]')
 
all_skills_dawg = pickle.load(open('skill_dawg.pkl', 'rb'))

get_skill = lambda x: all_skills_dawg.keys(x)[0] if all_skills_dawg.keys(x) else None

def get_bigram(array):
    out = []
    to_del = []
    for i in range(len(array)):
        if len(array) == i+1:
            return list(set(out) - set(to_del))
        else:
            str1 = array[i] +'_'+ array[i+1]
            str2 = array[i] + array[i+1]
            
            res1 = get_skill(str1)
            res2 = get_skill(str2)
            
            if res1: 
                to_del+= [array[i]] + [array[i+1]]
                out +=[res1]
            elif res2: 
                to_del+= [array[i]] + [array[i+1]]
                out +=[res2]
            else: 
                out+= [array[i]] + [array[i+1]]
    return list(set(out) - set(to_del))
  
def extract_skill(string):
    return get_bigram(list(filter(None, [get_skill(j.lower()) for j in splitter.split(string) if j])))
