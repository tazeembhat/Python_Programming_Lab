# Python script to check whether a given key already exists in a dictionary
dict1 = {"Name": "Tazeem", "RollNo": 17, "Sem": "5th"}
key = input("Enter the key ")
if key in dict1:
    print("Key already exist.")
else:
    print("Key does not exist.")
