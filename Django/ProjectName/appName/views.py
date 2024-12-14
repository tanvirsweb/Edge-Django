from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'index.html')

def newpageh(request):
    return HttpResponse ("<h1> Hi </h1>")

def page1(request):
    page_title = "Welcome to My Django Page"
    graph_html = interactive_plot_view()

    # Pass python value to a webpage
    return render(request,'page1.html', {
        'page_title': page_title,
        'username': "Tanvir Anjom Siddique",
        'items': ['item 01', 'item02', 3],
        'info': {'name': 'Alvi', 'age': 24, 'city': 'New York'},
        'graph_html': graph_html
    })

# views.py
import plotly.express as px
# pip install plotly
def interactive_plot_view():
    # Create a plot using Plotly
    df = px.data.gapminder().query("year == 2007")
    fig = px.scatter(
        df, x="gdpPercap", y="lifeExp", size="pop", color="continent", hover_name="country",
        log_x=True, size_max=60
    )
    
    # Convert the plot to HTML
    graph_html = fig.to_html(full_html=False)
    
    # return render(request, 'interactive_plot.html', {'graph_html': graph_html})
    return graph_html
