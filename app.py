import streamlit as st
import pandas as pd
import numpy as np
import pickle as pkl


df1= pd.read_csv("./data4.csv")
st.title("Proyecto 8")
st.subheader("Descripción suncita de las variables")
st.write(""" "INGLABO" = Ingresos Laborales """)
st.write(""" "P6050" = Variable discreta numerica que da información sobre ¿Cuál es el parentesco de ... con el jefe o jefa del hogar? a. Jefe (a) del hogar b. Pareja, esposo(a), cónyuge, compañero(a) c. Hijo(a), hijastro(a) d. Nieto(a) e. Otro pariente f. Empleado(a) del servicio doméstico y sus parientes g. Pensionista h.Trabajador i. Otro no pariente""")
st.write(""" "P6020" = Discreta numerica Información del Sexo del usuario 1 Hombre 2 Mujer """)
st.write(""" "P6040" = Variable Continua Numerica, ¿Cuántos años cumplidos tiene … ? Valores numericos en años, Si es menor de 1 año, escriba 00.""")
st.write(""" 'P6070' = Discreta numerica, Información del Estado Civil del Usuario;Actualmente: a. No esta casado(a) y vive en pareja hace menos de dos años b. No esta casado (a) y vive en pareja hace dos años o más c. Esta casado (a) d. Esta separado (a) o divorciado (a) e.Esta viudo (a) f. Esta soltero (a)""")
st.write(""" "ESC"= Continua Numerica que da los Años de escolaridad """)
st.write(""" "P6426"=Variable Continua Numerica, respuesta a ¿cuanto tiempo lleva trabajando en esta empresa, negocio,industria, oficina, firma o finca de manera continua? se obtiene el valor en meses, si es menos de un mes el dato es 000""")
st.write(""" "P6430"=Discreta Numerica- Categorica se tiene información sobre el tipo de trabajo este puede ser:1. Obrero o empleado de empresa particular 2. Obrero o empleado del gobierno 3. Empleado doméstico 4. Trabajador por cuenta propia 5. Patrón o empleador 6. Trabajador familiar sin remuneración 7. Trabajador sin remuneración en empresas o negocios de otros hogares 8. Jornalero o peón 9.Otro""")
st.write(""" "P6800"=Variable Continua Numerica que nos da información sobre: ¿Cuántas horas a la semana trabaja normalmente.... en ese trabajo ? en Horas """)
st.write(""" "P6585S1"= Discreta Numerica información sobre si recibio el mes pasado subsidio o auxilio de alimentación 1 Sí 2 No 9 No sabe, no informa""")
st.write(""" "P6585S2"=Discreta Numerica información sobre si recibio el mes pasado subsidio o auxilio de transporte 1 Sí 2 No 9 No sabe, no informa""")
st.write(""" "P6585S3"= Discreta Numerica información sobre si recibio el mes pasado subsidio o auxilio familiar 1 Sí 2 No 9 No sabe, no informa""")
st.write(""" "P6585S4"=Discreta Numerica información sobre si recibio el mes pasado subsidio o auxilio de educación 1 Sí 2 No 9 No sabe, no informa""")

st.subheader("Gráficas relevantes")

st.image("./4/1.png")
st.image("./4/2.png")

st.write("""prediccion""")

if jefe_de_hogar == "jefe del hogar" :
  jefe_hogar == 1
else 0
jefe_de_hogar = 1 if jefe_de_hogar == 'jefe del hogar' else 0
jefe_de_hogar = st.selectbox('Relacion:',("Jefe del hogar","Pareja", "esposo(a)", "cónyuge"," compañero(a)","Hijo(a)", "hijastro(a)","Nieto(a)", "Otro pariente"," f. Empleado(a) del servicio doméstico y sus parientes","Pensionista","Trabajador","Otro no pariente"))
Customer_Age =st.number_input('Ingrese su Edad')


Gender = 1 if Gender == 'Masculino' else 0

Education_Level = st.number_input('Ingrese su nivel educativo:(Si este es  ingrese 0, si este es secundaria ingrese 1, si este es universitario ingrese 2, si usted es graduado ingrese 3, si tiene un postgrado ingrese 4 y si tiene un doctorado ingrese 5, si se desconoce ingrese 6)')

Marital_Status = st.selectbox('Estado Civil:',('Casado','Soltero'))

Marital_Status = 1 if Marital_Status == 'Casado' else 0

Income_Category= st.number_input('Categoría de ingresos:(Si se desconoce ingrese 0, si es menor a $40K ingrese 1, si se encuentra entre $40K - $60K ingrese 2,si se encunetra entre $60K - $80K ingrese 3, si se encunetra entre $80K - $120K ingrese 4, si es de $120K o mayor ingrese 5)')
Card_Category = st.number_input('Tipo de tarjeta(Si es Azul ingrese 0, si es dorada ingrese 1, si es plata ingrese 2 y si es platino ingrese 3)')
Months_on_book = st.number_input('Duración de la relación con el banco')
Total_Relationship_Count = st.number_input('Número total de productos')
Months_Inactive_12_mon= st.number_input('Número de meses de inactividad')
Credit_Limit = st.number_input('Límite de crédito')
Total_Revolving_Bal = st.number_input('Saldo rotativo total')
Avg_Open_To_Buy = st.number_input('Línea de crédito abierta a la compra (media de los últimos 12 meses)')
Total_Amt_Chng_Q4_Q1 = st.number_input('Variación del importe de las transacciones(cuarto trimestre sobre primer trimestre)')
Total_Trans_Amt = st.number_input('Cantidad total de las transacciones(12 meses)')
Total_Trans_Ct = st.number_input('Recuento de transacciones')
Total_Ct_Chng_Q4_Q1 = st.number_input('Cambio en el recuento de transacciones')
Avg_Utilization_Ratio =  st.number_input('Utilización promedio de la tarjeta')

st.subheader("""Modelo """)

clsr_pickle8 = open('clsr_proyecto8.pickle','rb')
clsr = pkl.load(clsr_pickle8)
print(clsr)

datos= [Gender,Marital_Status,Customer_Age,Education_Level,Months_on_book,Income_Category,Card_Category,Total_Relationship_Count,Months_Inactive_12_mon,
Credit_Limit,Total_Revolving_Bal,Avg_Open_To_Buy,Total_Amt_Chng_Q4_Q1,Total_Trans_Amt,Total_Trans_Ct,Total_Ct_Chng_Q4_Q1,Avg_Utilization_Ratio]

prediction = clsr.predict([np.array(datos).reshape(1,-1)][0])[0]

resultado = 'Existing customer' if prediction ==1 else 'Attrited Customer'
st.write(resultado)
