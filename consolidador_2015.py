import pandas as pd
from pathlib import Path

from src.etl.columnas_2015 import columnas_estandar
from utils.logging_config import configurar_logger

# Inicializa el logger
logger = configurar_logger("consolidador_2015", archivo_log="consolidador_archivos.log")

# Diccionario de claves ENT a nombre de entidad
ENTIDADES = {
    1: "Aguascalientes", 2: "Baja California", 3: "Baja California Sur", 4: "Campeche",
    5: "Coahuila", 6: "Colima", 7: "Chiapas", 8: "Chihuahua", 9: "Ciudad de México",
    10: "Durango", 11: "Guanajuato", 12: "Guerrero", 13: "Hidalgo", 14: "Jalisco",
    15: "Estado de México", 16: "Michoacán", 17: "Morelos", 18: "Nayarit", 19: "Nuevo León",
    20: "Oaxaca", 21: "Puebla", 22: "Querétaro", 23: "Quintana Roo", 24: "San Luis Potosí",
    25: "Sinaloa", 26: "Sonora", 27: "Tabasco", 28: "Tamaulipas", 29: "Tlaxcala",
    30: "Veracruz", 31: "Yucatán", 32: "Zacatecas"
}

# Inicializa acumulador
anio = 2015
base_dir = Path("data/raw/2015")
df_total = pd.DataFrame()

logger.info("🚀 Iniciando consolidación de archivos 2015...")

for archivo_path in base_dir.glob("*.xlsx"):
    for hoja in ["primarias", "secundarias"]:
        try:
            df = pd.read_excel(archivo_path, sheet_name=hoja, header=None, skiprows=3)

            if df.shape[1] != len(columnas_estandar):
                logger.warning(f"⚠️  Columnas inesperadas en '{archivo_path.name}' [{hoja}]: {df.shape[1]} (esperadas: {len(columnas_estandar)})")
                continue

            df.columns = columnas_estandar
            df["ANIO_EVALUACION"] = anio
            df["ARCHIVO_ORIGEN"] = archivo_path.name
            df["ENTIDAD"] = df["ENT"].map(ENTIDADES)

            logger.info(f"✅ Procesado: {archivo_path.name} [{hoja}] — {df.shape[0]} registros")
            df_total = pd.concat([df_total, df], ignore_index=True)

        except Exception as e:
            logger.error(f"❌ Error en '{archivo_path.name}' [{hoja}]: {e}")

# Guardar consolidado
Path("output").mkdir(exist_ok=True)
output_path = Path("output/consolidado_2015.csv")
df_total.to_csv(output_path, index=False, encoding="latin1")

logger.info(f"\n📁 Consolidado 2015 generado: {output_path} — Total registros: {len(df_total)}")