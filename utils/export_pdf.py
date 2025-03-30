from fpdf import FPDF
from io import BytesIO

def generate_pdf(df):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Reporte de Pagos", ln=True, align='C')

    for index, row in df.iterrows():
        text = f"{row['Nombres']} | {row['Curso']} | {row['Fecha Pago'].strftime('%d/%m/%Y')} | ${row['Pago']:,.0f}"
        pdf.cell(200, 10, txt=text, ln=True)

    buffer = BytesIO()
    pdf.output(buffer)
    buffer.seek(0)
    return buffer