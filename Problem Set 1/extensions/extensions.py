fileName = input("Write a file name: ").strip().lower()

if fileName.endswith('.jpg') or fileName.endswith('.jpeg'):
    mediaType = "image/jpeg"
elif fileName.endswith('.gif'):
    mediaType = "image/gif"
elif fileName.endswith('.png'):
    mediaType = "image/png"
elif fileName.endswith('.pdf'):
    mediaType = "application/pdf"
elif fileName.endswith('.txt'):
    mediaType = "text/plain"
elif fileName.endswith('.zip'):
    mediaType = "application/zip"
else:
    mediaType = "application/octet-stream"

print(mediaType)
