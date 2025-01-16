from rembg import remove
import easygui
from PIL import Image

inputPath = easygui.fileopenbox(title='Selecione sua imagem')
outputPath = easygui.filesavebox(title ='Save file para..')

input = Image.open(inputPath)
output = remove(input)
output.save(outputPath)