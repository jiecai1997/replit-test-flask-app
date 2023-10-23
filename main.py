from flask import Flask
import datetime

app = Flask('app')


@app.route('/')
def hello_world():
  current_time = datetime.datetime.now().strftime("%H:%M:%S")
  current_date = datetime.datetime.now().strftime("%Y-%m-%d")
  return f'Current date and time is: {current_date} {current_time}'


app.run(host='0.0.0.0', port=8080)
