from flask import Flask, render_template, request, redirect, url_for
from consts import reasons, testimonials, treatments_catalog, wellness_packages, ayurveda_services
app = Flask(__name__)


@app.context_processor
def inject_treatments():
    return dict(treatments_catalog=treatments_catalog)
  
@app.route("/")
@app.route("/index")
@app.route("/home")
def home():
    return render_template("index.html", treatments=treatments_catalog.values(),
                            reasons=reasons, testimonials=testimonials)
       
@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/services')
def services():
    return render_template('services.html', services=ayurveda_services) 

@app.route('/treatments/<name>')
def treatments_details(name):
    treatment = treatments_catalog.get(name)
    if not treatment:
        return render_template('404.html'), 404
    return render_template('treatments_details.html', treatment=treatment, all_treatments=treatments_catalog)
  
                                          
# @app.route('/treatments')
# def treatments():
#     return render_template('treatments.html', treatments=treatmentlists)
 
@app.route('/treatments')
def treatments():
    return render_template('treatments.html', treatments=treatments_catalog.values())

@app.route('/packages')
def packages():
    return render_template('packages.html', packages=wellness_packages)

@app.route('/courses')
def courses():
    return render_template('courses.html')
           
@app.route('/blogs')
def blogs():
    return render_template('blogs.html')
    
@app.route('/review')
def review():
    return render_template('review.html')
 
@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        # Here you can add code to send email or save to DB
        return redirect(url_for("thank_you"))
    return render_template("contact.html")

@app.route("/thank-you")
def thank_you():
    return render_template("thank_you.html")

if __name__ == "__main__":
    app.run(debug=True)

 
   
      
     