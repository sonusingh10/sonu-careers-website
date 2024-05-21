# we are for build web application that we will ask flash here
#pip install Flask
#module from flash installed then we need to use class Flash
# We are importing the class and we r creating object of the class
#https://www.youtube.com/watch?v=yBDHkveJUf4
#https://jovian.com/learn/web-development-with-python-and-flask
#hmtldog.com , if you want to lean hlm
#excalidraw.com

from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
  }, 
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
}, 
{
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 'Rs. 12,00,000'
}, 
{
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$120,000'
}
]


@app.route("/")
def hello_world():
  #return "Hello Juhi Singh , how you are doing Good morning :) This message from Sonu Singh"
  return render_template('home.html', jobs=JOBS)


if __name__ == "__main__":
  print("I am inside if")

  app.run(host="0.0.0.0", debug=True)
