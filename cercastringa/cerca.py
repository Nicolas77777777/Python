import os
import PyPDF2

def CercaParolaInFilePdf(sFile,sParola):
    object = PyPDF2.PdfReader(sFile)
    numPages = len(object.pages)
    print (f'il file {sFile} contine{numPages}')
    return False

def CercaParolaInNomeFile(sFile,sParola):
    sFileLower = sFile.lower()
    sParolaLower = sParola.lower()
    if (sFileLower.find(sParolaLower) >=0):
        return True
    else:
        return False
    

def CercaParolaInFileTxt(sPathfile, sParola):
    with open(sPathfile, "r") as file1:
        sLine =file1.readline()
        while(len(sLine)>0):
            iRet= sLine.lower().find(sParola.lower())
            if (iRet >=0):
               return True
            sLine= file1.readline()
            print("Riga letta"+ sLine)
    return False
           
    
def CercaParolaInContenutoFile(sPathFile, sParola):
    bRet= False
    sFileName, sFileExt = os.path.splitext(sPathFile)
    if(sFileExt.lower()==".txt"):
        bRet = CercaParolaInFileTxt(sPathFile, sParola)
    if(sFileExt.lower()==".pdf"):
        bRet = CercaParolaInFilePdf(sPathFile, sParola)
    return bRet

    

sRoot = input('Insercisci la directory da cercare ')
sParola = input ('Inserisci la parola da cercare:')
sOutDir= input('Inserisci la directory dove mettere i file trovati:')


bRet = False
for root, ListDir, ListFiles in os.walk(sRoot):
    print(f'Nella directory {root} ci sono {len(ListDir)} sottodirectory e {len(ListFiles)} file')
    for file in ListFiles:
        print(f'Devo cercare {sParola} in {file}')
        bRet = CercaParolaInNomeFile(file,sParola)
        if (bRet== True):
            print(f'Trovata parola in file {file}')
        else:
            sFilePathCompleto = os.path.join(root,file)
            bRet = CercaParolaInContenutoFile(sFilePathCompleto,sParola)
            if (bRet==True):
                print(f"trovata parola in file {file}")

