# Automatización de la Evaluación del Rango de Movimiento del Hombro Mediante Human Pose Estimation (HPE)

**Autor:** Jesús Sánchez Rodríguez  
**Grado en Ingeniería Informática**  
**Especialidad:** Inteligencia Artificial  
**Consultor:** Ferran Diego Andilla  
**Profesora responsable de la asignatura:** Susana Acedo

## Descripción del Proyecto

Este proyecto tiene como objetivo desarrollar un software que, mediante una cámara, identifica puntos articulares y mide el rango de movimiento (ROM) del hombro utilizando técnicas de Human Pose Estimation (HPE).

## Estructura del Proyecto

El proyecto se compone de los siguientes archivos principales:
- `utils.py`: Contiene funciones auxiliares utilizadas en el procesamiento de datos y análisis de imágenes.
- `process.py`: Contiene el núcleo del algoritmo de estimación de pose y cálculo del ROM del hombro.

## Requisitos

Para ejecutar el software, se necesitan los siguientes requisitos:

- Python 3.x
- Librerías especificadas en `requirements.txt`

## Instalación

1. Clona el repositorio a tu máquina local:
    ```bash
    git clone https://github.com/jsr90/ROM_Shoulder_Estimation.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd ROM_Shoulder_Estimation
    ```
3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso en Jupyter Notebook

Puedes ejecutar el software directamente en un Jupyter Notebook. A continuación se muestra un ejemplo de cómo hacerlo:

1. **Instalación de Requisitos**

    Para instalar las dependencias necesarias, ejecuta el siguiente código en una celda de tu Jupyter Notebook:

    ```python
    !pip install -r requirements.txt -q
    ```

    Esto instalará todas las bibliotecas necesarias especificadas en el archivo `requirements.txt` de forma silenciosa (`-q`).

2. **Importación de `analyse_pose`**

    A continuación, importa la función `analyse_pose` del archivo `process.py`. Esta función es la encargada de analizar el rango de movimiento del hombro.

    ```python
    from process import analyse_pose
    ```

3. **Establecer el Diccionario de Resultados**

    Crea un diccionario llamado `results` para almacenar los resultados del análisis del rango de movimiento. Inicializa todas las claves con `None`.

    ```python
    results = {
        "abd_left": None,
        "abd_right": None,
        "add_left": None,
        "add_right": None,
        "flex_left": None,
        "flex_right": None,
        "ext_left": None,
        "ext_right": None
    }
    ```

4. **Obtener Resultados**

    Utiliza la función `analyse_pose` para obtener los resultados del análisis del rango de movimiento del hombro para diferentes movimientos y lados del cuerpo.

    ```python
    results['abd_left'], results['add_left'] = analyse_pose(left=True, func_='ABD/ADD')
    results['abd_right'], results['add_right'] = analyse_pose(left=False, func_='ABD/ADD')
    results['flex_left'], results['ext_left'] = analyse_pose(left=True, func_='FLEX/EXT')
    results['flex_right'], results['ext_right'] = analyse_pose(left=False, func_='FLEX/EXT')
    ```

    Aquí, se están calculando los resultados para la abducción (ABD), aducción (ADD), flexión (FLEX) y extensión (EXT) del hombro para ambos lados del cuerpo.

5. **Imprimir los Resultados**

    Por último, imprime los resultados del análisis del rango de movimiento del hombro utilizando el diccionario `results`.

    ```python
    print(results)
    ```

    Esto mostrará los resultados en la salida de la celda del Jupyter Notebook.


## Contacto

Para cualquier duda o consulta, por favor contacta con:
- **Jesús Sánchez Rodríguez**: [jsr90pro@gmail.com](mailto:jsr90pro@gmail.com)
