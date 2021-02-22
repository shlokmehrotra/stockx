from setup import mysql
#cursor = mysql.connection.cursor()

def new_user(user_data):
    print("New User: ")
    print(user_data)
    #check if username and/or email already exist before allowing for new user
    email = user_data["email"]
    username = user_data["username"]
    password = user_data["password"]
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO users(name, email, password) VALUES(%s, %s, %s);", (username, email, password))
    mysql.connection.commit()
    cursor.close()

    return ("user added")
def verify_user(user_data):
    print("Verify: ")
    print(user_data)
    email = user_data["email"]
    username = user_data["username"]
    password = user_data["password"]
    cursor = mysql.connection.cursor()
    results = cursor.execute("SELECT * FROM USERS WHERE name = %s, password = %s;", (username, password))
    mysql.connection.commit()
    cursor.close()
    if(results > 0):
        #success
        return("Success")