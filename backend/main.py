import uvicorn
import argparse

parser = argparse.ArgumentParser(
    prog="main",
    description="Launches the backend server for the project",
)
parser.add_argument("-n", "--hostname", help="hostname of the server",
                    default="0.0.0.0")
parser.add_argument("-p", "--port", help="port number of the server",
                    default="8000", type=int)
parser.add_argument("-r", "--release", help="set flag if running in prod",
                    action="store_true")
args = parser.parse_args()

hostname = args.hostname
port = args.port
release = args.release

if __name__ == "__main__":
    uvicorn.run("app.api:app", host=hostname, port=port, reload=not release)
