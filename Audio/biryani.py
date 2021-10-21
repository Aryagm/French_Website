# Import the required module for text
# to speech conversion
from gtts import gTTS

# The text that you want to convert to audio
string = """Lahori Biryani est notre premier plat de spécialité. C'est un plat épicé à base de riz et de mouton. Il a beaucoup de saveur! Un repas parfait!"""

# Language in which you want to convert
language = 'fr'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=string, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("biryani.mp3")
