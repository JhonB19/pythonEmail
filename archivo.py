"""
import imaplib
import email
import os
 # Establecer la conexión con el servidor IMAP de Gmail utilizando SSL
imap_server = imaplib.IMAP4_SSL('imap.gmail.com')
 # Iniciar sesión en tu cuenta de Gmail
imap_server.login('bermudezriverajhon@gmail.com', 'twbmqlrgpqxcqxyo')
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
            filepath = os.path.join(r'C:\archivos de prueba', filename)  # Convertir a cadena de texto
            with open(filepath, 'wb') as f:
                f.write(part.get_payload(decode=True))
            print(f"Archivo adjunto descargado: {filename}")
 # Cerrar la conexión con el servidor IMAP
imap_server.logout()
"""