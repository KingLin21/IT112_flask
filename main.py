from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def home():
  return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/fortune', methods=['GET', 'POST'])
def fortune():
  return render_template('fortune.html')

@app.route('/fortunetold', methods=['GET','POST'])
def fortunetold():
  fortune=None
  if request.method == 'POST':
    color = request.form.get('color')
    number = request.form.get('number')
    if color == 'red' and number =='1':
      fortune = "You will have great success in life"
    elif color =='red' and number =='2':
      fortune = "You will be unusually successful in business"
    elif color =='red' and number =='3':
      fortune = "You will become more and more wealthy"
    elif color =='red' and number =='4':
      fortune = "You will make a change for the better"
    elif color =='red' and number =='5':
      fortune = "You will be loved by millions"
    elif color =='yellow' and number =='1':
      fortune = "You will travel all around the world"
    elif color =='yellow' and number =='2':
      fortune = "You will alwyas be surrounded by true friends"
    elif color =='yellow' and number =='3':
      fortune = "You will be find many treasures in life"
    elif color =='yellow' and number =='4':
      fortune = "You are blessed with a long life"
    elif color =='yellow' and number =='5':
      fortune = "You will enjoy good health"
    elif color =='blue' and number =='1':
      fortune = "You will inherit a large sum of money"
    elif color =='blue' and number =='2':
      fortune = "A life time of happiness awaits you"
    elif color =='blue' and number =='3':
      fortune = "A beautiful, smart, and loving person will enter your life"
    elif color =='blue' and number =='4':
      fortune = "A dubious friend may be an enemy in hiding"
    elif color =='blue' and number =='5':
      fortune = "A pleasant surprise awaits you"
    elif color =='green' and number =='1':
      fortune = "All will go well with your next project"
    elif color =='green' and number =='2':
      fortune = "All your hardwork will soon pay off"
    elif color =='green' and number =='3':
      fortune = "Allow compassion to guide your decisions"
    elif color =='green' and number =='4':
      fortune = "Believe in yourself and others will too"
    elif color =='green' and number =='5':
      fortune = "Bide your time, for success is near"
  return render_template('fortunetold.html', user=request.form.get('user'), fortune=fortune)


app.run(host='0.0.0.0', port=81)
