
def generate_report(findings, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        file.write("# 🛡️ Informe de Auditoría de Seguridad – Servidor Linux\n\n")
        file.write("**Fecha de Auditoría:** 2025-07-10\n")
        file.write("**Sistema Auditado:** servidor-local\n")
        file.write("**Generado por:** linux-sec-auditor v1.0\n\n")
        file.write("---\n\n")

        # Sección: Hallazgos por categoría
        file.write("## 📍 Hallazgos Detectados\n\n")
        for category, items in findings.items():
            file.write(f"### 🔎 {category.capitalize()}\n")
            for item in items:
                nombre = item.get("usuario") or item.get("servicio") or item.get("paquete") or "Ítem"
                riesgo = item.get("riesgo", "No definido")
                detalle = item.get("detalle", "Sin detalles")
                file.write(f"- **{nombre}** — Riesgo: **{riesgo}**\n  - {detalle}\n")
            file.write("\n")

        file.write("---\n\n")
        file.write("## ✅ Recomendaciones Técnicas Automatizadas\n\n")
        file.write("| Hallazgo | Acción Sugerida |\n")
        file.write("|----------|-----------------|\n")
        file.write("| Usuarios Privilegiados | Verificar grupo `sudo`, aplicar MFA si corresponde |\n")
        file.write("| Puertos Abiertos | Configurar firewall (`ufw`), limitar IPs externas |\n")
        file.write("| Actualizaciones | Ejecutar `apt upgrade`, activar actualizaciones automáticas |\n")
        file.write("| Contraseñas Débiles | Aplicar políticas con `pam_pwquality`, usar SHA512 |\n")

        file.write("\n---\n\n")
        file.write("Este informe fue generado de forma automatizada y está diseñado para ser ampliado o exportado según necesidad.\n")

