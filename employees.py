import streamlit as st
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

date_column = 'released'
data_url = ('Employees.csv')
import codecs

@st.cache
def load_data(nrows):
    doc = codecs.open('Employees.csv', 'rU', 'latin1')
    data = pd.read_csv(doc, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return data
def filter_data_by_employee(Employee_ID):
    filtered_data_employee = data[data['Employee_ID'] == Employee_ID]
    return filtered_data_employee

def filter_data_by_hometown(Hometown):
    filtered_data_hometown = data[data['Hometown'] == Hometown]
    return filtered_data_hometown

def filter_data_by_unit(Unit):
    filtered_data_unit = data[data['Unit'] == Unit]
    return filtered_data_unit

def filter_data_by_level(Education_Level):
    filtered_data_level = data[data['Education_Level'] == Education_Level]
    return filtered_data_level

def filter_data_by_home(Hometown):
    filtered_data_home = data[data['Hometown'] == Hometown]
    return filtered_data_home

def filter_data_by_unidad(Unit):
    filtered_data_unidad = data[data['Unit'] == Unit]
    return filtered_data_unidad

data_load_state = st.text('Loading')
data = load_data(500)
data_load_state.text("Done! (using st.cache)")

# Create the title for the web app
st.title("Fenómeno de deserción laboral.")
st.header("Análisis de datos.")
st.write('Con los datos provistos en el Hackathon HackerEarth  2020, tomando como hipótesis que esta información resultará explicativa del fenómeno de deserción laboral que tanto afecta en la actualidad a las empresas y organizaciones, se analizará el siguiente DataFrame. ')


sidebar = st.sidebar
st.sidebar.image('foto.jpg')
sidebar.title("Búsqueda deserción laboral")
sidebar.header("Utiliza el mismo formato de la tabla (mayúsculas o mínusculas)")

if st.sidebar.checkbox('Mostrar Dataframe'):
    st.subheader('Dataframe completo')
    st.write(data)

employee_id = st.sidebar.text_input('Employee_ID :')
btnBuscar = st.sidebar.button('Buscar Employee')

if (btnBuscar):
    data_empleado = filter_data_by_employee(employee_id.upper())
    count_row = data_empleado.shape[0]  
    st.write(f"Total empleados : {count_row}")
    st.write(data_empleado)

hometown = st.sidebar.text_input('Hometown:')
btnBuscar1 = st.sidebar.button('Buscar Hometown')

if (btnBuscar1):
    data_hometown = filter_data_by_hometown(hometown)
    count_row = data_hometown.shape[0]  
    st.write(f"Total : {count_row}")
    st.write(data_hometown)


unit = st.sidebar.text_input('Unit :')
btnBuscar2 = st.sidebar.button('Buscar Unit')

if (btnBuscar2):
    data_unit = filter_data_by_unit(unit)
    count_row = data_unit.shape[0]  
    st.write(f"Total : {count_row}")
    st.write(data_unit)

selected_level = st.sidebar.selectbox("Seleccionar Nivel Educativo", data['Education_Level'].unique())
btnFilterbylevel = st.sidebar.button('Filtrar')

if (btnFilterbylevel):
   filterbylevel = filter_data_by_level(selected_level)
   count_row = filterbylevel.shape[0]  # Gives number of rows
   st.write(f"Total : {count_row}")

   st.dataframe(filterbylevel)

selected_home = st.sidebar.selectbox("Seleccionar Ciudad Natal", data['Hometown'].unique())
btnFilterbyhome = st.sidebar.button('Filtrar por ciudad')

if (btnFilterbyhome):
   filterbyhome = filter_data_by_home(selected_home)
   count_row = filterbyhome.shape[0]  # Gives number of rows
   st.write(f"Total : {count_row}")

   st.dataframe(filterbyhome)

selected_unit = st.sidebar.selectbox("Seleccionar Unidad", data['Unit'].unique())
btnFilterbyunit = st.sidebar.button('Filtrar por unidad')

if (btnFilterbyunit):
   filterbyunit = filter_data_by_unidad(selected_unit)
   count_row = filterbyunit.shape[0]  # Gives number of rows
   st.write(f"Total : {count_row}")

   st.dataframe(filterbyunit)


fig, ax = plt.subplots()  
   
ax.hist(data.Age)  
   
st.header("Empleados agrupados por edad")  
   
st.pyplot(fig)  
   
st.markdown("___")   

fig1, ax1 = plt.subplots()  
   
ax1.hist(data.Unit)  
   
st.header("Empleados agrupados por Unidad")
plt.xticks(rotation=90)  
   
st.pyplot(fig)  
   
st.markdown("___")  

fig2, ax2 = plt.subplots()  
   
y_pos = data['Hometown']  
x_pos = data['Attrition_rate']  
   
ax2.barh(y_pos, x_pos)  
ax2.set_ylabel("Hometown")  
ax2.set_xlabel("Tasa de deserción")  
ax2.set_title('Ciudades con mayor índice de deserción')   
st.header("Visualización de ciudades con tasa de deserción")  
   
st.pyplot(fig2)  
   
st.markdown("___")    

fig3, ax3 = plt.subplots()  
   
ax3.scatter(data.Age, data.Attrition_rate)  
ax3.set_xlabel("Edad")  
ax3.set_ylabel("Tasa de deserción")  
   
st.header("Relación edad-tasa de deserción")  
   
st.pyplot(fig3)
st.markdown("___")  

fig4, ax4 = plt.subplots()  
   
ax4.scatter(data.Time_of_service, data.Attrition_rate)  
ax4.set_xlabel("Tiempo de servicio")  
ax4.set_ylabel("Tasa de deserción")  
   
st.header("Relación Tiempo de servicio-tasa de deserción")  
   
st.pyplot(fig4)
st.markdown("___") 




