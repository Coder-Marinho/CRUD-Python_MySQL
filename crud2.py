import mysql.connector

# Database connect
#conn = mysql.connector.connect(
#    host=" localhost",       # ou IP do servidor remoto
#    user="desenvolvedores",
#    password="pai de muitos",
#    database="gamification_db"
#)

#cursor = conn.cursor()

credentials = {"host":"",
        "user": "",
        "password": "",
        "database": ""
        }

#MAIN LOOP
def mainLoop():
    for key in credentials:
        credentials[key] = input(f"Insert the {key}: ")

mainLoop()

# Database connect
databaseConn = mysql.connector.connect(**credentials)


cursor = databaseConn.cursor()


