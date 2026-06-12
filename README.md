# Panorama Global de la IA — 2026

![Actualización](https://img.shields.io/badge/Actualizado-Junio%202026-blue?style=for-the-badge)
![Herramientas](https://img.shields.io/badge/Herramientas-40%2B-success?style=for-the-badge)
![Licencia](https://img.shields.io/badge/Licencia-MIT-purple?style=for-the-badge)

> Informe interactivo del ecosistema de Inteligencia Artificial para el **Master en IA Aplicada**.  
> Benchmarks, precios, comparativas y más de 40 herramientas organizadas en 6 capas. **Actualizado: junio 2026.**

🔗 **[Ver informe en vivo → pjbarberoiglesias.github.io/Panorama-IA](https://pjbarberoiglesias.github.io/Panorama-IA/)**

---

## Póster del Ecosistema

> Infografía resumen de las 6 capas en una sola imagen. El informe interactivo incluye además una pestaña **Infografías** con liga de benchmarks, mapa de precios, cuadrante autonomía/privacidad e hitos del año.

![Infografía del ecosistema de la IA 2026](assets/infografia_ecosistema_2026.svg)

---

## El Ecosistema IA en 6 Capas

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryColor': '#1e1e2e', 'edgeLabelBackground': '#1e1e2e', 'lineColor': '#89b4fa'}}}%%
flowchart TB
    subgraph L6["CAPA 6 — Infraestructura Self-Hosted  |  PRIVACIDAD TOTAL"]
        direction LR
        Ollama["Self-Hosted\nOllama ⭐"] --- vLLM["Self-Hosted\nvLLM"] --- LMStudio["Self-Hosted\nLM Studio"] --- JanAI["Self-Hosted\nJan.ai"] --- llamacpp["Self-Hosted\nllama.cpp"]
    end
    subgraph L5["CAPA 5 — Frameworks de Agentes & MCP  |  DEV / TÉCNICO"]
        direction LR
        LangGraph["Framework\nLangGraph ⭐"] --- CrewAI["Framework\nCrewAI"] --- MSAF["Framework\nMS Agent Framework"] --- ClaudeSDK["Framework\nClaude Agent SDK"] --- MCP["Protocolo\nMCP ⭐"]
    end
    subgraph L4["CAPA 4 — Agentes IA Generales  |  ALTA AUTONOMÍA"]
        direction LR
        Manus["Agente\nManus ⭐"] --- ChatGPTAgent["Agente\nChatGPT Agent"] --- OpenClaw["Agente\nOpenClaw"] --- ManagedAgents["Agente\nManaged Agents"] --- DeepR["Agente\nDeep Research"]
    end
    subgraph L3["CAPA 3 — IDEs con IA & Agentes de Código  |  DEV / CÓDIGO"]
        direction LR
        CC["IDE & Agente\nClaude Code ⭐"] --- AG["IDE & Agente\nAntigravity 2.0 ⭐"] --- Cursor["IDE & Agente\nCursor"] --- Codex["IDE & Agente\nCodex"] --- DevinD["IDE & Agente\nDevin Desktop"]
    end
    subgraph L2["CAPA 2 — Asistentes IA  |  REACTIVOS → AGÉNTICOS"]
        direction LR
        ChatGPT["Asistente\nChatGPT"] --- ClaudeAI["Asistente\nClaude.ai"] --- GeminiA["Asistente\nGemini"] --- Copilot["Asistente\nCopilot"] --- Perp["Asistente\nPerplexity"]
    end
    subgraph L1["CAPA 1 — Modelos Fundacionales  |  CAPA BASE"]
        direction LR
        Cl["Modelo\nClaude Fable 5 / Opus 4.8"] --- GPT["Modelo\nGPT-5.5"] --- Gem["Modelo\nGemini 3.1 Pro"] --- DS["Modelo\nDeepSeek V4"] --- Kimi["Modelo\nKimi K2.6"]
    end

    L1 --> L2
    L1 --> L3
    L6 --> L1

    style L1 fill:#1e1b4b,stroke:#a855f7,color:#e9d5ff,stroke-width:2px
    style L2 fill:#172554,stroke:#3b82f6,color:#bfdbfe,stroke-width:2px
    style L3 fill:#064e3b,stroke:#10b981,color:#a7f3d0,stroke-width:2px
    style L4 fill:#431407,stroke:#f97316,color:#fed7aa,stroke-width:2px
    style L5 fill:#14532d,stroke:#22c55e,color:#bbf7d0,stroke-width:2px
    style L6 fill:#500724,stroke:#ec4899,color:#fbcfe8,stroke-width:2px
```

---

## Autonomía vs Privacidad

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'quadrantChart': {'quadrant1Fill': '#1e1e2e', 'quadrant2Fill': '#2a2a35', 'quadrant3Fill': '#1e1e2e', 'quadrant4Fill': '#2a2a35'}}}}%%
quadrantChart
    title Posicionamiento por Autonomia y Privacidad
    x-axis "Baja Autonomia" --> "Alta Autonomia"
    y-axis "Privacidad Nula" --> "Privacidad Total"
    quadrant-1 Autonomo y privado
    quadrant-2 Privado pero basico
    quadrant-3 Uso personal en la nube
    quadrant-4 Muy potente, datos en la nube
    Asistentes IA: [0.25, 0.08]
    Agentes de Codigo: [0.62, 0.30]
    Agentes Generales: [0.88, 0.10]
    Self-Hosted: [0.50, 0.92]
    Frameworks: [0.65, 0.65]
    OpenClaw self-hosted: [0.80, 0.85]
```

---

## Árbol del Ecosistema

```mermaid
%%{init: {'theme': 'dark'}}%%
mindmap
  root((Ecosistema IA 2026))
    Modelos LLM
      Anthropic
        Claude Fable 5 ⭐
        Claude Opus 4.8
        Claude Sonnet 4.6
        Claude Haiku 4.5
      OpenAI
        GPT-5.5 / 5.5 Pro
        GPT-5.4 / mini
      Google
        Gemini 3.1 Pro (2M ctx)
        Gemini 3.5 Flash
      xAI
        Grok 4.3
      Open Weights
        DeepSeek V4 Pro/Flash
        Kimi K2.6
        Qwen 3.6
        GLM-5.1
        Llama 4
        Mistral Large 3
    Asistentes
      ChatGPT (Agent mode)
      Claude.ai
      Gemini
      Microsoft Copilot
      Perplexity + Comet
      Grok
    IDEs & Agentes de Código
      Claude Code ⭐
      Antigravity 2.0 ⭐
      Cursor
      Codex (OpenAI)
      GitHub Copilot
      Devin / Devin Desktop
      Kiro · Zed · Aider · Junie
    Agentes Generales
      Manus ⭐
      ChatGPT Agent
      OpenClaw
      Claude Managed Agents
      Gemini Deep Research
    Frameworks
      LangChain / LangGraph
      CrewAI
      MS Agent Framework
      OpenAI Agents SDK
      Claude Agent SDK
      Google ADK
      MCP - estándar ⭐
    Self-Hosted
      Ollama ⭐
      vLLM
      LM Studio
      Jan.ai · LocalAI
      llama.cpp
```

---

## Benchmarks de Modelos LLM

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'xyChart': {'backgroundColor': '#1e1e2e', 'plotColorPalette': '#a855f7'}}}}%%
xychart-beta
    title "SWE-bench Verified % — Ingenieria de software real (mayor es mejor)"
    x-axis ["Fable 5", "Opus 4.8", "GPT-5.5", "Sonnet 4.6", "DeepSeek V4", "Gemini 3.1", "GPT-5.4", "Qwen 3.6", "GLM-5.1", "Grok 4.3"]
    y-axis 55 --> 100
    bar [95.0, 88.6, 86.0, 82.0, 80.6, 80.6, 80.0, 78.0, 77.0, 76.0]
```

---

## Precios de API (entrada, $/1M tokens)

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'xyChart': {'backgroundColor': '#1e1e2e', 'plotColorPalette': '#10b981'}}}}%%
xychart-beta
    title "Precio de API — Entrada $/1M tokens (menor es mejor)"
    x-axis ["Fable 5", "GPT-5.5", "Opus 4.8", "Sonnet 4.6", "Gemini 3.1", "Mistral L3", "Gemini 3.5F", "Grok 4.3", "DeepSeek V4", "Qwen 3.6"]
    y-axis 0 --> 12
    bar [10.0, 5.0, 5.0, 3.0, 2.0, 2.0, 1.5, 1.25, 0.6, 0.4]
```

---

## ¿Qué herramienta usar?

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryColor': '#1e1e2e', 'lineColor': '#89b4fa'}}}%%
flowchart LR
    NECESIDAD{{"Que necesito?"}}

    NECESIDAD -->|Pregunta puntual| ASIST["Asistente IA\nChatGPT · Claude.ai · Gemini"]
    NECESIDAD -->|Escribir / depurar codigo| IDE["Agente de código\nClaude Code · Cursor · Antigravity"]
    NECESIDAD -->|Tarea compleja autonoma| AGENTE["Agente General\nManus · ChatGPT Agent · OpenClaw"]
    NECESIDAD -->|Crear mis propios agentes| FW["Framework\nLangGraph · CrewAI · Claude Agent SDK"]
    NECESIDAD -->|Privacidad / sin coste API| SH["Self-Hosted\nOllama · vLLM · LM Studio"]

    style NECESIDAD fill:#1e1b4b,stroke:#a855f7,color:#e9d5ff,stroke-width:2px
    style ASIST fill:#172554,stroke:#3b82f6,color:#bfdbfe,stroke-width:2px
    style IDE fill:#064e3b,stroke:#10b981,color:#a7f3d0,stroke-width:2px
    style AGENTE fill:#431407,stroke:#f97316,color:#fed7aa,stroke-width:2px
    style FW fill:#14532d,stroke:#22c55e,color:#bbf7d0,stroke-width:2px
    style SH fill:#500724,stroke:#ec4899,color:#fbcfe8,stroke-width:2px
```

---

## Estructura del Proyecto

```
Panorama-IA/
├── index.html          ← Informe interactivo principal
├── README.md           ← Este archivo (con diagramas Mermaid)
└── assets/
    ├── panorama_ia_2026_resumen.md        ← Resumen en Markdown
    ├── infografia_ecosistema_2026.svg     ← Póster del ecosistema (SVG)
    └── panorama_ia_2026_*.png             ← Infografía (PNG)
```

## Secciones del Informe Interactivo

| # | Sección | Contenido |
|---|---------|-----------|
| 1 | Resumen | Las 6 capas del ecosistema IA con tooltips |
| 2 | Modelos LLM | 17 modelos con benchmarks ordenables (MMLU-Pro, GPQA Diamond, LiveCodeBench, AIME, SWE-bench Verified) |
| 3 | Herramientas | 40+ herramientas en 5 categorías con filtros |
| 4 | Precios | Suscripciones y precios de API de todos los proveedores |
| 5 | Matriz Comparativa | Selección y comparación lado a lado de 2+ elementos |
| 6 | Infografías | Póster del ecosistema, liga de benchmarks, mapa de precios, cuadrante autonomía/privacidad e hitos de 2026 |

## Historial de Versiones

| Fecha | Versión | Cambios |
|-------|---------|---------|
| Junio 2026 | v1.0 | Creación inicial del informe interactivo |
| Junio 2026 | v1.1 | Publicación en GitHub Pages + README con Mermaid |
| Junio 2026 | v2.0 | Actualización completa: 17 modelos (Claude Fable 5, GPT-5.5, Gemini 3.1...), nuevas herramientas (Antigravity 2.0, Devin Desktop, Kiro, MCP...), precios y benchmarks de junio 2026 |
| Junio 2026 | v2.1 | Nueva pestaña Infografías (póster del ecosistema, liga de benchmarks, mapa de precios, cuadrante autonomía/privacidad, hitos del año) + póster SVG en assets |

---

> El ecosistema IA evoluciona muy rápido. Esta foto es de **junio 2026**.  
> Repositorio: [github.com/pjbarberoiglesias/Panorama-IA](https://github.com/pjbarberoiglesias/Panorama-IA)
