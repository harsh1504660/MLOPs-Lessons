import time
import redis
from flask import Flask 

app = Flask(__name__)
cache = redis.Redis()

def get_hit_count():
    retries=5
    while True:
        try:
            return cache.incr('hits')
        
        except redis.exceptions.ConnectionError as exc :
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route("/")
def hello():
    count = get_hit_count()
    return f"Hello from Docker , this is MLOps course, and I have seen this {count} times"

if __name__ =="__main__":
    app.run()