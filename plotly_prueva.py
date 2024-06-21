import plotly.graph_objects as go

# Datos para la función lineal y = 2x + 1
x_dat = [0, 1, 2, 3, 4]
y_dat = [2, 3, 5, 7, 8]

# Crear la figura
fig = go.Figure()

# Agregar la línea de la función lineal
fig.add_trace(go.Scatter(x=x_dat, y=y_dat, mode='lines', name='y = 2x + 1'))

# Configurar el diseño del gráfico
fig.update_layout(
    title='Función Lineal',
    xaxis_title='Eje X',
    yaxis_title='Eje Y'
)

# Guardar la figura en un archivo HTML
# fig.write_html('funcion_lineal.html')

# Guardar la figura en un archivo pdf
# fig.write_image('funcion_lineal.pdf', format='pdf')

# Mostrar la figura en el navegador web
fig.show()

