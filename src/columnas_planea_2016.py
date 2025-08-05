# Definición de columnas estandarizadas para bases PLANEA para 2016
# Agrupadas temáticamente para facilitar el análisis, mantenimiento y validación

#   1. Datos básicos de la escuela
columnas_datos_basicos = [
    "ENT",
    "ENTIDAD",
    "TIPO_ESCUELA",
    "GRADO_EVALUADO",
    "GRADO_MARGINACION",
    "CLAVE_ESCUELA",
    "TURNO",
    "NOMBRE_ESCUELA",
    "MUNICIPIO",
    "LOCALIDAD"
]

#   2. Participación en la prueba
columnas_participacion = [
    "ALUMNOS_PROGRAMADOS",
    "ALUMNOS_EVALUADOS_LENGUAJE",
    "ALUMNOS_EVALUADOS_MATEMATICAS"
]

#   3. Calidad de datos / confiabilidad
#      - Representatividad: Los alumnos evaluados son representativos de la totalidad de los estudiantes de la escuela
#      - Confiabilidad:     Se encontró un número excesivo de respuestas similares entre estudiantes que realizaron la prueba en la misma aula, de manera que la calidad de la información es poco confiable, por lo que los resultados en la misma deben ser tomados con reserva
columnas_calidad = [
    "CONFIABILIDAD_LENGUAJE",
    "CONFIABILIDAD_MATEMATICAS",
    "REPRESENTATIVIDAD_LENGUAJE",
    "REPRESENTATIVIDAD_MATEMATICAS"
]

#   4. Niveles de logro en lenguaje y comunicación: I, II, III y IV
#       - Porcentaje de alumnos en la escuela
columnas_lenguaje = [
    "LENGUAJE_PCT_I",
    "LENGUAJE_PCT_II",
    "LENGUAJE_PCT_III",
    "LENGUAJE_PCT_IV"
]

#   5. Niveles de logro en matemáticas: I, II, III y IV
#       - Porcentaje de alumnos en la escuela
columnas_matematicas = [
    "MATEMATICAS_PCT_I",
    "MATEMATICAS_PCT_II",
    "MATEMATICAS_PCT_III",
    "MATEMATICAS_PCT_IV"
]

#   Lista consolidada final
columnas_estandar = (
    columnas_datos_basicos +
    columnas_participacion +
    columnas_calidad +
    columnas_lenguaje +
    columnas_matematicas
)
