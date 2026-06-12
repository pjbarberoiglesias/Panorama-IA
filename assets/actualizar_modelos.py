import re
import json
import urllib.request
from pathlib import Path

# Ruta al archivo HTML principal (ajusta si lo ejecutas desde otro directorio)
HTML_FILE = Path(__file__).parent.parent / 'index.html'

# Mapeo de tus IDs locales a los IDs reales futuros en la API de OpenRouter
# (He puesto los actuales equivalentes como ejemplo)
API_MAPPING = {
    'opus48': 'anthropic/claude-3-opus',
    'sonnet46': 'anthropic/claude-3.5-sonnet',
    'gpt55': 'openai/gpt-4o',
    'gpt54mini': 'openai/gpt-4o-mini',
    'gemini31pro': 'google/gemini-1.5-pro',
    'llama4': 'meta-llama/llama-3.3-70b-instruct',
    'deepseekv4': 'deepseek/deepseek-coder'
}

def actualizar_campo(model_id, campo, nuevo_valor):
    """Busca un modelo por su ID en el index.html y actualiza un campo específico."""
    with open(HTML_FILE, 'r', encoding='utf-8') as f:
        contenido = f.read()

    # Formatear el valor: si es texto (y no nulo/booleano), añadir comillas simples
    if isinstance(nuevo_valor, str) and not nuevo_valor.replace('.', '', 1).isdigit():
        if nuevo_valor not in ['null', 'true', 'false']:
            nuevo_valor = f"'{nuevo_valor}'"

    # Regex: Busca el id del modelo, avanza hasta encontrar el campo y captura su valor
    patron = r"(\{id:'" + model_id + r"'.*?,\s*" + campo + r"\s*:\s*)([^,}]+)(.*?\})"
    
    nuevo_contenido, reemplazos = re.subn(patron, r"\g<1>" + str(nuevo_valor) + r"\g<3>", contenido)

    if reemplazos > 0:
        with open(HTML_FILE, 'w', encoding='utf-8') as f:
            f.write(nuevo_contenido)
        print(f"✅ [{model_id}] {campo} actualizado -> {nuevo_valor}")
    else:
        print(f"⚠️ No se pudo encontrar el modelo '{model_id}' o el campo '{campo}'.")

def sincronizar_precios_api():
    """Se conecta a OpenRouter para obtener los precios y contexto reales actualizados."""
    print("🌐 Conectando a la API de OpenRouter...")
    req = urllib.request.Request("https://openrouter.ai/api/v1/models")
    
    try:
        with urllib.request.urlopen(req) as response:
            datos = json.loads(response.read().decode('utf-8'))
            modelos_api = {m['id']: m for m in datos['data']}
            
            for local_id, api_id in API_MAPPING.items():
                if api_id in modelos_api:
                    info = modelos_api[api_id]
                    # OpenRouter da precios por token, lo multiplicamos por 1M
                    precio_in = round(float(info['pricing']['prompt']) * 1_000_000, 3)
                    precio_out = round(float(info['pricing']['completion']) * 1_000_000, 3)
                    contexto = info['context_length']
                    
                    actualizar_campo(local_id, 'apiIn', precio_in)
                    actualizar_campo(local_id, 'apiOut', precio_out)
                    actualizar_campo(local_id, 'context', contexto)
                else:
                    print(f"❌ Modelo no encontrado en API: {api_id}")
    except Exception as e:
        print(f"Error en la API: {e}")

if __name__ == '__main__':
    print("🤖 Actualizador del Panorama IA")
    print("-" * 30)
    
    # EJEMPLO 1: Actualizar manualmente la nota de un benchmark
    # actualizar_campo('fable5', 'sweBench', 96.5)
    # actualizar_campo('grok43', 'apiIn', 1.00)
    
    # EJEMPLO 2: Sincronizar automáticamente con la API
    sincronizar_precios_api()