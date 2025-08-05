# 📊 Proyecto de Consolidación de Resultados PLANEA (2015–2018)

Este repositorio contiene un flujo de trabajo en Python para consolidar los resultados de la evaluación PLANEA de los años 2015, 2016, 2017 y 2018, estandarizando columnas, limpiando datos y generando un archivo maestro listo para análisis posteriores.

---

## 📁 Estructura del Proyecto

```
tesis_petc/
│
├── data/
│   └── raw/
│       └── planea/
│           ├── 2015/
│           ├── 2016/
│           ├── 2017/
│           └── 2018/
│
├── logs/
│   └── planea/
│       ├── consolidador_planea.log
│       └── final_planea.log
│
├── output/
│   └── planea/
│       ├── consolidado_2015.csv
│       ├── consolidado_2016.csv
│       ├── consolidado_2017.csv
│       ├── consolidado_2018.csv
│       └── planea_total.csv
│
├── params/
│   └── paths.py
│
├── src/
│   └── etl/
│      ├── columnas_planea_2015.py
│      ├── columnas_planea_2016.py
│      ├── columnas_planea_2017.py
│      ├── columnas_planea_2018.py
│      └── schema_planea.py
│
├── utils/
│   └── logging_config.py
│
├── planea_2015.py
├── planea_2016.py
├── planea_2017.py
├── planea_2018.py
├── planea_final.py
├── requirements.txt
└── .gitignore
```

---

## 🚀 Flujo de Ejecución

### Paso 1: Consolidar por año

Ejecuta los siguientes scripts desde la raíz del proyecto para procesar los archivos de cada año y generar sus respectivos archivos `consolidado_*.csv`:

```bash
python planea_2015.py
python planea_2016.py
python planea_2017.py
python planea_2018.py
```

Cada script:

- Lee archivos Excel por año desde `data/raw/planea/`.
- Asigna nombres de columnas estandarizados (ver `src/etl/columnas_planea_20XX.py`).
- Añade columnas auxiliares (`ANIO_EVALUACION`, `ENTIDAD`, `ARCHIVO_ORIGEN`).
- Guarda el resultado en `output/planea/consolidado_20XX.csv`.
- Registra los logs en `logs/planea/consolidador_planea.log`.

---

### Paso 2: Consolidar el archivo maestro

Una vez generados los archivos de cada año, ejecuta:

```bash
python planea_final.py
```

Este script:

- Carga los archivos `consolidado_2015.csv` a `consolidado_2018.csv`.
- Genera el archivo final `output/planea/planea_total.csv`.
- Registra los eventos en `logs/planea/final_planea.log`.

---

## 🧠 Archivos clave

| Archivo | Descripción |
|--------|-------------|
| `planea_20XX.py` | Script para consolidar archivos de cada año. |
| `planea_final.py` | Une todos los `consolidado_*.csv` en un archivo final limpio. |
| `schema_planea.py` | Define las columnas estándar (`columnas_finales_planea`) y una lista auxiliar de entidades (`ENTIDADES`). |
| `columnas_planea_20XX.py` | Contiene la lista de nombres de columnas específicas para ese año. |
| `logging_config.py` | Función `configurar_logger_planea()` para configurar logs año a año. |
| `paths.py` | Define rutas útiles como `LOGS_DIR`, etc. |

---

## 📦 Requisitos

Instala las dependencias necesarias con:

```bash
pip install -r requirements.txt
```

---

## 🔍 Tipos de datos del archivo final

El archivo `planea_total.csv` consolidado en la ruta `output/planea/` contiene todas las columnas en formato **`object`**, sin aplicar conversión específica de tipos (por ejemplo, enteros o flotantes).

Esto se decidió así por dos razones principales:

1. **Robustez ante valores no numéricos**: Algunos campos como `'ENT'` o `'LENGUAJE_CANTIDAD_I'` pueden contener valores no numéricos (por ejemplo, `'S/D'`, `'_'` o celdas vacías) que complican la conversión directa.
2. **Evitar errores al leer en Excel o herramientas de análisis**: Dejar los datos como `object` garantiza una mayor compatibilidad inicial con herramientas como Excel o notebooks exploratorios.

> 💡 Si se requiere aplicar tipos específicos en fases posteriores, se recomienda realizar una limpieza controlada y luego usar `astype()` con validaciones.

---

## ✨ Próximos pasos

- Extender esquema y scripts a EXCALE/ENLACE (estructuras similares).

---
