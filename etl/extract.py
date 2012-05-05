""" extract.py 

Downloads header-less csv files from a ftp server and
stores them locally, mirroring the content.

"""
import logging
import ftputil
import os

def extract(**kwargs):
    """Downloads files from the FTP source to the directory
    indicated in the extract_storage argument.

    Keyword Arguments:
    source -- ftp folder to download content from
    extract_storage -- local directory to store content in

    """
    source = kwargs['source']
    extract_storage = kwargs['extract_storage']

    logging.debug('extract begin')

    ftp_domain_root = source.replace('ftp://', '')
    ftp_domain = ftp_domain_root[:ftp_domain_root.index('/')]
    ftp_folder = ftp_domain_root[ftp_domain_root.index('/')+1:]
    
    host = ftputil.FTPHost(ftp_domain, 'anonymous', 'anonymous')
    count = 0
    for dirname, dirnames, filenames in host.walk(ftp_folder):
        for subdirname in dirnames:
            host_dir_path = host.path.join(dirname, subdirname)
            local_dir_path = os.path.join(extract_storage, host_dir_path)
            logging.debug('Navigating to %s: ' % host_dir_path)
            if not os.path.exists(local_dir_path):
                os.makedirs(local_dir_path)
        for filename in filenames:
            host_file_path = host.path.join(dirname, filename)
            local_file_path = os.path.join(extract_storage, host_file_path)
            logging.debug('Downloading %s ' % host_file_path)
            if host.path.isfile(host_file_path):
                host.download(host_file_path,
                              local_file_path, 'a')
                count = count + 1
    logging.debug('extract end')
    return count
