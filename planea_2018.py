import pandas as pd
from pathlib import Path

from src.columnas_planea_2017 import columnas_estandar
from utils.logging_config import configurar_logger_planea

# Inicializa el logger
logger = configurar_logger_planea("consolidador_planea_2018", archivo_log="consolidador_planea.log")


# Inicializa acumulador
anio = 2018
base_dir = Path("data/raw/planea/2018")
df_total = pd.DataFrame()

logger.info("🚀 Iniciando consolidación de archivos 2018...")

for archivo_path in base_dir.glob("*.xlsx"):
    try:
        # Detectar el nombre de la única hoja
        hoja = pd.ExcelFile(archivo_path).sheet_names[0]
        df = pd.read_excel(archivo_path, sheet_name=hoja, header=None, skiprows=4)

        if df.shape[1] != len(columnas_estandar):
            logger.warning(f"⚠️  Columnas inesperadas en '{archivo_path.name}' [{hoja}]: {df.shape[1]} (esperadas: {len(columnas_estandar)})")
            continue

        df.columns = columnas_estandar
        df["ANIO_EVALUACION"] = anio
        df["ARCHIVO_ORIGEN"] = archivo_path.name

        logger.info(f"✅ Procesado: {archivo_path.name} [{hoja}] — {df.shape[0]} registros")
        df_total = pd.concat([df_total, df], ignore_index=True)

    except Exception as e:
        logger.error(f"❌ Error en '{archivo_path.name}' [{hoja}]: {e}")

# Guardar consolidado
Path("./output/planea").mkdir(parents=True, exist_ok=True)
output_path = Path("./output/planea/consolidado_2018.csv")
df_total.to_csv(output_path, index=False, encoding="utf-8-sig")

logger.info(f"\n📁 Consolidado 2018 generado: {output_path} — Total registros: {len(df_total)}")