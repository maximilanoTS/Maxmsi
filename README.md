# 🔒 Maxmsi - Sistema de Detección de Malware

Herramienta avanzada para detectar si un archivo contiene malware utilizando múltiples motores de análisis.

## 🎯 Características

- ✅ Escaneo de archivos individuales
- ✅ Escaneo recursivo de directorios
- ✅ Integración con ClamAV
- ✅ Reportes detallados
- ✅ GitHub Actions para CI/CD automático
- ✅ Análisis de hashes con VirusTotal (opcional)

## 📋 Requisitos

- Python 3.8+
- ClamAV instalado en el sistema
- pip para gestionar dependencias

## 🚀 Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/maximilanoTS/Maxmsi.git
cd Maxmsi
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
sudo apt-get update && sudo apt-get install clamav clamav-daemon -y  # Linux
brew install clamav  # macOS
```

### 3. Actualizar la base de datos de firmas
```bash
sudo freshclam
```

## 💻 Uso

### Escanear un archivo
```bash
python malware_detector.py scan --file /ruta/al/archivo
```

### Escanear un directorio
```bash
python malware_detector.py scan --directory /ruta/al/directorio
```

### Ver reportes
```bash
python malware_detector.py report --file /ruta/al/archivo
```

## 🔧 Configuración

Edita `config.py` para personalizar:
- Rutas de ClamAV
- Niveles de alerta
- Formatos de reporte
- Integraciones con servicios externos

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/NewFeature`)
3. Commit tus cambios (`git commit -m 'Add NewFeature'`)
4. Push a la rama (`git push origin feature/NewFeature`)
5. Abre un Pull Request

## 📞 Soporte

Para reportar problemas o vulnerabilidades, abre un [issue](https://github.com/maximilanoTS/Maxmsi/issues).

## 📄 Licencia

Este proyecto está bajo la licencia MIT.

---
**Última actualización:** 2026-03-25