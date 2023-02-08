import speech_recognition as sr
import re
import pyttsx3


# variável para guardar o nome
nome = ''
while True:
    mic = sr.Recognizer()

    with sr.Microphone() as source:
        engine = pyttsx3.init()
        engine.setProperty('voice', 'com.apple.speech.synthesis.voice.luciana')
        mic.adjust_for_ambient_noise(source)
        
        if nome != '':
            # se já tem nome, já trata de forma pessoal
            print(nome+", você pode falar alguma coisa agora.")
        else:
            print("Vamos começar. Fale alguma coisa.")
        
        audio = mic.listen(source)
        
        try:
            frase = mic.recognize_google(audio, language='pt-BR')
            
            if re.search(r'\b'+'ajudar'+r'\b',format(frase)):
                engine.say('Ajuda')
                engine.runAndWait()
                print('Algo relacionado a ajudar')
            elif re.search(r'\b'+'meu nome é'+r'\b',format(frase)):
                t = re.search('meu nome é (.*)', format(frase))
                nome = t.group(1)
                print("seu nome é "+nome)
                engine.say("Nome falado foi "+ nome)
                engine.runAndWait()
                    
                
            print('você falou:' + frase)
            
        except sr.UnknownValueError:
            print('algo deu errado')
        
    