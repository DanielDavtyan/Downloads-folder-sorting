import os
import glob
import shutil
from os import path
# folder = glob.glob("../Downloads", recursive= True)
path = "/home/daniel/Downloads"

folder2 = [f for f in glob.glob(path + '**/*', recursive=True)]
# folder2 = [f for f in glob.glob(path + '**/*/', recursive=True)]
print(folder2)

documents = ['.pdf','.docx','.doc','.txt', '.odt', '.djvu', '.ipynb']
media = ['.jpeg','.jpg','.svg','.png','.PNG','.mp4','.mp3']
setupFiles = ['.exe','.msi', '.gz']
compressedFiles = ['.zip']
files = ['.apk', ".sql"]

documentLocation = "/home/daniel/Downloads/Documents"
mediaLocation = "/home/daniel/Downloads/Media"
setupFilesLocation = "/home/daniel/Downloads/SetupFiles"
compressedFilesLocation = "/home/daniel/Downloads/ZIPs"
filesLocation = "/home/daniel/Downloads/OtherFiles"


# print('I am here')
for file in folder2:
    if os.path.splitext(file)[1] in documents:
        if documentLocation in folder2:
            shutil.move(file, documentLocation)
            print("in the documents")
        else:
            #print('I am here')
            os.mkdir(documentLocation)
            shutil.move(file,documentLocation)
            print("in the documents2")
    if os.path.splitext(file)[1] in media:
        if mediaLocation in folder2:
            shutil.move(file, mediaLocation)
            print("in the media1")
        else:
            os.mkdir(mediaLocation)
            shutil.move(file,mediaLocation)
            print("in the media2")
    if os.path.splitext(file)[1] in setupFiles:
        if setupFilesLocation in folder2:
            shutil.move(file,setupFilesLocation)
            print("in the stup1")
        else:
            os.mkdir(setupFilesLocation)
            shutil.move(file,setupFilesLocation)
            print("in the setup2")
    if os.path.splitext(file)[1] in compressedFiles:
        if compressedFilesLocation in folder2:
            shutil.move(file,compressedFilesLocation)
            print("in the compressed")
        else:
            os.mkdir(compressedFilesLocation)
            shutil.move(file,compressedFilesLocation)
            print("in the compressed2")
    if os.path.splitext(file)[1] in files:
        if filesLocation in folder2:
            shutil.move(file,filesLocation)
            print("in the other")
        else:
            os.mkdir(filesLocation)
            shutil.move(file,filesLocation)
            print("in the other2")
    folder2 = [f for f in glob.glob(path + '**/*', recursive=True)]


