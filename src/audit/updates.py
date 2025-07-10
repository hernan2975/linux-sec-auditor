
import subprocess

def audit_pending_updates():
    try:
        output = subprocess.check_output(
            ["apt", "list", "--upgradable"], text=True, stderr=subprocess.DEVNULL
        )
        findings = []
        lines = output.splitlines()[1:]  # Skip header

        for line in lines:
            pkg = line.split('/')[0].strip()
            findings.append({
                "paquete": pkg,
                "riesgo": "Alto",
                "detalle": f"El paquete '{pkg}' tiene una versión actualizable disponible."
            })

        return findings if findings else [{
            "paquete": "Todo actualizado",
            "riesgo": "Bajo",
            "detalle": "No se detectaron paquetes pendientes de actualización."
        }]

    except Exception as e:
        return [{
            "paquete": "Error",
            "riesgo": "Crítico",
            "detalle": f"No se pudo verificar actualizaciones: {e}"
        }]
