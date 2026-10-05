import array as arr
students_names=["Mercy", "Sharon", "Janet", "Shellah", "Crispus"]
students_ages=arr.array('i',[20,21,22,23,24])
print (students_names)
print (students_ages)
#
students=[
    ["Mercy", 20],
    ["Sharon", 21],
    ["Janet", 22],
    ["Shellah", 23],
    ["Crispus", 24]
]
print(students)

students_3D=[
    [   
        ["Mercy", 20],
        ["Sharon", 21]
    ],
    [ 
        ["Janet", 22],
        ["Shellah", 23],
        ["Crispus", 24]
    ]
]
print(students_3D)
#ADD
students.append(["John", 25])
#EDIT Mercy
students[0]=["Mercy", 21]
#DELETE Sharon
del students[1]
print(students)