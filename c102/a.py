import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.AnQHwh5fZWLX_DDXcHVuM3sjbtXcjw1w5drtEHr3ZsnV1YRllHMFrV2XDfxXFxJhNeg1boZvWzSptD6EkyE3K93dzcrhwjJO3PIqzipqmehzr8wEhUDj6xyX-85PnfnIXhl32Vc'
    transferData = TransferData(access_token)

    file_from = 'D:/Coding Class/Python/c102/test2.txt'
    file_to = '/Dropbox/test2.txt'  # The full path to upload the file to, including the file name
    #C:\Users\<UserName>\Dropbox\<FileName>


    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()