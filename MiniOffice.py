from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QToolBar, QFileDialog,
    QMessageBox, QColorDialog, QFontDialog, QWidget, QVBoxLayout, QLabel,
    QLineEdit, QPushButton, QCheckBox, QHBoxLayout, QStatusBar
)
from PySide6.QtGui import QAction, QIcon, QTextCursor, QFont, QTextImageFormat, QTextDocument
from PySide6.QtCore import QSize
import sys

class MiniOffice(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini Office Completo")
        self.resize(1000, 600)

        
        self.text_edit = QTextEdit()
        self.text_edit.setFont(QFont("Arial", 12))
        self.font_size = 12
        self.text_edit.textChanged.connect(self.actualizar_contador_palabras)

      
        self.panel_buscar = QWidget()
        self.panel_buscar.setFixedWidth(280)
        self.panel_buscar_layout = QVBoxLayout()
        self.panel_buscar.setLayout(self.panel_buscar_layout)
        self.panel_buscar.setVisible(False)

        self.input_buscar = QLineEdit()
        self.input_buscar.setPlaceholderText("Buscar...")
        self.panel_buscar_layout.addWidget(QLabel("Buscar:"))
        self.panel_buscar_layout.addWidget(self.input_buscar)

        self.input_reemplazar = QLineEdit()
        self.input_reemplazar.setPlaceholderText("Reemplazar con...")
        self.panel_buscar_layout.addWidget(QLabel("Reemplazar:"))
        self.panel_buscar_layout.addWidget(self.input_reemplazar)

        self.chk_reemplazar_todos = QCheckBox("Reemplazar todos")
        self.panel_buscar_layout.addWidget(self.chk_reemplazar_todos)

        btn_layout_buscar = QHBoxLayout()
        self.btn_buscar_arriba = QPushButton("Buscar ↑")
        self.btn_buscar_abajo = QPushButton("Buscar ↓")
        btn_layout_buscar.addWidget(self.btn_buscar_arriba)
        btn_layout_buscar.addWidget(self.btn_buscar_abajo)
        self.panel_buscar_layout.addLayout(btn_layout_buscar)

        btn_layout_reemplazar = QHBoxLayout()
        self.btn_reemplazar = QPushButton("Reemplazar")
        btn_layout_reemplazar.addWidget(self.btn_reemplazar)
        self.panel_buscar_layout.addLayout(btn_layout_reemplazar)

        self.btn_buscar_arriba.clicked.connect(lambda: self.buscar_texto_panel(True))
        self.btn_buscar_abajo.clicked.connect(lambda: self.buscar_texto_panel(False))
        self.btn_reemplazar.clicked.connect(self.reemplazar_texto_panel)

        main_layout = QHBoxLayout()
        main_widget = QWidget()
        main_layout.addWidget(self.text_edit)
        main_layout.addWidget(self.panel_buscar)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        self.barra_estado = QStatusBar()
        self.setStatusBar(self.barra_estado)
        self.etiqueta_contador = QLabel("Palabras: 0 | Caracteres: 0")
        self.barra_estado.addPermanentWidget(self.etiqueta_contador)
        
     
        self.barra_estado.showMessage("Listo. Presiona Ctrl+N para crear un nuevo documento.")

        menu_bar = self.menuBar()
        
        self.archivo_menu = menu_bar.addMenu("&Archivo")
        self.editar_menu = menu_bar.addMenu("&Editar")
        self.personalizar_menu = menu_bar.addMenu("&Personalizar")

  
        barra_herramientas = QToolBar("Barra de herramientas")
        barra_herramientas.setIconSize(QSize(16, 16))
        self.addToolBar(barra_herramientas)

        acciones_archivo = {
            "Nuevo": ("document-new", self.nuevo_documento, "Ctrl+N"),
            "Abrir": ("document-open", self.abrir_archivo, "Ctrl+O"),
            "Guardar": ("document-save", self.guardar_archivo, "Ctrl+S"),
            "Salir": ("application-exit", self.close, "Ctrl+Q")
        }
        for nombre, (icono, func, atajo) in acciones_archivo.items():
            accion = QAction(nombre, self)
            try:
                accion.setIcon(QIcon.fromTheme(icono))
            except:
                pass
            accion.triggered.connect(func)
            accion.setShortcut(atajo)
            self.archivo_menu.addAction(accion)
            barra_herramientas.addAction(accion)
        barra_herramientas.addSeparator()

  
        acciones_editar = {
            "Deshacer": ("edit-undo", self.text_edit.undo, "Ctrl+Z"),
            "Rehacer": ("edit-redo", self.text_edit.redo, "Ctrl+Y"),
            "Cortar": ("edit-cut", self.text_edit.cut, "Ctrl+X"),
            "Copiar": ("edit-copy", self.text_edit.copy, "Ctrl+C"),
            "Pegar": ("edit-paste", self.text_edit.paste, "Ctrl+V"),
            "Buscar/Reemplazar": ("edit-find", self.mostrar_panel_buscar, "Ctrl+F")
        }
        for nombre, (icono, func, atajo) in acciones_editar.items():
            accion = QAction(nombre, self)
            try:
                accion.setIcon(QIcon.fromTheme(icono))
            except:
                pass
            accion.triggered.connect(func)
            if atajo:
                accion.setShortcut(atajo)
            self.editar_menu.addAction(accion)
            barra_herramientas.addAction(accion)
        barra_herramientas.addSeparator()

     
        acciones_personalizar = {
            "Color de texto": ("format-text-color", self.color_palabra, None),
            "Color de fondo": ("format-fill-color", self.color_fondo, None),
            "Tipo de letra": ("preferences-desktop-font", self.tipo_letra, None),
            "Insertar imagen": ("insert-image", self.insertar_imagen, None)
        }
        for nombre, (icono, func, atajo) in acciones_personalizar.items():
            accion = QAction(nombre, self)
            try:
                accion.setIcon(QIcon.fromTheme(icono))
            except:
                pass
            accion.triggered.connect(func)
            if atajo:
                accion.setShortcut(atajo)
            self.personalizar_menu.addAction(accion)
            barra_herramientas.addAction(accion)

        
        self.actualizar_contador_palabras()

   
    def actualizar_contador_palabras(self):
        texto = self.text_edit.toPlainText()
        palabras = len(texto.split())
        caracteres = len(texto)
        self.etiqueta_contador.setText(f"Palabras: {palabras} | Caracteres: {caracteres}")

    
    def nuevo_documento(self):
        self.text_edit.clear()
        self.barra_estado.showMessage("Documento vacío creado.")
        QMessageBox.information(self, "Nuevo", "Documento vacío creado.")

    def abrir_archivo(self):
        ruta, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Archivos de texto (*.txt)")
        if ruta:
            try:
                with open(ruta, "r", encoding="utf-8") as f:
                    self.text_edit.setPlainText(f.read())
                self.barra_estado.showMessage(f"Archivo abierto: {ruta}")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"No se pudo abrir el archivo:\n{str(e)}")
                self.barra_estado.showMessage(f"Error al abrir el archivo: {str(e)}")

    def guardar_archivo(self):
        ruta, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Archivos de texto (*.txt)")
        if ruta:
            try:
                with open(ruta, "w", encoding="utf-8") as f:
                    f.write(self.text_edit.toPlainText())
                mensaje = f"Archivo guardado en: {ruta}"
                self.barra_estado.showMessage(mensaje)
                QMessageBox.information(self, "Guardar", mensaje)
            except Exception as e:
                mensaje_error = f"No se pudo guardar el archivo: {str(e)}"
                QMessageBox.warning(self, "Error", mensaje_error)
                self.barra_estado.showMessage(mensaje_error)

  
    def color_palabra(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.text_edit.setTextColor(color)
            self.barra_estado.showMessage("Color de texto cambiado")

    def color_fondo(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.text_edit.setStyleSheet(f"background-color: {color.name()};")
            self.barra_estado.showMessage("Color de fondo cambiado")

    def tipo_letra(self):

        dialog = QFontDialog(self)
        dialog.setCurrentFont(self.text_edit.currentFont())
        
        if dialog.exec() == QFontDialog.DialogCode.Accepted:
            fuente_seleccionada = dialog.selectedFont()
            if fuente_seleccionada:
               
                cursor = self.text_edit.textCursor()
                if cursor.hasSelection():
           
                    formato = cursor.charFormat()
                    formato.setFont(fuente_seleccionada)
                    cursor.setCharFormat(formato)
                    self.barra_estado.showMessage("Fuente aplicada al texto seleccionado")
                else:
       
                    self.text_edit.setCurrentFont(fuente_seleccionada)
                    self.barra_estado.showMessage("Fuente cambiada para todo el documento")

    def insertar_imagen(self):
        ruta, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen", "", "Imágenes (*.png *.jpg *.bmp *.gif)")
        if ruta:
            cursor = self.text_edit.textCursor()
            formato = QTextImageFormat()
            formato.setName(ruta)
            cursor.insertImage(formato)
            self.barra_estado.showMessage("Imagen insertada")

    
    def mostrar_panel_buscar(self):
        self.panel_buscar.setVisible(not self.panel_buscar.isVisible())
        if self.panel_buscar.isVisible():
            self.barra_estado.showMessage("Panel de búsqueda activado")
        else:
            self.barra_estado.showMessage("Panel de búsqueda desactivado")

    def buscar_texto_panel(self, hacia_arriba=False):
        texto_buscado = self.input_buscar.text()
        if not texto_buscado:
            QMessageBox.information(self, "Buscar", "Por favor, ingresa texto para buscar.")
            return
        
        if hacia_arriba:
         
            encontrado = self.text_edit.find(texto_buscado, QTextDocument.FindFlag.FindBackward)
        else:
        
            encontrado = self.text_edit.find(texto_buscado)
            
        if not encontrado:
            mensaje = f"No se encontró: {texto_buscado}"
            QMessageBox.information(self, "Buscar", mensaje)
            self.barra_estado.showMessage(mensaje)
        else:
            self.barra_estado.showMessage(f"Texto encontrado: {texto_buscado}")

    def reemplazar_texto_panel(self):
        texto_buscado = self.input_buscar.text()
        texto_reemplazo = self.input_reemplazar.text()
        
        if not texto_buscado:
            QMessageBox.information(self, "Reemplazar", "Por favor, ingresa texto para buscar.")
            return
        
        cursor = self.text_edit.textCursor()
        
        if self.chk_reemplazar_todos.isChecked():
            
            contenido = self.text_edit.toPlainText()
            nuevo_contenido = contenido.replace(texto_buscado, texto_reemplazo)
            self.text_edit.setPlainText(nuevo_contenido)
            mensaje = f"Reemplazadas todas las ocurrencias de '{texto_buscado}'"
            QMessageBox.information(self, "Reemplazar", mensaje)
            self.barra_estado.showMessage(mensaje)
        else:
          
            if cursor.hasSelection() and cursor.selectedText() == texto_buscado:
                cursor.insertText(texto_reemplazo)
                self.barra_estado.showMessage("Texto reemplazado")
            else:
         
                if self.text_edit.find(texto_buscado):
                    cursor = self.text_edit.textCursor()
                    cursor.insertText(texto_reemplazo)
                    self.barra_estado.showMessage("Texto reemplazado")
                else:
                    self.barra_estado.showMessage("No se encontró el texto para reemplazar")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    ventana = MiniOffice()
    ventana.show()
    sys.exit(app.exec())