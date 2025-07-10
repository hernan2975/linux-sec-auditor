
import subprocess

def audit_open_ports(target="127.0.0.1"):
    try:
        command = ["nmap", "-Pn", "-p-", target]
        output = subprocess.check_output(command, text=True)
        findings = []

        for line in output.splitlines():
            if "/tcp" in line and "open" in line:
                port_info = line.strip()
                findings.append({
                    "servicio": port_info,
                    "riesgo": "Medio",
                    "detalle": f"Puerto abierto detectado: {port_info}"
                })

        return findings if findings else [{
            "servicio": "Ninguno",
            "riesgo": "Bajo",
            "detalle": "No se encontraron puertos abiertos."
        }]

    except Exception as e:
        return [{
            "servicio": "Error",
            "riesgo": "Crítico",
            "detalle": f"Fallo al ejecutar nmap: {e}"
        }]
