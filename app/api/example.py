# from flask import Blueprint, jsonify, session, request
# from app.models import db, < Model Name > 
# from app.forms import < Formm Name >

# <Route Name>_routes = Blueprint("<Route Name>", __name__)

# #---------- GET ROUTES ----------
# @<Route Name>.route("/")
# def get_all_<Model Name>s(): 
#     <Model Name> = <Model Name>.query.all()

#     return {"data": response, "message":"Success"},200


# @<Route Name>.route("/<int:id>")
# def get_single_<Model Name>(id):
#     <Model Name> = <Model Name>.query.get(id)
#     if <Model Name> is None:
#         return {"error": "<Model Name> Not Found"},404
#     response = <Model Name> .to_dict()
    
#     return {"data": response, "message":"Success"},200
    
# #---------- POST ROUTES ----------
# @<Route Name>.route("/",methods=["POST"])
# def post_new_<Model Name>():
    
#     form = <Model Name>Form()
#     form["csrf_token"].data = request.cookies["csrf_token"]
    
#     if form.validate_on_submit():
#         data = form.data
#         new_<Model Name> = <Model Name>(
#              Whatever you are adding
#         )        
        
#         db.session.add(new_<Model Name>)
#         db.session.commit()
#         return {"message":"success","data":new_<Model Name>.to_dict()},200
    
#     if form.errors:
#        print("There were some form errors", form.errors)
#        return {"errors": form.errors}, 400, {"Content-Type": "application/json"}

# #---------- PUT/UPDATE ROUTES ----------

# #---------- DELETE ROUTES ----------
# @<Route Name>.route("/<int:id>",methods=["DELETE"])
# def delete_single_<Model Name>(id):
#     deleted_<Model Name> = < Model Name >.query.get(id)
    
#     if deleted_< Model Name > is None:
#         return{"errors":"< Model Name > could not be found"},404
    
#     db.session.delete(deleted_< Model Name >)
#     db.session.commit()
#     return {"message":"< Model Name > Successfully delelted"}

