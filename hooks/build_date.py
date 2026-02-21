"""
Hook MkDocs per aggiungere la data di build locale (Europe/Rome) al contesto del template.
"""

from datetime import datetime, timezone, timedelta


def on_env(env, config, files):
    """Aggiunge la variabile build_date_local al contesto globale Jinja."""
    # Fuso orario Europe/Rome (CET = UTC+1, CEST = UTC+2)
    utc_now = datetime.now(timezone.utc)

    # Calcola l'offset per l'ora legale italiana (ultima domenica di marzo - ultima domenica di ottobre)
    year = utc_now.year
    # Ultima domenica di marzo
    march_last = datetime(year, 3, 31, tzinfo=timezone.utc)
    dst_start = march_last - timedelta(days=(march_last.weekday() + 1) % 7)
    dst_start = dst_start.replace(hour=1)  # Cambio alle 01:00 UTC

    # Ultima domenica di ottobre
    oct_last = datetime(year, 10, 31, tzinfo=timezone.utc)
    dst_end = oct_last - timedelta(days=(oct_last.weekday() + 1) % 7)
    dst_end = dst_end.replace(hour=1)  # Cambio alle 01:00 UTC

    if dst_start <= utc_now < dst_end:
        rome_offset = timedelta(hours=2)  # CEST
    else:
        rome_offset = timedelta(hours=1)  # CET

    local_time = utc_now + rome_offset
    formatted = local_time.strftime("%d/%m/%Y %H:%M")

    env.globals["build_date_local"] = formatted
    return env
