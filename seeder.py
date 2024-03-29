from app.infrastructure.database.db import *

def get_intent_label_query():
    with open("./sql/intent_labels.sql") as file:
        query = text(file.read())
    file.close()
    return query

def get_response_query():
    with open("./sql/responses.sql") as file:
        query = text(file.read())
    file.close()
    return query

def get_user_query():
    with open("./sql/users.sql") as file:
        query = text(file.read())
    file.close()
    return query

if __name__ == "__main__":
    with engine.connect() as con:
        try:
            intent_label_query = get_intent_label_query()
            response_query = get_response_query()
            user_query = get_user_query()
            con.execute(intent_label_query)
            con.execute(response_query)
            con.execute(user_query)
            print("Intents, Admin user, and Responses is successfully loaded into the database")
        except:
            print("Intents, Admin user, and responses are already loaded.")
