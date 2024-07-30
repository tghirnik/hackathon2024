import os
import webex
import dotenv
import service

SCRIPT = "SCRIPT"
SYSTEM = "SYSTEM"
SERVICE = "SERVICE"

if __name__ == "__main__":
    dotenv.load_dotenv()
    system = os.getenv(SYSTEM) or SCRIPT
    systems = { SCRIPT: webex.orchestrate, SERVICE: service.run }
    if system not in systems: print("no such system"); exit(1)
    systems[system]()