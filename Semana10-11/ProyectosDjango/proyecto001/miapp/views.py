from django.shortcuts import render, HttpResponse, redirect

layout = """
        <h1>Proyecto web (LP3)</h1>
        <hr/>
        <ul>
            <li>
                <a href="/inicio">Inicio</a>
            </li>
            <li>
                <a href="/saludo">Mensaje de saludo</a>
            </li>
            <li>
                <a href="/rango">Mostrar números [a,b]</a>
            </li>
            <li>
                <a href="/rango2">Mostrar números [10,15]</a>
            </li>
        <ul>
        <hr/>
"""

# Create your views here.
def index(request):
    estudiantes = ['Alexia Asunción',
                    'Jheremy Ayquipa',
                    'Axel Barzola',
                    'Josue Caman',
                    'Carlos Curo',
                    'Brian Inca',
                    'Gerson Sahuma',
                    'Jhon Urbisagastegui',
                    'Elias Talledo'
                    ]
    return render(request,'index.html',{
        'titulo':'Inicio',
        'mensaje':'Proyecto web con DJango',
        'estudiantes':estudiantes
    })

def saludo(request):
    return render(request,'saludo.html',{
        'titulo':'Saludo',
        'autor':'Alexia Asunción'
    })

def rango(request):
    a = 10
    b = 20
    rango_numeros = range(a,b+1)
    return render(request,'rango.html',{
        'titulo':'Rango',
        'a':a,
        'b':b,
        'rango_numeros':rango_numeros
    })

def rango2(request,a,b):
    if a > b:
        return redirect('rango2', a=b, b=a)
    resultado = f"""
                <h2>Números de [{a},{b}]</h2>
                Resultado: <br>
                <ul>
    """
    while a <= b:
        resultado += f"<li> {a} </li>"
        a += 1
    resultado += "</ul>"
    return HttpResponse(layout + resultado)