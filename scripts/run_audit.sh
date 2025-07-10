
#!/bin/bash

echo "🧪 Ejecutando Auditoría de Seguridad con linux-sec-auditor..."

# Verificar que se ejecuta desde la raíz del proyecto
cd "$(dirname "$0")/.."

# Crear carpeta de salida si no existe
mkdir -p outputs

# Ejecutar script principal
python3 src/main.py

# Verificar si se generó informe
if [ -f outputs/informe-auditoria.md ]; then
    echo "✅ Auditoría completada correctamente."
else
    echo "❌ No se pudo generar el informe."
fi
