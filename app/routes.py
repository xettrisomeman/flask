
from app import app #__init__.py
from flask import render_template , request , json , Response



courseData = [{"courseID":"1111",
    "title":"PHP 111",
    "description":"Intro to PHP",
    "credits":"3","term":"Fall, Spring"}, 
    {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":"4","term":"Spring"},
     {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":"3","term":"Fall"}, 
     {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":"3","term":"Fall, Spring"}, 
     {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":"4","term":"Fall"}]


@app.route('/')
def hello_world():
    return "<h1>Hello , World!</h1>"


@app.route('/index')
def index():
    return render_template('index.htm',index=True)


@app.route('/courses/')
@app.route('/courses/<term>')
def courses(term="Spring 2019"):
    
    return render_template('courses.htm',courseData=courseData,courses=True , term=term)


@app.route('/register')
def register():
    return render_template('register.htm',register=True)


@app.route('/login')
def login():
    return render_template('login.htm',login=True)


@app.route('/enrollment', methods=["GET" , "POST"])
def enroll():
    id = request.form.get('courseID')
    title = request.form.get('title')
    term = request.form.get('term')

    return render_template('enroll.htm',  data={"id":id, "title":title , "term":term})


@app.route('/api/')
@app.route('/api/<idx>')
def apifunc(idx=None):
    if(idx==None):
        jdata = courseData
    else:
        jdata = courseData[int(idx)]

    return Response(json.dumps(jdata) , content_type="application/json" ) #it takes six parameters , 

#json dumps -> returns a string representing a json object from an object.

