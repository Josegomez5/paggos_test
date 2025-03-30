from io import BytesIO
import pandas as pd

def generate_excel(data):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        data.to_excel(writer, index=False, sheet_name='Pagos')
    output.seek(0)
    return output