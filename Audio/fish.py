# Import the required module for text
# to speech conversion
from gtts import gTTS

# The text that you want to convert to audio
string = """Le poisson frit Lahori est notre deuxième délice ! Le plat est du saumon frit trempé dans un mélange salé. Il est servi avec une sauce piquante et garni d'épices! Délicieux!"""

# Language in which you want to convert
language = 'fr'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=string, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("fish.mp3")
