import pyAesCrypt
import gitbxlogger

#   create get tag logger
dec_file_logger = gitbxlogger.myLooger('decFileLogger')
#   Length of file to decrypt
FILE_SIZE = 64*1024
#   Public key
PASSWORD = "versionbx"


def decrypt_file(src_dec_file, dst_dec_file):
    data = ""
    # decrypt
    try:
        pyAesCrypt.decryptFile(src_dec_file, dst_dec_file, PASSWORD, FILE_SIZE)
        dec_file_data = open(dst_dec_file)
        data = dec_file_data.read()
    except Exception as ex:
        dec_file_logger.logger.fatal(ex)

    print(data)
    return data


# if __name__ == "__main__":
#     decrypt_file("/Users/daniellemachpud/workspace/Test1/data.txt.aes",
#                  "/Users/daniellemachpud/workspace/Test1/dataout.txt")
