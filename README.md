# Proyecto: Sandbox Automation Testing con Selenium y Pytest

Este repositorio contiene un conjunto de pruebas automatizadas diseñadas para practicar y demostrar habilidades en **QA Automation** usando **Selenium**, **Pytest** y el enfoque **Page Object Model (POM)**.

## 🚀 Características principales

- Automatización de formularios (texto, checkboxes, radios, dropdowns).
- Manejo de popups y alertas.
- Interacción con tablas estáticas y dinámicas.
- Validación de elementos con ID dinámico.
- Ejemplos de Shadow DOM.
- Organización con **Page Object Model** para mayor mantenibilidad.

## 📂 Estructura del proyecto

```
├── pages/                  # Clases POM que representan las páginas
├── tests/                  # Casos de prueba organizados por módulo
├── conftest.py             # Configuración de Pytest (fixtures, setup/teardown)
├── requirements.txt        # Dependencias del proyecto
└── README.md               # Documentación principal
```

## ⚙️ Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/florcel/sandbox-automation.git
   cd sandbox-automation
   ```

2. Crear un entorno virtual e instalar dependencias:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   .venv\Scripts\activate    # Windows

   pip install -r requirements.txt
   ```

## ▶️ Ejecución de pruebas

Ejecutar todas las pruebas:
```bash
pytest -v
```

Ejecutar pruebas específicas (ejemplo: forms y popup):
```bash
pytest -k "forms or popup" -v
```

## 📊 Reportes

### Allure Report

1. Ejecutar las pruebas generando resultados para Allure:
   ```bash
   pytest --alluredir=allure-results
   ```

2. Levantar el reporte:
   ```bash
   allure serve allure-results
   ```

## 🛠️ Tecnologías utilizadas

- Python 3.10+
- Selenium
- Pytest
- Webdriver Manager
- Allure Framework

## ✨ Autor

Proyecto desarrollado por *Florencia* como práctica de QA Automation.
