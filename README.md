# 📚 Aplicación de Pagos de Estudiantes

Aplicación web desarrollada en Python usando Streamlit para visualizar, filtrar y gestionar pagos de estudiantes en cursos.

## 🔧 Funcionalidades

- Visualización de pagos totales por estudiante y por curso (dashboard).
- Filtros por nombre, curso y rango de fechas.
- Exportación de reportes en Excel y PDF.
- Formulario para agregar nuevos pagos (persistencia en CSV).
- Preparado para Streamlit Cloud y Docker.

## 🚀 Cómo Ejecutar

### 1. Requisitos

Instala las dependencias necesarias:
```bash
pip install -r requirements.txt
```

### 2. Ejecutar localmente

```bash
streamlit run main.py
```

---

## ☁️ Despliegue en Streamlit Cloud

1. Sube el proyecto a un repositorio en GitHub.
2. Ve a [streamlit.io/cloud](https://streamlit.io/cloud)
3. Conéctate con tu cuenta de GitHub.
4. Selecciona el repo y apunta a `main.py`.

---

## 🐳 Docker

### 1. Construir la imagen
```bash
docker build -t pagos-app .
```

### 2. Ejecutar el contenedor
```bash
docker run -p 8501:8501 pagos-app
```

---

## 📁 Estructura del proyecto

```
.
├── main.py
├── requirements.txt
├── Dockerfile
├── Pagos estudiante - Pagos.csv
└── utils/
    ├── __init__.py
    ├── load.py
    ├── filters.py
    ├── export_excel.py
    └── export_pdf.py
```

---

## 📬 Contacto

Desarrollado por [Tu Nombre] – ¡Mejorando la gestión educativa con Python!