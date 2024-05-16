# from app.models import db,,<Seed Model> environment, SCHEMA
# from sqlalchemy.sql import text
# 
# def seed_<Seed Data Name>():
#     [db.session.add(cereal) for cereal in cereal_list]
#     db.session.commit()
    
    


# def undo_<Seed Data Name> ():
#     if environment == "production":
#         db.session.execute(f"TRUNCATE table {SCHEMA}.<Seed Data Name> RESTART IDENTITY CASCADE;")
#     else:
#         db.session.execute(text("DELETE FROM <Seed Data Name>"))
        
#     db.session.commit()
    
