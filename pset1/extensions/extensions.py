file = input("File's name: ").strip().lower()
extension = file.rpartition(".")[-1]

match extension:
    case "gif" | "jpeg" | "png":
        print(f"image/{extension}")
    case "jpg":
        print(f"image/jpeg")
    case "pdf" | "zip":
        print(f"application/{extension}")
    case "txt":
        print(f"text/plain")
    case _:
        print("application/octet-stream")