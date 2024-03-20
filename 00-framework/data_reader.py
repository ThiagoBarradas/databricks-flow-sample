# data_reader.py

from modules.sftp.sftp import Sftp

class DataReader:
    def __init__(self, configuration):
        """Constructor Method"""
        self.configuration = configuration

    def read_files_from_sftp(self, local_path, remote_path, host, port, user, private_key, ignored_files):
        sftp = Sftp(host, port, user, private_key)
        downloaded_files = []
        try:
            sftp.connect()
            files = sftp.list_excluding(remote_path, ignored_files)
            for file in files:
                sftp.download(remote_path, local_path, file)  
                downloaded_files.append(local_path + file)
            return downloaded_files
        except Exception as err:
            raise Exception(err)
        finally:
            sftp.disconnect()
