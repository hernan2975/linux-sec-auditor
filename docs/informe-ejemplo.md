Este archivo será una plantilla de informe de auditoría en Markdown, diseñada para que los scripts puedan exportarlo directamente o servir como referencia visual.

✅ Propósito del archivo
Mostrar cómo se estructuran los resultados.

Facilitar revisión técnica post-auditoría.

Permitir exportación directa a HTML con estilo limpio.

# 🛡️ Informe de Auditoría de Seguridad – Servidor Linux

**Fecha de Auditoría:** 2025-07-10  
**Sistema Auditado:** servidor-prod-01.local  
**Sistema Operativo:** Ubuntu 22.04 LTS  
**Auditoría Ejecutada por:** linux-sec-auditor v1.0

---

## 📍 Hallazgos Detectados

| Categoría                 | Descripción                                     | Nivel de Riesgo |
|--------------------------|--------------------------------------------------|-----------------|
| Usuarios Privilegiados   | 3 usuarios con acceso sudo                      | Alto            |
| Puertos Abiertos         | SSH, HTTP, PostgreSQL abiertos al exterior      | Medio           |
| Actualizaciones Pendientes | OpenSSL y sudo sin actualizar                  | Alto            |
| Contraseñas Débiles      | 2 usuarios sin políticas de complejidad         | Alto            |

---

## 🔍 Análisis Técnico

### 🔐 Usuarios Privilegiados
- **Usuarios:** `admin`, `deploy`, `sysroot`
- Recomendación: validar su uso y aplicar MFA si es necesario.

### 🌐 Puertos Abiertos (`nmap`)
```bash
nmap -sS -Pn servidor-prod-01.local

22/tcp   open  ssh
80/tcp   open  http
5432/tcp open  postgresql

📦 Actualizaciones Pendientes

apt list --upgradable

-openssl: versión actual vulnerable
-sudo: versión sin parche CVE-2024-xxxx

🔑 Contraseñas Débiles (John the Ripper)

-Usuarios afectados: test1, legacy-admin
-Recomendación: habilitar pam_pwquality y hash robusto (SHA512)

✅ Recomendaciones Técnicas Automatizadas

📤 Exportación del Informe
Este informe se puede convertir a HTML con markdown2, Jinja2, o integrar en dashboards visuales.

Copia Markdown: outputs/informe-auditoria.md

Copia HTML: outputs/informe-auditoria.html

📎 Notas Finales
Este informe fue generado de forma automatizada con herramientas open-source, con enfoque en accesibilidad y escalabilidad para ambientes Linux.
