import pandas as pd
import re
from pathlib import Path
import argparse

from src.schema_plenea import columnas_finales_planea
from utils.logging_config import configurar_logger_planea

# Argumentos desde línea de comandos
parser = argparse.ArgumentParser(description="Consolidar archivos PLANEA")
parser.add_argument("--forzar-lf", action="store_true", help="Usar lineterminator='\\n' para compatibilidad con Windows")
args = parser.parse_args()

# Logger
logger = configurar_logger_planea("consolidar_final", archivo_log="final_planea.log")

# Archivos fuente por año
archivos = {
    2015: "./output/planea/consolidado_2015.csv",
    2016: "./output/planea/consolidado_2016.csv",
    2017: "./output/planea/consolidado_2017.csv",
    2018: "./output/planea/consolidado_2018.csv"
}

df_consolidado = pd.DataFrame({col: pd.Series(dtype="object") for col in columnas_finales_planea})

for anio, ruta in archivos.items():
    try:
        df = pd.read_csv(ruta, encoding="utf-8-sig", low_memory=False)

        # Rellenar columnas faltantes
        columnas_faltantes = set(columnas_finales_planea) - set(df.columns)
        for col in columnas_faltantes:
            df[col] = pd.NA

        df = df[columnas_finales_planea]

        # Establecer tipos compatibles antes del concat
        df = df.astype(df_consolidado.dtypes.to_dict())

        logger.info(f"✅ Archivo {anio} cargado: {df.shape[0]} filas")

        df_consolidado = pd.concat([df_consolidado, df], ignore_index=True)

    except Exception as e:
        logger.error(f"❌ Error al procesar {ruta}: {e}")

# Guardar archivo final
Path("./output/planea").mkdir(parents=True, exist_ok=True)
salida = Path("./output/planea/planea_total.csv")

# Seleccionar si se usa lineterminator o no
csv_kwargs = {"index": False, "encoding": "utf-8-sig"}
if args.forzar_lf:
    csv_kwargs["lineterminator"] = "\n"

df_consolidado.to_csv(salida, **csv_kwargs)

logger.info(f"📁 Consolidado final guardado en: {salida} — Registros: {len(df_consolidado)}")
