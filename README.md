# 🌐 Panorama Global de la IA — 2026

> Informe interactivo del ecosistema de Inteligencia Artificial para el **Master en IA Aplicada**.  
> Benchmarks, precios, comparativas y más de 40 herramientas organizadas en 6 capas.

🔗 **[Ver informe en vivo → pjbarberoiglesias.github.io/Panorama-IA](https://pjbarberoiglesias.github.io/Panorama-IA/)**

---

## 🗺️ El Ecosistema IA en 6 Capas

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#f0f4ff', 'edgeLabelBackground': '#ffffff'}}}%%
flowchart TB
    subgraph L6["🖥️ CAPA 6 — Infraestructura Self-Hosted  |  PRIVACIDAD TOTAL"]
        direction LR
        Ollama["🦙 Ollama ⭐"] --- LMStudio["🎛️ LM Studio"] --- LocalAI["🏠 LocalAI"] --- JanAI["🌙 Jan.ai"] --- llamacpp["⚙️ llama.cpp"]
    end
    subgraph L5["🔧 CAPA 5 — Frameworks Multi-Agente  |  DEV / TÉCNICO"]
        direction LR
        LangChain["🔗 LangChain"] --- LangGraph["📊 LangGraph"] --- CrewAI["👥 CrewAI"] --- AutoGen["🔄 AutoGen"] --- SK["🎯 Semantic Kernel"]
    end
    subgraph L4["🤖 CAPA 4 — Agentes IA Generales  |  ALTA AUTONOMÍA"]
        direction LR
        Manus["🤖 Manus ⭐"] --- OpenHands["🙌 OpenHands"] --- Operator["🌐 Operator"] --- DeepR["🔬 Deep Research"]
    end
    subgraph L3["💻 CAPA 3 — IDEs con IA & Agentes de Código  |  DEV / CÓDIGO"]
        direction LR
        AG["🚀 Antigravity ⭐"] --- Cursor["🖱️ Cursor"] --- WS["🏄 Windsurf"] --- CC["⌨️ Claude Code"] --- Codex["📦 Codex"]
    end
    subgraph L2["💬 CAPA 2 — Asistentes IA  |  REACTIVOS"]
        direction LR
        ChatGPT["🟢 ChatGPT"] --- ClaudeAI["🟠 Claude.ai"] --- GeminiA["🔷 Gemini"] --- Copilot["🟣 Copilot"] --- Perp["🔍 Perplexity"]
    end
    subgraph L1["🧠 CAPA 1 — Modelos Fundacionales  |  CAPA BASE"]
        direction LR
        GPT["GPT-4o/o3"] --- Cl["Claude 3.7"] --- Gem["Gemini 2.5"] --- Ll["Llama 3.3"] --- DS["DeepSeek V3/R1"]
    end

    L1 --> L2
    L1 --> L3
    L6 --> L1

    style L1 fill:#ede9fe,stroke:#7c3aed,color:#1e1b4b
    style L2 fill:#dbeafe,stroke:#2563eb,color:#1e3a5f
    style L3 fill:#d1fae5,stroke:#059669,color:#064e3b
    style L4 fill:#ffedd5,stroke:#ea580c,color:#431407
    style L5 fill:#dcfce7,stroke:#16a34a,color:#14532d
    style L6 fill:#fce7f3,stroke:#db2777,color:#500724
```

---

## 📊 Autonomía vs Privacidad

```mermaid
%%{init: {'theme': 'base'}}%%
quadrantChart
    title Posicionamiento por Autonomia y Privacidad
    x-axis "Baja Autonomia" --> "Alta Autonomia"
    y-axis "Privacidad Nula" --> "Privacidad Total"
    quadrant-1 Autonomo y privado
    quadrant-2 Privado pero basico
    quadrant-3 Uso personal en la nube
    quadrant-4 Muy potente, datos en la nube
    Asistentes IA: [0.15, 0.05]
    IDEs con IA: [0.45, 0.35]
    Agentes Generales: [0.85, 0.08]
    Self-Hosted: [0.50, 0.92]
    Frameworks: [0.62, 0.65]
```

---

## 🧠 Árbol del Ecosistema

```mermaid
mindmap
  root((🌐 Ecosistema IA 2026))
    🧠 Modelos LLM
      OpenAI
        GPT-4o
        o3 / o4-mini
      Anthropic
        Claude 3.7 Sonnet
        Claude 3.5 Haiku
      Google
        Gemini 2.5 Pro
        Gemini 2.0 Flash
        Gemma 3
      Open Source
        Llama 3.3 70B
        DeepSeek V3 / R1
        Mistral Large 2
        Qwen 2.5 / Phi-4
    💬 Asistentes
      ChatGPT
      Claude.ai
      Gemini
      Microsoft Copilot
      Perplexity
      Grok 3
    💻 IDEs con IA
      Antigravity ⭐
      Cursor
      Windsurf
      VS Code + Copilot
      Zed / Aider
      JetBrains AI
    🤖 Agentes Generales
      Manus ⭐
      OpenHands
      OpenAI Operator
      Gemini Deep Research
      AutoGPT
    🔧 Frameworks
      LangChain
      LangGraph
      CrewAI
      AutoGen
      Semantic Kernel
      OpenAI Agents SDK
    🖥️ Self-Hosted
      Ollama ⭐
      LM Studio
      LocalAI
      Jan.ai
      llama.cpp
```

---

## 🧪 Benchmarks de Modelos LLM

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'xyChart': {'backgroundColor': '#ffffff', 'plotColorPalette': '#7c3aed'}}}}%%
xychart-beta
    title "MMLU % — Conocimiento General (mayor es mejor)"
    x-axis ["o3/o4", "DeepSeek R1", "Gemini 2.5 Pro", "GPT-4o", "DeepSeek V3", "Claude 3.7", "Gemma 3", "Llama 3.3", "Qwen 2.5", "Phi-4"]
    y-axis 78 --> 99
    bar [96.7, 90.8, 89.0, 88.7, 88.5, 88.3, 82.2, 86.0, 86.7, 84.8]
```

---

## 💰 Precios de API (entrada, $/1M tokens)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'xyChart': {'backgroundColor': '#ffffff', 'plotColorPalette': '#059669'}}}}%%
xychart-beta
    title "Precio de API — Entrada $/1M tokens (menor es mejor)"
    x-axis ["o3", "Claude 3.7", "GPT-4o", "Mistral L2", "Gemini 2.5 Pro", "DeepSeek R1", "DeepSeek V3", "Llama 3.3", "Gemini Flash", "Phi-4"]
    y-axis 0 --> 12
    bar [10.0, 3.0, 2.5, 2.0, 1.25, 0.55, 0.27, 0.59, 0.10, 0.07]
```

---

## 🎯 ¿Qué herramienta usar?

```mermaid
%%{init: {'theme': 'base'}}%%
flowchart LR
    NECESIDAD{{"❓ Que necesito?"}}

    NECESIDAD -->|Pregunta puntual| ASIST["💬 Asistente IA\nChatGPT · Claude.ai · Gemini"]
    NECESIDAD -->|Escribir / depurar codigo| IDE["💻 IDE con IA\nAntigravity · Cursor · Windsurf"]
    NECESIDAD -->|Tarea compleja autonoma| AGENTE["🤖 Agente General\nManus · OpenHands · Operator"]
    NECESIDAD -->|Crear mis propios agentes| FW["🔧 Framework\nLangChain · CrewAI · AutoGen"]
    NECESIDAD -->|Privacidad / sin coste API| SH["🖥️ Self-Hosted\nOllama · LM Studio · LocalAI"]

    style NECESIDAD fill:#ede9fe,stroke:#7c3aed,color:#1e1b4b
    style ASIST fill:#dbeafe,stroke:#2563eb,color:#1e3a5f
    style IDE fill:#d1fae5,stroke:#059669,color:#064e3b
    style AGENTE fill:#ffedd5,stroke:#ea580c,color:#431407
    style FW fill:#dcfce7,stroke:#16a34a,color:#14532d
    style SH fill:#fce7f3,stroke:#db2777,color:#500724
```

---

## 📁 Estructura del Proyecto

```
1.Panorama IA/
├── index.html          ← Informe interactivo principal
├── README.md           ← Este archivo (con diagramas Mermaid)
└── assets/
    ├── panorama_ia_2026_resumen.md     ← Resumen en Markdown
    ├── panorama_ia_2026_*.png          ← Infografía (PNG)
    ├── panorama_ia_infografia_*.webp   ← Infografía completa
    └── panorama_ia_preview_*.webp      ← Preview del diagrama
```

## 🚀 Secciones del Informe Interactivo

| # | Sección | Contenido |
|---|---------|-----------|
| 1 | 🗺️ Resumen | Las 6 capas del ecosistema IA con tooltips |
| 2 | 🧠 Modelos LLM | 14 modelos con benchmarks ordenables (MMLU, GPQA, HumanEval, MATH, SWE-bench) |
| 3 | 🛠️ Herramientas | 40+ herramientas en 5 categorías con filtros |
| 4 | 💰 Precios | Suscripciones y precios de API de todos los proveedores |
| 5 | 📊 Matriz Comparativa | Selección y comparación lado a lado de 2+ elementos |

## 📅 Historial de Versiones

| Fecha | Versión | Cambios |
|-------|---------|---------|
| Junio 2026 | v1.0 | Creación inicial del informe interactivo |
| Junio 2026 | v1.1 | Publicación en GitHub Pages + README con Mermaid |

---

> ⚠️ El ecosistema IA evoluciona muy rápido. Esta foto es de **junio 2026**.  
> Repositorio: [github.com/pjbarberoiglesias/Panorama-IA](https://github.com/pjbarberoiglesias/Panorama-IA)
