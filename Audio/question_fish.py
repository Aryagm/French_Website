# Import the required module for text
# to speech conversion
from gtts import gTTS

# The text that you want to convert to audio
string = """Le prix de Lahori Poisson Frit est de $15.99"""

# Language in which you want to convert
language = 'fr'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=string, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("question_fish.mp3")
