import json

def handle_read():
    with open("db.json","r") as file:
       # print(file.readlines())
       return json.load(file)

def handle_create(single_todo):
    # step 1 real all todos
    data = handle_read()
    
    # step 2 add data to notes array
    data["notes"].append(single_todo)

    #step 3 write file
    with open("db.json","w") as file:
           # file.write(data)
           json.dump(data,file)

def handle_remove(index):
     data= handle_read()
     data["notes"].pop(index-1)     
     with open("db.json","w") as file :
          json.dump(data,file)      

def handle_update(id,body):
     data= handle_read()
     data["notes"][id-1]= body

     with open("db.json","w") as file:
          #file.write(data)
          json.dump(data,file)
      