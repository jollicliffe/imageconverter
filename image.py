import PIL
import binascii
import codecs


def conToBytes(filename):
    with open(filename, "rb") as f:
        content = f.read()
    image_bytes = content
    return image_bytes

def conToHex(bytes):
    return bytes.hex()

def conToBase64(hex):
    return codecs.encode(codecs.decode(hex, 'hex'), 'base64').decode()

#takes hex value please
def writeImage(data):
    try:
        new=input("enter new filename: ")
        with open(new , "wb") as f:
            f.write(binascii.unhexlify(data))
        print("created new image file.")
    except:
        print("Unable to print new image")

def main():
    filename = input("enter file path: ")
    with open(filename, "rb") as f:
        data=f.read()
    hex = conToHex(data)
    writeImage(hex)


if __name__ == "__main__":
    print("please import")
else:
    main()
