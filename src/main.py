
import os
from audit import users, ports, updates
from utils.helpers import generate_report

def main():
    print("🔐 Iniciando auditoría de seguridad...")
    
    # Resultados por categoría
    user_report = users.audit_privileged_users()
    port_report = ports.audit_open_ports()
    updates_report = updates.audit_pending_updates()

    # Consolidar en diccionario
    findings = {
        "usuarios": user_report,
        "puertos": port_report,
        "actualizaciones": updates_report
    }

    # Generar informe
    output_path = os.path.join("outputs", "informe-auditoria.md")
    generate_report(findings, output_path)
    
    print(f"✅ Informe generado en: {output_path}")

if __name__ == "__main__":
    main()
