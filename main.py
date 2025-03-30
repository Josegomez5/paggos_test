# main.py
import streamlit as st
import pandas as pd
from io import BytesIO

from utils.load import load_data, save_new_payment
from utils.filters import filter_data
from utils.export_excel import generate_excel
from utils.export_pdf import generate_pdf

# Cargar datos desde CSV
DATA_FILE = "Pagos estudiante - Pagos.csv"
df = load_data(DATA_FILE)

st.title("📚 Aplicación de Pagos de Estudiantes")

# Sidebar - Filtros
st.sidebar.header("Filtrar datos")
nombre = st.sidebar.text_input("Buscar por nombre")
curso = st.sidebar.selectbox("Curso", options=['Todos'] + sorted(df['Curso'].unique().tolist()))

# Filtro por fechas
start_date = st.sidebar.date_input("Fecha inicio", df['Fecha Pago'].min())
end_date = st.sidebar.date_input("Fecha fin", df['Fecha Pago'].max())

# Filtro por monto de pago
min_pago = st.sidebar.number_input("Pago mínimo", min_value=0.0, value=0.0)
max_pago = st.sidebar.number_input("Pago máximo", min_value=0.0, value=float(df['Pago'].max()))

# Convertir fechas a datetime64 para comparación
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Aplicar filtros
filtered_df = filter_data(df, nombre, curso, start_date, end_date)
filtered_df = filtered_df[(filtered_df['Pago'] >= min_pago) & (filtered_df['Pago'] <= max_pago)]

st.subheader("📋 Datos Filtrados")
st.dataframe(filtered_df)

# Dashboard
st.subheader("📈 Total Pagado por Estudiante")
total_por_estudiante = filtered_df.groupby("Nombres")["Pago"].sum()
st.bar_chart(total_por_estudiante)

st.subheader("📊 Total Pagado por Curso")
total_por_curso = filtered_df.groupby("Curso")["Pago"].sum()
st.bar_chart(total_por_curso)

# Exportar a Excel
st.subheader("📤 Exportar Reporte a Excel")
if st.button("Generar Reporte Excel"):
    excel = generate_excel(filtered_df)
    st.download_button(
        label="📥 Descargar Excel",
        data=excel,
        file_name="reporte_pagos.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

# Exportar a PDF
st.subheader("🖨️ Exportar Reporte a PDF")
if st.button("Generar Reporte PDF"):
    pdf = generate_pdf(filtered_df)
    st.download_button(
        label="📥 Descargar PDF",
        data=pdf,
        file_name="reporte_pagos.pdf",
        mime="application/pdf"
    )

# Agregar nuevo registro
st.subheader("🆕 Agregar Pago")
with st.form("nuevo_pago"):
    nombre_nuevo = st.text_input("Nombre")
    curso_nuevo = st.text_input("Curso")
    fecha_pago_nuevo = st.date_input("Fecha de Pago")
    pago_nuevo = st.number_input("Pago", min_value=0.0)
    clases_nuevas = st.number_input("Número de clases", min_value=1, step=1)
    submitted = st.form_submit_button("Guardar")

    if submitted:
        if not nombre_nuevo or not curso_nuevo or pago_nuevo == 0.0 or clases_nuevas <= 0:
            st.error("❌ Por favor, completa todos los campos obligatorios correctamente.")
        else:
            nuevo = {
                'Nombres': nombre_nuevo,
                'Curso': curso_nuevo,
                'Fecha Pago': fecha_pago_nuevo,
                'Fecha inicio': fecha_pago_nuevo,
                'Pago': pago_nuevo,
                'num clases': clases_nuevas,
                'proximo pago': None
            }
            save_new_payment(DATA_FILE, nuevo)
            st.success("✅ Pago agregado y guardado correctamente en el archivo CSV.")
