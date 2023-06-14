from flask import Flask, request, render_template#, session

from algorithm import calculate

app = Flask(__name__)
app.config["DEBUG"] = True
#app.config["SECRET_KEY"] = "lkmaslkdsldsamdlsdmasldsmkdd"

@app.route("/", methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        a = None
        b = None
        c = None
        d = None
        e = None
        f = None
        g = None
        h = None
        i = None
        j = None
        k = None
        l = None
        m = None
        n = None
        o = None
        p = None
        try:
            a = str(request.form["a"])
            b = str(request.form["b"])
            c = str(request.form["c"])
            d = str(request.form["d"])
            e = str(request.form["e"])
            f = str(request.form["f"])
            g = str(request.form["g"])
            h = str(request.form["h"])
            i = str(request.form["i"])
            j = str(request.form["j"])
            k = str(request.form["k"])
            l = str(request.form["l"])
            m = str(request.form["m"])
            n = str(request.form["n"])
            o = str(request.form["o"])
            p = str(request.form["p"])
        except:
            errors += "{!r} is not a letter.\n".format(request.form["letters"])
        if a is not None and b is not None and c is not None and d is not None and e is not None and f is not None and g is not None and h is not None and i is not None and j is not None and k is not None and l is not None and m is not None and n is not None and o is not None and p is not None:
            result = calculate(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)
            return render_template('result.html',result=result)

    return render_template('index.html',errors=errors)


