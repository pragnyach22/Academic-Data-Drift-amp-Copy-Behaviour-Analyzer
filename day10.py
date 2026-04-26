import random
import math
import numpy as np
import pandas as pd
import copy

def generate_students(n):
    data=[]
    for i in range(1,n+1):
        student={
            "id":i,
            "marks": random.randint(40,100),
            "attendance": random.randint(60,100),  
            "scores": [random.randint(10,25), random.randint(10,25)]     
        }   
        data.append(student) 
    return data

def mutate_data(data, roll_no):
    for i in range(len(data)):
        if i%(roll_no%3)==0:
            data[i]["marks"]+=math.sqrt(data[i]["marks"])
            data[i]["attendance"]-=5
            data[i]["scores"][0]+=2
    return data

def analyze_data(original,modified):
    orig_marks=np.array([s["marks"] for s in original])
    mod_marks=np.array([s["marks"] for s in modified])
    mean_orig=np.mean(orig_marks)
    mean_mod=np.mean(mod_marks)
    median=np.median(mod_marks)
    std_dev=np.std(mod_marks)
    manual_mean=sum(mod_marks)/len(mod_marks)
    drift=abs(mean_orig-mean_mod)
    normalized=(mod_marks-np.min(mod_marks))/(np.max(mod_marks)-np.min(mod_marks))
    return mean_mod,drift,std_dev,median,manual_mean,normalized

def classify(drift,std_dev,original,shallow):
    threshold=5
    if original!=shallow:
        return "copy Failure Detected"
    elif drift<2:
        return "Stable Data"
    elif drift<threshold:
        return "Minor Drift"
    else:
        return "Critical Drift"
    
roll_no=2

students=generate_students(random.randint(10,15))
original_df=pd.DataFrame(students)
shallow_copy=students.copy()
deep_copy=copy.deepcopy(students)
mutated_shallow=mutate_data(shallow_copy,roll_no)
mutated_deep=mutate_data(deep_copy,roll_no)
mean, drift, std_dev, median, manual_mean, normalized=analyze_data(students,mutated_deep)
result=classify(drift, std_dev, students, shallow_copy)
shallow_df=pd.DataFrame(mutated_shallow)
deep_df=pd.DataFrame(mutated_deep)

print("Original Data:")
print(original_df)
print("\nShallow Copy Mutated Data:")
print(shallow_df)
print("\nDeep Copy Mutated Data:")
print(deep_df)
print("Drift Value")
print(drift)
print("Tuple Output")
print((mean, drift, std_dev))
print("Classification Result:")
print(result)
print("manual mean")
print(manual_mean)
print("Normalizrd marks")
print(normalized)
