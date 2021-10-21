# Import the required module for text 
# to speech conversion
from gtts import gTTS
  
# The text that you want to convert to audio
string = """Bienvenue à Essence de Lahore, Je suis votre "virtual waiter"! Je vais vous donner des informations sur notre food truck. Cliquez sur les boutons ci-dessous!"""
  
# Language in which you want to convert
language = 'fr'
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=string, lang=language, slow=False)
  
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("bonjour.mp3")