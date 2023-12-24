ph=input("file name: ")
ph=ph.lower().strip()



if ph.endswith(".jpeg") or ph.endswith(".jpg"):

    print("image/jpeg")

elif ph.endswith(".png"):
    print("image/png")

elif ph.endswith(".gif"):
    print("image/gif")

elif ph.endswith(".txt"):

    print("text/plain")

elif ph.endswith("pdf"):

    print("application/pdf")


elif ph.endswith(".zip"):
    print("application/zip")

else:
    print("application/octet-stream")