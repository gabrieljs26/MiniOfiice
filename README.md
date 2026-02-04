# 📝 Mini Office con Reconocimiento de Voz

Una aplicación de procesamiento de texto completa con reconocimiento de voz integrado usando PyAudio y SpeechRecognition.

## 🚀 Características

### Funcionalidades Básicas
- ✏️ Editor de texto con formato rico
- 📁 Abrir y guardar archivos (.txt)
- 🔍 Buscar y reemplazar texto
- 🎨 Personalización de colores (texto y fondo)
- 🖼️ Insertar imágenes
- ✂️ Operaciones: cortar, copiar, pegar
- ↩️ Deshacer y rehacer
- 📊 Contador de palabras y caracteres

### 🎤 Reconocimiento de Voz
**Atajo de teclado:** `Ctrl+R`

La aplicación puede:
1. **Transcribir voz a texto** - Habla normalmente y tu voz se convertirá en texto
2. **Ejecutar comandos de voz** - Di comandos especiales para activar funciones

## 📋 Comandos de Voz Disponibles

| Comando | Acción |
|---------|--------|
| **"negrita"** o **"bold"** | Activa/desactiva formato negrita |
| **"cursiva"** o **"itálica"** o **"italic"** | Activa/desactiva formato cursiva |
| **"subrayado"** o **"underline"** | Activa/desactiva formato subrayado |
| **"guardar archivo"** o **"guardar documento"** | Abre el diálogo para guardar |
| **"nuevo documento"** o **"documento nuevo"** | Crea un nuevo documento vacío |

## 🔧 Instalación

### Requisitos Previos
- Python 3.7 o superior
- Micrófono funcional

### Instalar Dependencias

```bash
pip install -r requirements.txt
```

O instalar manualmente:

```bash
pip install PySide6
pip install pyaudio
pip install SpeechRecognition
```

## ▶️ Uso

1. **Ejecutar la aplicación:**
   ```bash
   python MiniOffice.py
   ```

2. **Activar reconocimiento de voz:**
   - Presiona `Ctrl+R` o selecciona "🎤 Reconocimiento de voz" en el menú Personalizar
   - Espera a que aparezca "🎤 Escuchando... Habla ahora" en la barra de estado
   - Habla claramente al micrófono

3. **Usar comandos de voz:**
   - Di "negrita" para activar formato negrita
   - Di "guardar archivo" para guardar el documento
   - Etc.

4. **Transcribir texto:**
   - Simplemente habla y el texto se insertará donde esté el cursor

## 🎯 Ejemplos de Uso

### Ejemplo 1: Escribir y formatear con voz
1. Presiona `Ctrl+R`
2. Di: "negrita"
3. Presiona `Ctrl+R` de nuevo
4. Di: "Este es un título importante"
5. Resultado: **Este es un título importante**

### Ejemplo 2: Crear y guardar documento
1. Presiona `Ctrl+R` y di: "nuevo documento"
2. Presiona `Ctrl+R` y di: "Hola mundo, este es mi primer documento"
3. Presiona `Ctrl+R` y di: "guardar archivo"

## 🛠️ Tecnologías Utilizadas

- **PySide6**: Interfaz gráfica de usuario
- **PyAudio**: Captura de audio del micrófono
- **SpeechRecognition**: 
  - `Recognizer`: Calibra el ruido ambiente, escucha y procesa el audio
  - `Microphone`: Wrapper sobre PyAudio para abrir el micrófono
  - Reconocimiento mediante Google Speech Recognition API

## ⚡ Atajos de Teclado

| Atajo | Función |
|-------|---------|
| `Ctrl+N` | Nuevo documento |
| `Ctrl+O` | Abrir archivo |
| `Ctrl+S` | Guardar archivo |
| `Ctrl+Z` | Deshacer |
| `Ctrl+Y` | Rehacer |
| `Ctrl+X` | Cortar |
| `Ctrl+C` | Copiar |
| `Ctrl+V` | Pegar |
| `Ctrl+F` | Buscar/Reemplazar |
| `Ctrl+R` | 🎤 Reconocimiento de voz |
| `Ctrl+Q` | Salir |

## 📝 Notas

- El reconocimiento de voz requiere conexión a Internet (usa Google Speech Recognition)
- El micrófono debe estar correctamente configurado en tu sistema
- Los comandos de voz son case-insensitive (no distinguen mayúsculas/minúsculas)
- El tiempo máximo de escucha es de 15 segundos por comando
- Si no se detecta audio en 10 segundos, el reconocimiento se detendrá automáticamente

## 🐛 Solución de Problemas

**Error de PyAudio:**
Si tienes problemas instalando PyAudio en Windows, descarga el archivo `.whl` apropiado desde:
https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

**Micrófono no detectado:**
Verifica que:
- El micrófono esté conectado y configurado como dispositivo predeterminado
- Windows tenga permisos para acceder al micrófono
- El micrófono funcione en otras aplicaciones

**Reconocimiento impreciso:**
- Habla clara y pausadamente
- Reduce el ruido de fondo
- Acércate más al micrófono

- ### 🧩 Integración de Componentes
Se ha modularizado la funcionalidad de estadísticas mediante la integración del componente `contadorWidget`.
**Cambios realizados:**
- **Modularización:** Se sustituyó la lógica básica de conteo en [MiniOffice.py] por el widget especializado [WordCounterWidget].
- **Señales y Slots:** Implementación de un sistema de señales (`Signal`) para la comunicación reactiva entre el editor de texto y la barra de estado.
- **Nuevas Métricas:** Además del conteo de palabras y caracteres, ahora se calcula y visualiza el tiempo estimado de lectura en tiempo real.
- **Interfaz Fluida:** El widget se integra nativamente en la `QStatusBar` usando `addPermanentWidget` para una apariencia consistente.

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso educativo.

---
Desarrollado con Python, PySide6, PyAudio y SpeechRecognition


