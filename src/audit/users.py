
import subprocess

def audit_privileged_users():
    try:
        output = subprocess.check_output(['getent', 'group', 'sudo'], text=True)
        users = output.strip().split(':')[-1].split(',') if ':' in output else []
        findings = []

        for user in users:
            username = user.strip()
            if username:
                findings.append({
                    "usuario": username,
                    "riesgo": "Alto",
                    "detalle": f"Usuario '{username}' posee privilegios sudo."
                })

        if not findings:
            findings.append({
                "usuario": "Ninguno",
                "riesgo": "Bajo",
                "detalle": "No se detectaron usuarios con privilegios sudo."
            })

        return findings

    except subprocess.CalledProcessError as e:
        return [{
            "usuario": "Error",
            "riesgo": "Crítico",
            "detalle": f"No se pudo obtener el grupo sudo: {e}"
        }]
