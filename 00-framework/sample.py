%pip install -r requirements.txt

# sample.py
from data_processor import DataProcessor

if 'dbutils' not in locals():
    dbutils = None

ignored_files = [ "1.csv" ]

processor = DataProcessor(dbutils)

downloaded_files = processor.data_reader.read_files_from_sftp(
    processor.configuration.local_path,
    processor.configuration.sftp_default_directory,
    processor.configuration.sftp_host, 
    processor.configuration.sftp_port,
    processor.configuration.sftp_user, 
    processor.configuration.sftp_private_key,
    ignored_files    
)

print("# Downloaded Files #")
for file in downloaded_files:
    print("- " + file)