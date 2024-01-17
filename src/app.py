import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("EMPLEATRONIX")
st.text("Todos los datos sobre los empleados en una aplicación.")

# Cargar el conjunto de datos
file_path = 'archivo/employees.csv'
df = pd.read_csv(file_path)
# Mostrar la tabla en Streamlit
st.write(df)

# Crear gráfica horizontal
st.subheader("Gráfica Horizontal")

# Organizar elementos horizontalmente utilizando st.columns
col1, col2, col3 = st.columns([1, 1, 2])

# Selector de color para la gráfica
bar_color = col1.color_picker("Elige un color para las barras", "#1f77b4")

# Toggle button para mostrar o no los nombres
name_feature = col2.toggle('Mostrar el nombre') 

# Checkbox para mostrar o no el sueldo en la gráfica
salary_feature = col3.toggle('Mostrar sueldo en la barra')

# Crear la gráfica
fig, ax = plt.subplots(figsize=(10, len(df) * 0.5))

if name_feature and salary_feature:
    bars = plt.barh(df['full name'], df['salary'], color=bar_color)
    ax.bar_label(bars, fmt="%d€", padding=5)
elif not name_feature and not salary_feature:
    plt.barh(df['full name'], df['salary'], color=bar_color)
    plt.tick_params(axis='y', which='both', left=False, labelleft=False)
else:
   
    if name_feature:
        bars = plt.barh(df['full name'], df['salary'], color=bar_color)
        
    elif salary_feature:
       bars = plt.barh(df.index, df['salary'], color=bar_color)

       ax.bar_label(bars, fmt="%d€", padding=5)


st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot(fig)
