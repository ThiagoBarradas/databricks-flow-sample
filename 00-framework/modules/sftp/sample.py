# sample.py
from sftp import Sftp

# vars 
local_path = "temp/"
sftp_default_directory = "/recebidos/"
sftp_host = "127.0.0.1"
sftp_port = 22
sftp_user = "sftp-test"
sftp_private_key_content = """-----BEGIN RSA PRIVATE KEY-----
pk_here
-----END RSA PRIVATE KEY-----
"""

processed_files = [
    "1.csv", 
    "2.csv"
]

# Connect SFTP and show files
sftp = Sftp(sftp_host, sftp_port, sftp_user, sftp_private_key_content)

try:
    sftp.connect()

    # Get not unprocessed files
    files = sftp.list_excluding(sftp_default_directory, processed_files)

    # List and download unprocessed files
    for file in files:
        sftp.download(sftp_default_directory, local_path, file)   
            
except Exception as err:
    raise Exception(err)
finally:
    sftp.disconnect()
