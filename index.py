import speech_recognition as sr
import re

# variável para guardar o nome
nome = ''
while True:
    mic = sr.Recognizer()

    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)
        
        if nome != '':
            print(nome+", você pode falar alguma coisa agora.")
        else:
            print("Vamos começar. Fale alguma coisa.")
        
        audio = mic.listen(source)
        
        try:
            frase = mic.recognize_google(audio, language='pt-BR')
            
            if re.search(r'\b'+'ajudar'+r'\b',format(frase)):
                print('Algo relacionado a ajudar')
            elif re.search(r'\b'+'meu nome é'+r'\b',format(frase)):
                t = re.search('meu nome é (.*)', format(frase))
                nome = t.group(1)
                print("seu nome é "+nome)
                    
                
            print('você falou:' + frase)
            
        except sr.UnknownValueError:
            print('algo deu errado')
        
    