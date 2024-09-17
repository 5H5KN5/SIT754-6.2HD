import os
print("Current working directory:", os.getcwd())
os.chdir(r"C:\Users\hrsto\SIT754-6.2HD")
print("Current working directory:", os.getcwd())

import newrelic.agent
newrelic.agent.initialize('newrelic.ini')

import datetime

def main():
    current_time = datetime.datetime.now()
    print("Current time:", current_time.strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    main()
