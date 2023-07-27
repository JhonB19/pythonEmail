
import imaplib
import email
import os
import PySimpleGUI as sg
def download_attachment():
    # Establecer la conexión con el servidor IMAP de Gmail utilizando SSL
    imap_server = imaplib.IMAP4_SSL('imap.gmail.com')
    # Iniciar sesión en tu cuenta de Gmail
    imap_server.login('tu_correo@gmail.com', 'tu_contraseña')
    # Seleccionar la bandeja de entrada o la carpeta deseada
    imap_server.select('INBOX')
    # Buscar los IDs de los correos electrónicos en orden descendente
    status, data = imap_server.search(None, 'ALL')
    email_ids = data[0].split()[::-1]  # Invertir el orden de los IDs
    # Obtener el ID del último correo electrónico
    latest_email_id = email_ids[0]
    # Obtener el contenido del último correo electrónico
    status, email_data = imap_server.fetch(latest_email_id, "(RFC822)")
    # Parsear el contenido del correo electrónico
    raw_email = email_data[0][1]
    email_message = email.message_from_bytes(raw_email)
    # Verificar si el correo electrónico tiene archivos adjuntos
    if email_message.get_content_maintype() == 'multipart':
        for part in email_message.walk():
            if part.get_content_maintype() == 'multipart' or part.get('Content-Disposition') is None:
                continue
            # Descargar el archivo adjunto
            filename = part.get_filename()
            if filename:
                filepath = sg.popup_get_file('Guardar archivo adjunto', save_as=True, default_extension='', initial_file=filename)
                with open(filepath, 'wb') as f:
                    f.write(part.get_payload(decode=True))
                sg.popup(f"Archivo adjunto descargado: {filename}")
    # Cerrar la conexión con el servidor IMAP
    imap_server.logout()
 # Definir la interfaz gráfica utilizando PySimpleGUI con Material UI
layout = [
    [sg.Button('Descargar Archivo Adjunto', button_color=('white', '#2196f3'), size=(25, 3), key='-DOWNLOAD-')]
]
 # Crear la ventana de la interfaz gráfica
window = sg.Window('Descargar Archivo Adjunto', layout, use_default_focus=False)
 # Iniciar el bucle de eventos de la interfaz gráfica
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == '-DOWNLOAD-':
        download_attachment()
 # Cerrar la ventana de la interfaz gráfica
window.close()