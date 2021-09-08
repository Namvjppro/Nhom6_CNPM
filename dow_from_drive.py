from requests import get  # to make GET request
def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)
download("https://drive.google.com/drive/u/0/my-drive","ok.pdf")