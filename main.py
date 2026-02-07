from fastapi import FastAPI
import json

app = FastAPI()

global data

with open('./data.json') as f:
    data = json.load(f)


@app.get('/')
def hello_world():
    return 'Hello, World!'

@app.get('/students')
async def get_students(pref=None):
    if pref:
        filtered_students = []
        for student in data:
            if student['pref'] == pref: 
              filtered_students.append(student) 
        return filtered_students
    return data

@app.get('/students/{id}')
async def get_student(id):
  for student in data: 
    if student['id'] == id: 
      return student
    

@app.get("/stats")
def stats():
    from collections import Counter   
    
    meal_counts = Counter(student["pref"] for student in data if "pref" in student)
    programme_counts = Counter(student["programme"] for student in data if "programme" in student)
    
    lines = []
    
    for meal, count in sorted(meal_counts.items()):
        lines.append(f"{meal}: {count},")
    
    for prog, count in sorted(programme_counts.items()):
        lines.append(f"{prog}: {count},")
    
    result = " ".join(lines).rstrip(",")
    
    return result


# Exercise 2 - Math operation routes
@app.get("/add/{a}/{b}")
def add(a: float, b: float):
    return {"result": a + b}

@app.get("/subtract/{a}/{b}")
def subtract(a: float, b: float):
    return {"result": a - b}

@app.get("/multiply/{a}/{b}")
def multiply(a: float, b: float):
    return {"result": a * b}

@app.get("/divide/{a}/{b}")
def divide(a: float, b: float):
    if b == 0:
        return {"error": "Division by zero is not allowed"}
    return {"result": a / b}