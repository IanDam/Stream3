import streamlit as st
import pandas as pd
import numpy as np
import pickle as pkl
import geihdanepy as geih

df1= geih.datos(2021,'junio','Caracteristicas','Cabecera')
df2= geih.datos(2021,'junio','Ocupados','Cabecera')

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

