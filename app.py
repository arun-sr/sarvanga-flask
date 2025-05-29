from flask import Flask, render_template, request, redirect, url_for
from consts import treatmentlists, reasons, testimonials
app = Flask(__name__)

@app.route("/")
@app.route("/index")
@app.route("/home")
def home():
    return render_template("index.html", treatments=treatmentlists,
                            reasons=reasons, testimonials=testimonials)
      
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route('/treatments/<name>')
def treatment_detail(name):
    return render_template(f'treatments/{name}.html')
     
@app.route('/treatments')
def treatments():
    return render_template('treatments.html')
  
@app.route('/packages')
def packages():
    return render_template('packages.html')

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

 
   
      
    