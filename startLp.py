from localpaste import app_global
import argparse
import os

if __name__ == "__main__":

    # Parse the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", help="the db file", type=str)
    parser.add_argument("--port", help="port: default=5000",
                        type=int, default=5000)
    arg = parser.parse_args()

    # print(arg.db)
    if arg.db and arg.db.endswith(".db"):
        print("swithing db to", arg.db)
        if os.path.exists(arg.db):
            print("file exists")
            app_global.config["DB_FILE"] = arg.db
            app_global.getDb()
        print(app_global.config)

    from localpaste.main import startServer
    startServer(port=arg.port)
