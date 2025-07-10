
#!/bin/bash

echo "🚀 Iniciando Auditoría en contenedor Docker..."

# Crear directorio de salida si no existe
mkdir -p /app/outputs

# Ejecutar flujo principal de auditoría
python3 /app/src/main.py

# Verificación de éxito
if [ -f /app/outputs/informe-auditoria.md ]; then
    echo "✅ Informe generado correctamente dentro del contenedor."
else
    echo "❌ Error al generar el informe. Revisa los logs."
fi
