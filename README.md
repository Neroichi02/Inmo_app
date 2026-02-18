# Inmo_app
# 🏢 Sistema de Gestión Inmobiliaria

Aplicación de escritorio desarrollada en **Python** para la gestión de una inmobiliaria.  
Permite administrar clientes, propiedades, ventas, alquileres y generar reportes en PDF y Excel.

---

## 🚀 Tecnologías utilizadas

- 🐍 Python 3
- 🖥 PyQt6 (Interfaz gráfica)
- 🗄 SQLite (Base de datos)
- 🧠 SQLAlchemy (ORM)
- 📄 ReportLab (Generación de PDF)
- 📊 OpenPyXL (Exportación a Excel)

---

## 📦 Funcionalidades

- Gestión de clientes
- Gestión de propiedades
- Registro de ventas y alquileres
- Base de datos local con SQLite
- Generación de reportes en PDF
- Exportación de datos a Excel
- Interfaz gráfica moderna con PyQt6

---

## 🗂 Estructura del Proyecto

Inmobiliaria_app/
│
├── main.py
├── database.py
│
├── models/
├── services/
├── ui/
├── testing/
│
└── README.md


---

## ⚙️ Instalación

1. Clonar el repositorio:

git clone <url-del-repositorio>


2. Crear entorno virtual:

python -m venv venv


3. Activar entorno virtual:

- Linux / Mac:
source venv/bin/activate

- Windows:
venv\Scripts\activate


4. Instalar dependencias:
pip install -r requirements.txt


---

## ▶️ Ejecutar la aplicación

python main.py


---

## 📄 Generación de Reportes

- Reportes PDF generados con **ReportLab**
- Exportación a Excel usando **OpenPyXL**

---

## 🧠 Arquitectura

La aplicación utiliza el patrón:

- **Modelo (Models)** → SQLAlchemy ORM
- **Servicios (Services)** → Lógica de negocio
- **UI** → Interfaz PyQt6
- **Base de Datos** → SQLite local

---

## 📌 Autor

Desarrollado por Tobias Leguizamón  
Proyecto educativo de aprendizaje en Python.

---

## 📜 Licencia

Proyecto de uso educativo.



