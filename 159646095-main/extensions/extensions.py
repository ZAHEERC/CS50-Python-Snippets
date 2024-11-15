a = input("File Name : ")
a = a.strip().lower()

if(a.endswith(".gif")):
    print("image/gif")
elif(a.endswith(".jpg") or a.endswith(".jpeg")):
    print("image/jpeg")
elif(a.endswith("png")):
    print("image/png")
elif(a.endswith("pdf")):
    print("application/pdf")
elif(a.endswith("txt")):
    print("text/plain")
elif(a.endswith("zip")):
    print("application/zip")
else:
    print("application/octet-stream")
