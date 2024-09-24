from fastapi import FastAPI, Path
from fastapi.responses import FileResponse

app = FastAPI()

students = {
    1 : {
        "name" : "abc",
        "class" : "3"
    }
}

# ********** basic one ***********
@app.get("/")
def index():
    return {"name" : "new name"}

# ********** path parameter : getting student details by specifying id ***********
@app.get("/get-student/{student_id}")
def get_student(student_id : int): # = Path(None,description="id of student",gt=0)):
    return students[student_id]

# ********** query parameter  ***********
@app.get("/get-by-name")
def get_student(name : str):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data" : "data not found"}

# ********** combining path and query parameter  ***********
@app.get("/get-combined/{student_id}")
def get_student(name : str,student_id : int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data" : "data not found"}

# ********** getting an html page ***********
@app.get("/htmlpage",response_class=FileResponse)
def index():
    return "samplehtml.html"