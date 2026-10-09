students={
    101:{"Name":"Diya","Scores":[23,54,64]},
    102:{"Name":"Soha","Scores":[54,38,89]},
    103:{"Name":"Rohan","Scores":[65,56,77]}
}
print(students)

#calculate average score and flag pass/fail
for sid, details in students.items():
    avg=sum(details["Scores"]) / len(details["Scores"]) #avg using
    details["Average"]=avg
    details["Passed"]=avg>=30   #Boolean flag

#print name of students who passed
print("Student who passed:")
for sid,details in students.items():
    if details["Passed"]:
        print(details["Name"])    