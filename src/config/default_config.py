"""
Configuración por defecto del sistema
Valores heredados del proyecto anterior Horas-cat-v3
"""

# --- Feriados 2025 (Argentina) ---
# Formato YYYY-MM-DD
HOLIDAYS_2025 = [
    "2025-01-01",  # Año Nuevo

    "2025-03-01",  # Inicio del Ramadán
    "2025-03-03",  # Carnaval
    "2025-03-04",  # Carnaval
    "2025-03-24",  # Día Nacional de la Memoria por la Verdad y la Justicia
    "2025-03-30",  # Culminación del Ayuno

    "2025-04-02",  # Día del Veterano y de los Caídos en la Guerra de Malvinas
    "2025-04-12",  # Pascuas Judías
    "2025-04-13",  # Pascuas Judías
    "2025-04-14",  # Pascuas Judías
    "2025-04-17",  # Jueves Santo
    "2025-04-18",  # Pascuas Judías | Viernes Santo
    "2025-04-19",  # Pascuas Judías
    "2025-04-20",  # Domingo de Pascua | Último Día del Pésaj
    "2025-04-24",  # Día de acción por la tolerancia y el respeto entre los pueblos

    "2025-05-01",  # Día del Trabajo
    "2025-05-02",  # Puente Turístico
    "2025-05-25",  # Primer Gobierno Patrio

    "2025-06-07",  # Fiesta del Sacrificio (provisional)
    "2025-06-16",  # Conmemoración de General Don Martín Miguel de Güemes
    "2025-06-17",  # Conmemoración de General Don Martín Miguel de Güemes
    "2025-06-20",  # Paso a la Inmortalidad del General Manuel Belgrano
    "2025-06-27",  # Año Nuevo Islámico (provisional)

    "2025-07-09",  # Día de la Independencia

    "2025-08-15",  # Puente Turístico
    "2025-08-18",  # Paso a la Inmortalidad del General José de San Martín

    "2025-10-12",  # Dia de la Raza
    "2025-10-19",  # Día de la Madre

    "2025-11-21",  # Puente Turístico
    "2025-11-24",  # Día de la Soberanía Nacional

    "2025-12-08",  # Inmaculada Concepción de María
    "2025-12-25",  # Navidad
    "2025-12-31",  # Fiesta de Fin de Año
]

# Mapa de nombres de feriados 2025
HOLIDAY_NAMES_2025 = {
    "2025-01-01": "Año Nuevo",

    "2025-03-01": "Inicio del Ramadán",
    "2025-03-03": "Carnaval",
    "2025-03-04": "Carnaval",
    "2025-03-24": "Día Nacional de la Memoria por la Verdad y la Justicia",
    "2025-03-30": "Culminación del Ayuno",

    "2025-04-02": "Día del Veterano y de los Caídos en la Guerra de Malvinas",
    "2025-04-12": "Pascuas Judías",
    "2025-04-13": "Pascuas Judías",
    "2025-04-14": "Pascuas Judías",
    "2025-04-17": "Jueves Santo",
    "2025-04-18": "Pascuas Judías | Viernes Santo",
    "2025-04-19": "Pascuas Judías",
    "2025-04-20": "Domingo de Pascua | Último Día del Pésaj",
    "2025-04-24": "Día de acción por la tolerancia y el respeto entre los pueblos",

    "2025-05-01": "Día del Trabajo",
    "2025-05-02": "Puente Turístico",
    "2025-05-25": "Primer Gobierno Patrio",

    "2025-06-07": "Fiesta del Sacrificio (provisional)",
    "2025-06-16": "Conmemoración de General Don Martín Miguel de Güemes",
    "2025-06-17": "Conmemoración de General Don Martín Miguel de Güemes",
    "2025-06-20": "Paso a la Inmortalidad del General Manuel Belgrano",
    "2025-06-27": "Año Nuevo Islámico (provisional)",

    "2025-07-09": "Día de la Independencia",

    "2025-08-15": "Puente Turístico",
    "2025-08-18": "Paso a la Inmortalidad del General José de San Martín",

    "2025-10-12": "Dia de la Raza",
    "2025-10-19": "Día de la Madre",

    "2025-11-21": "Puente Turístico",
    "2025-11-24": "Día de la Soberanía Nacional",

    "2025-12-08": "Inmaculada Concepción de María",
    "2025-12-25": "Navidad",
    "2025-12-31": "Fiesta de Fin de Año",
}



DEFAULT_CONFIG = {
    # API
    'api_key': 'NTgyNTM5NTpuYzhJSXFQNEUzeXZNcndpNzVCR3ZJYm4wTkJ2aWpXTg==',
    'base_url': 'https://api-prod.humand.co/public/api/v1',

    "local_timezone": "America/Argentina/Buenos_Aires",



    "hora_viatico1_comida1": 6, 
    # Jornada
    'jornada_completa_horas': 8,
    'tolerancia_minutos': 20,
    'fragmento_minutos': 30,

    # Horarios especiales
    'hora_nocturna_inicio': 21,  # 21:00
    'hora_nocturna_fin': 6,      # 06:00
    'sabado_limite_hora': 13,

    # Zona horaria
    'timezone': 'America/Argentina/Buenos_Aires',

    # Red/Requests
    'max_retries': 3,
    'retry_delay': 1000,
    'request_timeout': 30000,

    # Paralelismo
    'max_workers': 6,
    'batch_size_users': 10,
    'batch_size_dates': 7,
    'delay_between_retries': 1000,
    'delay_between_batches': 500,

    # Archivos
    'output_directory': '~/Downloads',
    'filename_format': 'reporte_{start_date}_{end_date}.xlsx',

    # UI
    'window_width': 800,
    'window_height': 600,
    'theme': 'default',

    # Feriados
    'holidays': HOLIDAYS_2025,
    'holiday_names': HOLIDAY_NAMES_2025,
}

# Headers API
def get_api_headers(api_key=None):
    if api_key is None:
        api_key = DEFAULT_CONFIG['api_key']
    return {
        'Authorization': f'Basic {api_key}',
        'Content-Type': 'application/json'
    }

# Endpoints
API_ENDPOINTS = {
    'users': '/users',
    'time_tracking_entries': '/time-tracking/entries',
    'day_summaries': '/time-tracking/day-summaries'
}


