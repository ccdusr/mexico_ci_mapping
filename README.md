# Mexico Mapping

Un proyecto para mapear las industrias creativas en México.

## Prerequisitos

- Git (https://git-scm.com)
- Python (https://www.python.org/downloads/)
- Jupyter Notebook (https://jupyter.readthedocs.io/en/latest/install.html)
- Anaconda (opcional<sup>[1]</sup>) (https://www.anaconda.com)

<a name="anaconda">1.</a> La instalación de Anaconda incluye Python y Jupyter Notebook.

## Manual de uso

1. Descargar el proyecto desde la línea de comandos:
```bash
git clone https://github.com/ccdusr/mexico_ci_mapping.git
```

2. Instalar las librerías necesarias desde la línea de comandos:
```bash
pip install -r requirements.txt
```

3. Abrir Jupyter desde la línea de comandos:
```bash
jupyter notebook
```

4. Se debería poder ver el notebook en una pestaña de su navegador.

5. Dentro de jupyter navegar hasta la carpeta *notebooks*, la cual se encuentra dentro del proyecto descargado.

6. Abrir y correr el notebook *denue.ipynb*.

Project Organization
------------
    .
    ├── data
    │   ├── denue: Datos de INEGI.
    │   ├── nesta: Datos de las empresas creativas de DENUE definidas por NESTA.
    │   ├── processed: Datos limpios.
    │   └── shapefiles: Shapefile con los estados de México.
    │       └── mexico
    ├── notebooks
    ├── references
    │   └── reading
    └── reports
        ├── data_sources
        ├── figures
        └── project_reports_and_slides
