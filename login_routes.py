from setup import mysql
#cursor = mysql.connection.cursor()

def new_user(user_data):
    errormessage = ""
    print("New User: ")
    print(user_data)
    email = str(user_data["email"])
    username = str(user_data["username"])
    password = str(user_data["password"])
    #check if username and/or email already exist before allowing for new user
    cursor = mysql.connect.cursor()
    results = cursor.execute("SELECT * FROM users WHERE name = %s", [username])
    if results > 0:
        print("username taken")
        errormessage += "username" #username taken
    results = cursor.execute("SELECT * FROM users WHERE email = %s", [email])
    if results > 0: 
        print("email taken")
        errormessage += "email" #email taken

    if errormessage == "":
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users(name, email, password) VALUES(%s, %s, %s);", (username, email, password))
        mysql.connection.commit()
        cursor.close()

        return("success")
    else:
        return(errormessage)
def verify_user(user_data):
    print("Verify: ")
    print(user_data)
    email = user_data["email"]
    username = user_data["username"]
    password = user_data["password"]
    cursor = mysql.connection.cursor()
    results = cursor.execute("SELECT * FROM users WHERE name = %s, password = %s;", (username, password))
    mysql.connection.commit()
    cursor.close()
    if(results > 0):
        #success
        return("Success")