import array as arr
students_names=["Mercy", "Sharon", "Janet", "Shellah", "Crispus"]
students_ages=arr.array('i',[20,21,22,23,24])
students_data={ 
    "student1":{
        "name":"Mercy",
        "age":20,
        "date_of_birth":"2006-01-15",
        "location":"Ruiru",
        "admission_number":"3148"
    },
    "student2":{    
        "name":"Sharon",
        "age":21,
        "date_of_birth":"2005-03-20",
        "location":"Kihunguro",
        "admission_number":"3145"
    },
    "student3":{    
        "name":"Janet",
        "age":22,
        "date_of_birth":"2004-07-10",
        "location":"Agape",
        "admission_number":"3120"
    },
    "student4":{    
        "name":"Shellah",
        "age":23,
        "date_of_birth":"2003-05-25",
        "location":"Rainbow",
        "admission_number":"3150"
    },
    "student5":{    
        "name":"Crispus",
        "age":24,
        "date_of_birth":"2002-09-12",
        "location":"Roysambu",
        "admission_number":"3100"
    }
}
print(students_data)
print(students_data["student1"])
print(students_data["student2"])
print(students_data["student4"])
print(students_data["student3"])
print(students_data["student5"])










