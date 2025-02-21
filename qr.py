# import qrcode
#
# # Create an instance of the QRCode class
# qr = qrcode.QRCode(version=1, box_size=2, border=1)
# qr.make("hellohttps://youtube.com/shorts/uddVh4iYX2w?si=Xbosfc1JtutHAIDw")
# # Add data to the QR Code
# # qr.add_data("hello this is a qr code")
# qr.make(fit=True)
#
# # Output the QR code as ASCII
# qr.print_ascii()
# # print("QR code printed as ASCII.")
#

# from pyzbar.pyzbar import decode
# from PIL import Image
#
# # Load the QR code image
# img = Image.open('qr.png')  # Replace 'qr.png' with your QR code image file name
#
# # Decode the QR code
# qr_data = decode(img)
#
# # Print the result(s)
# for obj in qr_data:
#     print("Type:", obj.type)  # Type of barcode scanned (e.g., QR Code)
#     print("Data:", obj.data.decode("utf-8"))  # Decoded text or URL


# import cv2
#
# # Load the QR code image
# img = cv2.imread('qr.png')  # Replace 'qr.png' with your QR code image file name
#
# # Initialize the QRCode detector
# detector = cv2.QRCodeDetector()
#
# # Detect and decode the QR code
# data, bbox, _ = detector.detectAndDecode(img)
#
# if data:
#     print("QR Code detected!")
#     print(f"Data: {data}")
# else:
#     print("No QR code found in the image.")
#
# import qrcode
# from PIL import Image
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_H,
#     box_size=10,
#     border=4,
# )
# qr.add_data("https://youtube.com/shorts/uddVh4iYX2w?si=Xbosfc1JtutHAIDw")
# qr.make(fit=True)
# img = qr.make_image(fill_color="black", back_color="white")
# img.save("qr.png")
# # img = Image.open("qr.png")
# # img.show()

# import qrcode
#
# # Create an instance of the QRCode class
# qr = qrcode.QRCode(
#     version=1,
#     box_size=2,
#     border=1
# )
#
# # Add data to the QR Code
# qr.add_data("hellohttps://youtube.com/shorts/uddVh4iYX2w?si=Xbosfc1JtutHAIDw")
#
# # Compile the data into a QR code array
# qr.make(fit=True)
#
# # Output the QR code as ASCII
# qr.print_ascii()


import qrcode

# Create an instance of the QRCode class
qr = qrcode.QRCode(
    version=1,
    box_size=10,  # Increased size
    border=4  # Increased border size
)

# Add data to the QR Code
qr.add_data("https://youtu.be/-t5b7MrWENk?si=oALTYDkqvaWPleG0")

# Compile the data into a QR code array
qr.make(fit=True)

# Create an image file
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("D:/fee/qrrvideo.png")

print("QR Code generated and saved as qrvideo.png")
