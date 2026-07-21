# SEOS

### Software Engineering Operating System

> **Una Plataforma Autónoma de Ingeniería de Software Orquestada por IA**
>
> **Analiza • Diseña • Construye • Refactoriza • Documenta • Prueba • Despliega • Ejecuta**

---

![Versión](https://img.shields.io/badge/Versión-v3.0.0-blue)

![Licencia](https://img.shields.io/badge/Licencia-MIT-green)

![Python](https://img.shields.io/badge/Python-3.10+-yellow)

![Estado](https://img.shields.io/badge/Estado-Estable-success)

---

**🇺🇸 [Read in English](README.md)**

---

# 🚀 ¿Qué es SEOS?

SEOS (**Software Engineering Operating System**) es una plataforma **Local-First**, orquestada por IA, diseñada para asistir a los ingenieros de software durante todo el ciclo de vida del desarrollo.

A diferencia de los asistentes tradicionales, SEOS ejecuta flujos completos de ingeniería de software de forma autónoma.

---

# ⚡ El Cambio de Paradigma (v3.0.0)

SEOS ya no es simplemente un chat con IA.

Es un **Motor Autónomo de Ingeniería de Software**.

En lugar de mostrar el código generado en pantalla para copiar y pegar manualmente, SEOS escribe directamente los artefactos generados dentro del proyecto, respetando su arquitectura, estructura y convenciones.

---

# ✨ Características Actuales (v3.0.0)

## 🤖 Ejecución Autónoma

- Generación automática de archivos
- Extracción automática de código desde JSON
- Extracción automática desde Markdown
- Escritura directa de archivos en el proyecto

---

## 🧠 IA Multi-Proveedor

Compatible con proveedores locales y en la nube, con seguimiento de consumo de tokens.

### Local

- LM Studio
- Ollama

### Nube

- OpenAI
- Claude
- Gemini

---

## 📁 Inteligencia del Workspace

- Gestión de múltiples proyectos
- Navegación del workspace
- Comprensión del contexto del proyecto
- Análisis de código mediante AST

Lenguajes soportados:

- Python
- Java
- JavaScript
- C#
- Rust
- Perl

---

## 📄 Motor de Documentos

- Traducción por lotes
- Resúmenes automáticos
- Reescritura de documentos
- Conservación del formato original

---

## 🏗 Fábrica de Software

- Generación de código
- Generación de APIs
- Generación de bases de datos
- Refactorización segura
- Generación automática de pruebas

---

## 🤝 Flujos Multi-Agente

Flujos de trabajo autónomos coordinados por agentes especializados.

Ejemplo:

```text
Usuario

 │

 ▼

Arquitecto

 │

 ▼

Desarrollador

 │

 ▼

Revisor

 │

 ▼

Tester

 │

 ▼

Documentación

 │

 ▼

Sprint Completado
```

---

## 🧠 RAG y Memoria

- Integración con ChromaDB
- Búsqueda semántica de código
- Memoria conversacional

---

## 🔍 Inteligencia del Proyecto

- Grafo de dependencias
- Análisis de impacto
- Detección de código muerto
- Generación de diagramas de secuencia

---

## 🔌 Integraciones

- API REST
- API de GitHub
- Extensión para VS Code
- Cliente MCP

---

## 🧩 Sistema de Plugins

- Carga dinámica de plugins
- Instalación directa desde repositorios Git

---

# ⚡ Inicio Rápido

Clona el repositorio.

```bash
git clone https://github.com/your-org/seos.git

cd seos
```

---

## Crear un Entorno Virtual

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## Instalación

```bash
pip install -e .
```

---

## Configuración

Copia el archivo de configuración.

```text
.env.example → .env
```

Configura:

- `LLM_PROVIDER`
- Llaves API del proveedor seleccionado
- `SEOS_API_KEY`

---

# ▶ Uso

## Modo Interactivo

```bash
seos
```

---

## Modo Headless

```bash
seos --headless
```

---

# 💬 Comandos Principales

| Comando | Descripción |
|----------|-------------|
| `/chat <mensaje>` | Conversa con SEOS. Cuando corresponde, el código generado se escribe automáticamente en el proyecto. |
| `/sprint <requerimiento>` | Ejecuta un flujo de desarrollo autónomo coordinado por múltiples agentes. |
| `/write [ruta/archivo.ext]` | Extrae el código generado de la última respuesta y lo guarda en un archivo. |
| `/sequence <archivo>` | Genera un diagrama de secuencia Mermaid a partir del flujo del código. |
| `/impact <archivo>` | Analiza el impacto de dependencias dentro del proyecto. |
| `/translate <carpeta> <idioma>` | Traduce documentos por lotes. |
| `/help [comando]` | Muestra la ayuda detallada de un comando. |

---

# 📄 Licencia

Distribuido bajo la **Licencia MIT**.

Consulta el archivo **LICENSE** para obtener más información.
