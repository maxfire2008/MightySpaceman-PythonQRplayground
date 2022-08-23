import qrcode
from pathlib import Path

def create_qr():
    img = qrcode.make(text_input)
    type(img)
    img.save(path_input)
    print(f'\nQr Code Saved to ', path_input, '\n')
    print('Data Containted: ', text_input, '\n')

while True:
    rickroll_question = input('Generation options\n(C)ustom Message\n(R)ickroll QR Code\n>')
    if rickroll_question.lower() == 'r':
        text_input = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        path_input = str(Path.home() / "Downloads")
        path_input += 'Rickroll'
        path_input += '.png'
        create_qr()
    elif rickroll_question.lower() == 'c':
        text_input = input('Enter Plain Text or Link You Want To Encode\n')
        path_input_question = input('Save To Downloads (y) or Custom Path? (n)\n')

        if path_input_question == 'y':
            path_input = str(Path.home() / "Downloads")
            path_input += text_input
            path_input += '.png'
        elif path_input_question == 'n':
            path_input = input(r'Enter Custom Path (e.g. C:\\tmp\\ )\n')
            path_input += text_input
            path_input += '.png'
        create_qr()





                              
    

    


    
    
