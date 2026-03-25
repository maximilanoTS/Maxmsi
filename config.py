"""
Configuración central para Maxmsi - Sistema de Detección de Malware
"""

import os
from pathlib import Path

# Rutas
PROJECT_ROOT = Path(__file__).parent
SCAN_RESULTS_DIR = PROJECT_ROOT / "scan_results"
LOG_DIR = PROJECT_ROOT / "logs"

# Crear directorios si no existen
SCAN_RESULTS_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

# Configuración de ClamAV
CLAMAV_CONFIG = {
    "engine": "clamav",
    "db_update_interval": 3600,  # Actualizar cada hora
    "max_filesize": 100 * 1024 * 1024,  # 100 MB máximo
    "timeout": 300,  # 5 minutos timeout
}

# Configuración de escaneo
SCAN_CONFIG = {
    "recursive": True,
    "follow_symlinks": False,
    "archive_scan": True,
    "exclude_extensions": [".pyc", ".pyo", ".pyd"],
    "verbosity": True,
}

# Configuración de reportes
REPORT_CONFIG = {
    "format": "json",  # json, txt, csv
    "include_timestamp": True,
    "include_hashes": True,
    "save_report": True,
}

# Integraciones opcionales
INTEGRATIONS = {
    "virustotal": {
        "enabled": False,
        "api_key": os.getenv("VIRUSTOTAL_API_KEY", ""),
    },
    "slack": {
        "enabled": False,
        "webhook_url": os.getenv("SLACK_WEBHOOK_URL", ""),
    },
}

# Niveles de severidad
SEVERITY_LEVELS = {
    "CRITICAL": 5,
    "HIGH": 4,
    "MEDIUM": 3,
    "LOW": 2,
    "INFO": 1,
}

# Extensiones peligrosas por defecto
DANGEROUS_EXTENSIONS = [
    ".exe", ".dll", ".scr", ".vbs", ".js",
    ".bat", ".cmd", ".com", ".pif", ".msi",
    ".app", ".deb", ".rpm", ".dmg", ".pkg"
]