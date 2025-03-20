import jwt, datetime, os
from flask import Flask, request
from flask_mysqldb import MySQL

#make instance of flask and mysql db
server= Flask(__name__)
mysql = MySQL(server)

#configuration

server.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST")
server.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")
server.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD")
server.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")
server.config["MYSQL_PORT"] = os.environ.get("MYSQL_PORT")
# print(server.config["MYSQL_HOST"])


# login route
@server.route("/login", methods=["POST"])
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return {"message": "Could not verify"}, 401

    # check db for username and password
    cur = mysql.connection.cursor()
    res = cur.exeute(
        "SELECT * FROM user where email = %s", (auth.username)
    )

    if res > 0:
        user_row = cur.fetchone()
        email = user_row[1]
        password = user_row[2]

        if email != auth.username or password != auth.password:
            return {"message": "Could not verify"}, 401
        else:
            return createJWT(auth.username, os.environ.get("JWT_SECRET"), True)
        
    else:
        return {"message": "User not found"}, 401
    


# create JWT token
def createJWT(username, secret, is_admin):
    token = jwt.encode(
        {
            "user": username,
            "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=1),
            "lat" : datetime.datetime.utcnow(),
            "admin": is_admin,
        },
        secret,
        algorithm="HS256",
    )
    return {"token": token.decode("UTF-8")} 



if __name__ == "__main__":
    server.run(debug=True, host="0.0.0.0", port=5000)