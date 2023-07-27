import imaplib
import email

# Conectarse al servidor IMAP
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('johnjairorodriguez384@gmail.com', 'xnahlejjrvvwkdum')

# Seleccionar la bandeja de entrada
mail.select('inbox')

# Buscar correos electrónicos
status, data = mail.search(None, 'ALL')

# Iterar sobre los correos electrónicos
for num in data[0].split():
    # Obtener los encabezados del correo electrónico
    status, header = mail.fetch(num, '(RFC822.HEADER)')

    # Analizar los encabezados del correo electrónico
    msg = email.message_from_bytes(header[0][1])
    print('Asunto:', msg['Subject'])
    print('De:', msg['From'])
    print('Para:', msg['To'])
    print('Fecha:', msg['Date'])
    print('')

# Cerrar la conexión
mail.close()
mail.logout()




"""
import imaplib
import email

# Conectarse al servidor IMAP
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('tu_correo@gmail.com', 'tu_contraseña')

# Seleccionar la bandeja de entrada
mail.select('inbox')

# Buscar el último correo electrónico no leído
status, data = mail.search(None, 'UNSEEN')
latest_email_id = data[0].split()[-1]

# Obtener los encabezados del correo electrónico
status, header = mail.fetch(latest_email_id, '(RFC822.HEADER)')

# Analizar los encabezados del correo electrónico
msg = email.message_from_bytes(header[0][1])
print('Asunto:', msg['Subject'])
print('De:', msg['From'])
print('Para:', msg['To'])
print('Fecha:', msg['Date'])

# Marcar el correo electrónico como leído
mail.store(latest_email_id, '+FLAGS', '\\Seen')

# Cerrar la conexión
mail.close()
mail.logout()

"""