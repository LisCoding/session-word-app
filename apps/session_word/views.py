from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
def index(request):
    return render(request,'session_word/index.html')

def process(request):
    if request.method == "POST":
        time = strftime("%H:%M%p, %Y-%m-%d", gmtime())
        text =  request.POST['user_input']
        color = request.POST['color']
        # if checkbox in not check the we  pass a default value using get
        font = request.POST.get('font', 'small')
        request.session['info'] = {'time':time, 'user_input':text, 'color':color, 'font':font}

        if 'history' not in request.session:
            request.session["history"] = []
        request.session["history"] += [request.session['info']]
        print request.session["history"]

    return redirect("/session_word")

def reset_session(request):
    request.session["history"] = []
    return redirect("/session_word")
