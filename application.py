
#from Unit 5 Notes with Megan:

#from flask import Flask #render-template, #()url_for
#this connects html files under dirtory  to roots we created 

#app = Flask(__name__)

#@app.route('/')n 
      #(or @app.route('/meow')
#def index():
  #return 'Hello from Pet Adoption' #After: return render_template('index.html') (...This sends message to browser to add hyper link)
    #(or return 'meow')
    #replace with html site instead of the single message above: OR: return'''
       #<h1>Pet Adoption</h1>
       #<button>Add Pet</button>
        #'''
 ##@app.route('/add-pet')
 #def add_pet():
 #return render_template('addpet.html')

##@app.route('/pet')
#def  pet():
#       return render_template('pet.html')
  
  #if __name__== '__main__':
    #app.run(debug=True, part=8000, host='0.0.0.0')
    #(CLick on top eye and matching port to open up website and see what was typed on workspace)
    
    #___________________________________
    #UNDER index.html folder:
    #<!DOCTYPE html>
    #<html>
      #<head>
           #<meta charset="utf-8>
           #<title>Pet Adoption</title>
           #<meta name="description" content="A collection ofadpted pets"
           #<meta name="viewport" content="width=device-width, initi..  
           ##(add to syles.css) <link rel = "stylesheet" href="/static/css/styles.css"
      #</head>
      #<body>
          #<section class="main-header">
            
               #<a href="{{ url_for('index')}}">
                  #<h1 class="header">
                        #i class="fas fa-paw"></i>
                        #Pet Adoption 
                        #</h1>
                  
                  #</a>
                   #h1>Pet Adoption</h1>
               #</a>
          #</section>
          ##<section>
            #a href="#">
               #<div>
                    #<h2>Pet's name</h2>
                    #<p>Age</p>
                    #<p>Description<#copy or write in a decription#/p>
                    
      #</form
      #</body>
      #<a class=add-pet.btn" href="{{url_for alt=add pet('add_pet')">
      #</a>
      #</section>
      #script src="/static/js/app.js"></script>
    #</html>

#UNDER styles.css
#root:{
#   --primary
#   --secondary
#   --accent
#   --background
#}
#{
#font-family" 'sans-serif', 'romans', Arial;



