from flask import Flask,request ,render_template
from utility import handle_read , handle_create , handle_remove,handle_update

app=Flask(__name__)

@app.route("/create",methods=["POST"])
def create_todo():
    # handle_create()
    body= request.json
    handle_create(body)
    
    return "todo create success"

@app.route("/read",methods=["GET"])
def read_todo():
    data= handle_read()
    return {"message":"todo read success","result":data["notes"]}

@app.route("/modify/<int:id>",methods=["PUT"])
def update_todo(id):
    length= len(handle_read()["notes"])
    if id > length:
        return "invalid",400
    
    body=request.json
    handle_update(id,body)
    return "todo update success"

@app.route("/remove/<int:kahipan>",methods=["DELETE"])
def delete_todo(kahipan):
    length= len(handle_read()["notes"])
    if kahipan > length:
        return "invalid",400

    handle_remove(kahipan)
    return "todo delete success"
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)