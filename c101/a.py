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
    access_token = 'sl.AnP4zkfFwwbJsZ_UOvWQ5AkMuBXZjQiIIPl1lYIhZuiLfIaEF_x3KYBxvmiv9YrqN842oOOhT2mUm6OEDPb_KqhCdmVIfrypagN6Uod1NeUkjOzdl3dqCHIQKDQia7fKIn5loKU'
    transferData = TransferData(access_token)

    file_from = 'D:/Coding Class/Python/c102/test.txt'
    file_to = '/Dropbox/test.txt'  # The full path to upload the file to, including the file name
    #C:\Users\<UserName>\Dropbox\<FileName>


    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()