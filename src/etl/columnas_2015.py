# Definición de columnas estandarizadas para bases PLANEA para 2015
# Agrupadas temáticamente para facilitar el análisis, mantenimiento y validación

#   1. Datos básicos de la escuela
columnas_datos_basicos = [
    "ENT",
    "NOMBRE_ESCUELA",
    "CLAVE_ESCUELA",
    "TURNO",
    "MUNICIPIO",
    "LOCALIDAD",
    "TIPO_ESCUELA",
    "GRADO_EVALUADO",
    "GRADO_MARGINACION"
]

#   2. Participación en la prueba
columnas_participacion = [
    "ALUMNOS_PROGRAMADOS",
    "ALUMNOS_EVALUADOS_LENGUAJE",
    "ALUMNOS_EVALUADOS_MATEMATICAS",
    "PORCENTAJE_EVALUADOS_LENGUAJE",
    "PORCENTAJE_EVALUADOS_MATEMATICAS"
]

#   3. Calidad de datos / confiabilidad
#      - Representatividad: Los alumnos evaluados son representativos de la totalidad de los estudiantes de la escuela
#      - Confiabilidad:     Se encontró un número excesivo de respuestas similares entre estudiantes que realizaron la prueba en la misma aula, de manera que la calidad de la información es poco confiable, por lo que los resultados en la misma deben ser tomados con reserva
columnas_calidad = [
    "REPRESENTATIVIDAD_LENGUAJE",
    "REPRESENTATIVIDAD_MATEMATICAS",
    "CONFIABILIDAD_LENGUAJE",
    "CONFIABILIDAD_MATEMATICAS"
]

#   4. Información contextual
#       - Escuelas parecidas para comparación
columnas_contexto = [
    "ESCUELAS_PARECIDAS"
]

#   5. Niveles de logro en lenguaje y comunicación: I, II, III y IV
#       - Cantidad de alumnos en la escuela
#       - Porcentaje de alumnos en la escuela
#       - Porcentaje de alumnos en escuelas parecidas
#       - Porcentaje de alumnos en todas las escuelas de México
columnas_lenguaje = [
    "LENGUAJE_CANTIDAD_I",
    "LENGUAJE_CANTIDAD_II",
    "LENGUAJE_CANTIDAD_III",
    "LENGUAJE_CANTIDAD_IV",
    "LENGUAJE_PCT_I",
    "LENGUAJE_PCT_II",
    "LENGUAJE_PCT_III",
    "LENGUAJE_PCT_IV",
    "LENGUAJE_PARECIDAS_PCT_I",
    "LENGUAJE_PARECIDAS_PCT_II",
    "LENGUAJE_PARECIDAS_PCT_III",
    "LENGUAJE_PARECIDAS_PCT_IV",
    "LENGUAJE_NACIONAL_PCT_I",
    "LENGUAJE_NACIONAL_PCT_II",
    "LENGUAJE_NACIONAL_PCT_III",
    "LENGUAJE_NACIONAL_PCT_IV"
]

#   6. Niveles de logro en matemáticas
#       - Cantidad de alumnos en la escuela
#       - Porcentaje de alumnos en la escuela
#       - Porcentaje de alumnos en escuelas parecidas
#       - Porcentaje de alumnos en todas las escuelas de México
columnas_matematicas = [
    "MATEMATICAS_CANTIDAD_I",
    "MATEMATICAS_CANTIDAD_II",
    "MATEMATICAS_CANTIDAD_III",
    "MATEMATICAS_CANTIDAD_IV",
    "MATEMATICAS_PCT_I",
    "MATEMATICAS_PCT_II",
    "MATEMATICAS_PCT_III",
    "MATEMATICAS_PCT_IV",
    "MATEMATICAS_PARECIDAS_PCT_I",
    "MATEMATICAS_PARECIDAS_PCT_II",
    "MATEMATICAS_PARECIDAS_PCT_III",
    "MATEMATICAS_PARECIDAS_PCT_IV",
    "MATEMATICAS_NACIONAL_PCT_I",
    "MATEMATICAS_NACIONAL_PCT_II",
    "MATEMATICAS_NACIONAL_PCT_III",
    "MATEMATICAS_NACIONAL_PCT_IV"
]

#   7. Percepción de los alumnos sobre sus recursos familiares asociados al bienestar por tipo
#       - Cantidad de alumnos en la escuela
#       - Porcentaje de alumnos en la escuela
#       - Porcentaje de alumnos en escuelas parecidas
#       - Porcentaje de alumnos en todas las escuelas de México
columnas_bienestar = [
    "PERCEPCION_BIENESTAR_CANTIDAD_1",
    "PERCEPCION_BIENESTAR_CANTIDAD_2",
    "PERCEPCION_BIENESTAR_CANTIDAD_3",
    "PERCEPCION_BIENESTAR_CANTIDAD_4",
    "PERCEPCION_BIENESTAR_PCT_1",
    "PERCEPCION_BIENESTAR_PCT_2",
    "PERCEPCION_BIENESTAR_PCT_3",
    "PERCEPCION_BIENESTAR_PCT_4",
    "PERCEPCION_BIENESTAR_PARECIDAS_PCT_1",
    "PERCEPCION_BIENESTAR_PARECIDAS_PCT_2",
    "PERCEPCION_BIENESTAR_PARECIDAS_PCT_3",
    "PERCEPCION_BIENESTAR_PARECIDAS_PCT_4",
    "PERCEPCION_BIENESTAR_NACIONAL_PCT_1",
    "PERCEPCION_BIENESTAR_NACIONAL_PCT_2",
    "PERCEPCION_BIENESTAR_NACIONAL_PCT_3",
    "PERCEPCION_BIENESTAR_NACIONAL_PCT_4"
]

#   8. Porcentaje de escuelas en cada grado de marginación
#       - En escuelas parecidas: Bajo y Muy Bajo, Medio, Muy Alto y Alto
#       - En todas las escuelas de México: Bajo y Muy Bajo, Medio, Muy Alto y Alto
columnas_marginacion = [
    "MARGINACION_PARECIDAS_ALTO",
    "MARGINACION_PARECIDAS_MEDIO",
    "MARGINACION_PARECIDAS_BAJO",
    "MARGINACION_NACIONAL_ALTO",
    "MARGINACION_NACIONAL_MEDIO",
    "MARGINACION_NACIONAL_BAJO"
]

#   Lista consolidada final
columnas_estandar = (
    columnas_datos_basicos +
    columnas_participacion +
    columnas_calidad +
    columnas_contexto +
    columnas_lenguaje +
    columnas_matematicas +
    columnas_bienestar +
    columnas_marginacion
)
