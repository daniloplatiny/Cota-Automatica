import tkinter
from tkinter import filedialog
from tkinter import messagebox
import entradas
import principal
from tkinter import *
#
def sel():
    if var.get() == 2:
        entradas.correcaoDatum = 0
    else:
        entradas.correcaoDatum = 1

def abrirArquivo():
    openfilename = filedialog.askopenfilename(title = "Escolha o arquivo .inp",filetypes = ((".inp","*.inp"),("all files","*.*")))
    inFileTxt.insert(0,openfilename)
    entradas.endereco = openfilename

def salvarArquivo():
    saveFilename = filedialog.asksaveasfilename(title = 'Salvar Como',filetypes = ((".inp","*.inp"),("all files","*.*")), initialfile= 'Novo.inp',defaultextension = '.inp' )
    outFileTxt.insert(0,saveFilename)
    entradas.enderecoFinal = saveFilename

def cotar():
    if varCheck.get() == 1:
        entradas.limite = 2000
        entradas.inicio = 0
    else:
        entradas.limite = int(noFinalEntry.get())
        entradas.inicio = int(noInicialEntry.get())


    entradas.letraZona = letraUTMEntry.get()
    entradas.numZona = int(numeroUMTEntry.get())
    if varRadioButton.get() == 1:
        entradas.altitudeH = int(altitudeEntry.get())
        entradas.key = chaveGoogleEntry.get()
    else:
        entradas.referenciaX1 = float(referenciaX1Entry.get())
        entradas.referenciaX2 = float(referenciaX2Entry.get())
        entradas.referenciaY1 = float(referenciaY1Entry.get())
        entradas.referenciaY2 = float(referenciaY2Entry.get())

        entradas.epanetX1 = float(epanetX1Entry.get())
        entradas.epanetX2 = float(epanetX2Entry.get())
        entradas.epanetY1 = float(epanetY1Entry.get())
        entradas.epanetY2 = float(epanetY2Entry.get())

    if 'm' in matriculaTxt.get() and senhaTxt.get(): # Se necessario autenticar
        entradas.matricula = matriculaTxt.get()
        entradas.senha = senhaTxt.get()
        entradas.autenticaoProxy = True
    print('Cotando...')
    principal.main()

def controleNos():
    if varCheck.get() == 1:
        noFinalEntry.configure(state = 'disabled')
        noInicialEntry.configure(state = 'disabled')
    else:
        noFinalEntry.configure(state = 'normal')
        noInicialEntry.configure(state = 'normal')

def controleDatum():
    if varRadioButton.get() == 1:
        entradas.manual = 0

        datumLb.configure(state= 'normal')
        altitudeEntry.configure(state = 'normal')
        altitudeLb.configure(state = 'normal')
        R1.configure(state = 'normal')
        R2.configure(state= 'normal')

        epanetY1Entry.configure(state = 'disabled')
        epanetY2Entry.configure(state = 'disabled')
        epanetX1Lb.configure(state = 'disabled')
        epanetX2Lb.configure(state = 'disabled')
        epanetY1Lb.configure(state = 'disabled')
        epanetY2Lb.configure(state = 'disabled')
        epanetX1Entry.configure(state = 'disabled')
        epanetX2Entry.configure(state = 'disabled')

        referenciaY1Entry.configure(state = 'disabled')
        referenciaY2Entry.configure(state = 'disabled')
        referenciaX1Lb.configure(state = 'disabled')
        referenciaX2Lb.configure(state = 'disabled')
        referenciaY1Lb.configure(state = 'disabled')
        referenciaY2Lb.configure(state = 'disabled')
        referenciaX1Entry.configure(state = 'disabled')
        referenciaX2Entry.configure(state = 'disabled')
    else:
        entradas.manual = 1

        datumLb.configure(state= 'disabled')
        altitudeEntry.configure(state = 'disabled')
        altitudeLb.configure(state = 'disabled')
        R1.configure(state = 'disabled')
        R2.configure(state= 'disabled')

        epanetY1Entry.configure(state = 'normal')
        epanetY2Entry.configure(state = 'normal')
        epanetX1Lb.configure(state = 'normal')
        epanetX2Lb.configure(state = 'normal')
        epanetY1Lb.configure(state = 'normal')
        epanetY2Lb.configure(state = 'normal')
        epanetX1Entry.configure(state = 'normal')
        epanetX2Entry.configure(state = 'normal')

        referenciaY1Entry.configure(state = 'normal')
        referenciaY2Entry.configure(state = 'normal')
        referenciaX1Lb.configure(state = 'normal')
        referenciaX2Lb.configure(state = 'normal')
        referenciaY1Lb.configure(state = 'normal')
        referenciaY2Lb.configure(state = 'normal')
        referenciaX1Entry.configure(state = 'normal')
        referenciaX2Entry.configure(state = 'normal')

def popUpHelp():
    messagebox.showinfo(title= 'Ajuda', message= ">> Selecione o Arquivo .inp que será cotado."
                                         "\n\n>> Escolha onde salvar que o arquivo cotado"
                                         "\n\n>> Informe o intervalo dos nós que serão cotados"
                                         "\n\n>> Obtenha numero e zona das coordenadas no Google Earth"
                                         "\n\n>> Se o cadastro estiver Georeferenciado marque a opção \"Escolha de Datum\", se não, marque \"Translação e Rotação Manual\" "
                                         "\n\n>> Se a opção anterior for por datum, descubra o Datum utilizado no cadastro"
                                         "\n\n>> Se a opção for por rotação e translação, pegue as coo"
                                         "\n\n>> Adicione a chave do google. Cada chave cota 2500 nós por dia"
                                         "\n\n>> Se necessário autenticar o proxy. Informe matricula e senha. "
                                         "\n\n>> Para mais informações consulte a documentação"
                                         "\n\n>> Em caso de duvidas entre em contato pelo email danilo.platiny@gmail.com ")


bomdia = 1

if __name__ == '__main__':
    form = tkinter.Tk()

    getFld = tkinter.IntVar()

    form.wm_title('Cota Automatica')



#Definicao dos Frames PRINCIPAIS
    stepOne = tkinter.LabelFrame(form, text=" 1.Informações do Arquivo .inp: ")
    stepOne.grid(row=0, columnspan=7, sticky='WE', \
                 padx=5, pady=5, ipadx=5, ipady=5)

    stepTwo = tkinter.LabelFrame(form, text=" 2. Informações sobre as coordenadas UTM: ")
    stepTwo.grid(row=2, columnspan=7, sticky='WE', \
                 padx=5, pady=5, ipadx=5, ipady=5)

    stepExtra = tkinter.LabelFrame(form, text=" 3. Método de ajuste do cadastro: ")
    stepExtra.grid(row=3, columnspan=7, sticky='WE', \
                   padx=5, pady=5, ipadx=5, ipady=5)



    stepThree = tkinter.LabelFrame(form, text=" 4. Datum: ")
    stepThree.grid(row=4, columnspan=7, sticky='WE', \
                   padx=5, pady=5, ipadx=5, ipady=5)


    stepThreeRot = tkinter.LabelFrame(form, text=" 4. Rotação e Translação: ")
    stepThreeRot.grid(row=5, columnspan=7, sticky='WE', \
                   padx=5, pady=5, ipadx=5, ipady=5)


    step4 = tkinter.LabelFrame(form, text=" 4. Login e Senha: ")
    step4.grid(row= 6, columnspan=7, sticky='WE', \
                   padx=5, pady=5, ipadx=5, ipady=5)

    buttonLf = tkinter.LabelFrame(form, bd= 0)
    buttonLf.grid(row=0, column=9, columnspan=2, rowspan=8,
                sticky='NS', padx=5, pady=5)

    sobreFrame = tkinter.LabelFrame(form, bd= 0)
    sobreFrame.grid(row=10, columnspan=12, \
                 padx=5, pady=5)

#Definicao Frames secundarios
    stepThreeRotEpanet = tkinter.LabelFrame(stepThreeRot, text=" Coordenadas do Epanet")
    stepThreeRotEpanet.grid(row=0, columnspan=7, sticky='WE', \
                   padx=5, pady=5, ipadx=5, ipady=5)

    stepThreeRotEarth = tkinter.LabelFrame(stepThreeRot, text=" Coordenadas do Google Earth")
    stepThreeRotEarth.grid(row=1, columnspan=7, sticky='WE', \
                   padx=5, pady=5, ipadx=5, ipady=5)

    stepThreeRotEarthPonto1 = tkinter.LabelFrame(stepThreeRotEarth, text=" Ponto 1")
    stepThreeRotEarthPonto1.grid(row=0, column= 0)
    stepThreeRotEarthPonto2 = tkinter.LabelFrame(stepThreeRotEarth, text=" Ponto 2")
    stepThreeRotEarthPonto2.grid(row=0, column= 1)

    stepThreeRotEpanetPonto1 = tkinter.LabelFrame(stepThreeRotEpanet, text=" Ponto 1")
    stepThreeRotEpanetPonto1.grid(row=0, column= 0)
    stepThreeRotEpanetPonto2 = tkinter.LabelFrame(stepThreeRotEpanet, text=" Ponto 2")
    stepThreeRotEpanetPonto2.grid(row=0, column= 1)

#Frame 1
    inFileLbl = tkinter.Label(stepOne, text="Selecione o arquivo:")
    inFileLbl.grid(row=0, column=0, sticky='E', padx=5, pady=2)

    inFileTxt = tkinter.Entry(stepOne )
    inFileTxt.grid(row=0, column=1, columnspan=7, sticky="WE", pady=3)

    inFileBtn = tkinter.Button(stepOne, text="Abrir ...",  command = abrirArquivo)
    inFileBtn.grid(row=0, column=8, sticky='W', padx=5, pady=2)

    outFileLbl = tkinter.Label(stepOne, text="Salvar em:")
    outFileLbl.grid(row=1, column=0, sticky='E', padx=5, pady=2)

    outFileTxt = tkinter.Entry(stepOne)
    outFileTxt.grid(row=1, column=1, columnspan=7, sticky="WE", pady=2)

    outFileBtn = tkinter.Button(stepOne, text="Salvar ...", command = salvarArquivo)
    outFileBtn.grid(row=1, column=8, sticky='W', padx=5, pady=2)

    noInicialLb = tkinter.Label(stepOne, text="Nó inicial:")
    noInicialLb.grid(row=3, column=0, sticky='E', padx=5, pady=2)

    noInicialEntry = tkinter.Entry(stepOne)
    noInicialEntry.grid(row=3, column=1, sticky='E', pady=2)

    noFinalLb = tkinter.Label(stepOne, text="Nó Final:")
    noFinalLb.grid(row=3, column=5, padx=5, pady=2)

    noFinalEntry = tkinter.Entry(stepOne)
    noFinalEntry.grid(row=3, column=7, pady=2)

    varCheck = tkinter.IntVar()
    tkinter.Checkbutton(stepOne, text="Cotar tudo", variable=varCheck, command = controleNos).grid(row=2, column=1)


#Frame 2

    letraUTMLb = tkinter.Label(stepTwo, text="Letra da Zona:")
    letraUTMLb.grid(row=2, column=0, padx=2, pady=2)

    letraUTMEntry = tkinter.Entry(stepTwo,width = 7)
    letraUTMEntry.grid(row=2, column=1,padx = 2, pady=2)
    letraUTMEntry.insert(0,'K')

    numeroUMTLb = tkinter.Label(stepTwo, text="Número da Zona:")
    numeroUMTLb.grid(row=2, column=4, padx=2, pady=2)

    numeroUMTEntry = tkinter.Entry(stepTwo, width = 7)
    numeroUMTEntry.grid(row=2, column=5, padx = 2, pady=2)
    numeroUMTEntry.insert(0,'22')

#Frame Extra Escolha do tipo de ajusto
    varRadioButton = tkinter.IntVar()

    R1Metodo = tkinter.Radiobutton(stepExtra,text = 'Escolha de Datum              ' , variable = varRadioButton, value = 1, command = controleDatum )
    R1Metodo.grid(row = 1, column = 0)
    R1Metodo.select()
    R2Metodo = tkinter.Radiobutton(stepExtra,text = 'Translacao e Rotacao Manual' , variable = varRadioButton, value = 2,  command = controleDatum )
    R2Metodo.grid(row = 1, column = 2)


#Frame 3 Escolha do Datum

    datumLb = tkinter.Label(stepThree, text="Datum utilizado no Cadastro:")
    datumLb.grid(row=7, column=0, padx=2, pady=2)
    var = tkinter.IntVar()
    R1 = tkinter.Radiobutton(stepThree, text="Sirgas 2000 ", variable=var, value=1,
                  command=sel)
    R1.grid(row=7, column=1, padx=5, pady=2, sticky='W')
    R2 = tkinter.Radiobutton(stepThree, text="SAD 69", variable=var, value=2,
                  command=sel)
    R2.grid(row=7, column=2, padx=5, pady=2, sticky='W')


    altitudeLb = tkinter.Label(stepThree, text="Altitude média da região:")
    altitudeLb.grid(row=8, column=0, padx=2, pady=2, sticky = 'W')

    altitudeEntry = tkinter.Entry(stepThree)
    altitudeEntry.grid(row=8, column=1, padx = 2, pady=2, sticky = 'W')

#Frame 3 Escolha de rotacao e translacao
    #Frame Epanet
    epanetX1Lb = tkinter.Label(stepThreeRotEpanetPonto1, text="Coordenada X1:")
    epanetX1Lb.grid(row=0, column=0, sticky='E', padx=5, pady=2)
    epanetX1Entry = tkinter.Entry(stepThreeRotEpanetPonto1)
    epanetX1Entry.grid(row=0, column=1, sticky='E', pady=2)

    epanetY1Lb = tkinter.Label(stepThreeRotEpanetPonto1, text="Coordenada Y1:")
    epanetY1Lb.grid(row=2, column=0, sticky='E', padx=5, pady=2)
    epanetY1Entry = tkinter.Entry(stepThreeRotEpanetPonto1)
    epanetY1Entry.grid(row=2, column=1, sticky='E', pady=2)

    epanetX2Lb = tkinter.Label(stepThreeRotEpanetPonto2, text="Coordenada X2:")
    epanetX2Lb.grid(row=0, column=2, sticky='E', padx=5, pady=2)
    epanetX2Entry = tkinter.Entry(stepThreeRotEpanetPonto2)
    epanetX2Entry.grid(row=0, column=3, sticky='E', pady=2)

    epanetY2Lb = tkinter.Label(stepThreeRotEpanetPonto2, text="Coordenada Y2:")
    epanetY2Lb.grid(row=2, column = 2, sticky='E', padx=5, pady=2)
    epanetY2Entry = tkinter.Entry(stepThreeRotEpanetPonto2)
    epanetY2Entry.grid(row=2, column=3, sticky='E', pady=2)




    #Frame Google Earth
    referenciaX1Lb = tkinter.Label(stepThreeRotEarthPonto1, text="Coordenada X1:")
    referenciaX1Lb.grid(row=0, column=0, sticky='E', padx=5, pady=2)
    referenciaX1Entry = tkinter.Entry(stepThreeRotEarthPonto1)
    referenciaX1Entry.grid(row=0, column=1, sticky='E', pady=2)

    referenciaX2Lb = tkinter.Label(stepThreeRotEarthPonto2, text="Coordenada X2:")
    referenciaX2Lb.grid(row=0, column=2, sticky='E', padx=5, pady=2)
    referenciaX2Entry = tkinter.Entry(stepThreeRotEarthPonto2)
    referenciaX2Entry.grid(row=0, column=3, sticky='E', pady=2)

    referenciaY1Lb = tkinter.Label(stepThreeRotEarthPonto1, text="Coordenada Y1:")
    referenciaY1Lb.grid(row=2, column=0, sticky='E', padx=5, pady=2)
    referenciaY1Entry = tkinter.Entry(stepThreeRotEarthPonto1)
    referenciaY1Entry.grid(row=2, column=1, sticky='E', pady=2)

    referenciaY2Lb = tkinter.Label(stepThreeRotEarthPonto2, text="Coordenada Y2:")
    referenciaY2Lb.grid(row=2, column = 2, sticky='E', padx=5, pady=2)
    referenciaY2Entry = tkinter.Entry(stepThreeRotEarthPonto2)
    referenciaY2Entry.grid(row=2, column=3, sticky='E', pady=2)


#Frame 4
    chaveGoogleLb = tkinter.Label(step4, text="Chave do Google")
    chaveGoogleLb.grid(row=1, column=0, sticky='E', padx=5, pady=2)

    chaveGoogleEntry = tkinter.Entry(step4)
    chaveGoogleEntry.grid(row=1, column=1, columnspan=7, sticky="WE", pady=2)

    inMatriculaTxt = tkinter.Label(step4, text="Matricula:")
    inMatriculaTxt.grid(row=2, column=0, sticky='E', padx=5, pady=2)

    matriculaTxt = tkinter.Entry(step4)
    matriculaTxt.grid(row=2, column=1, sticky='E', pady=2)

    inSenhaTxt = tkinter.Label(step4, text="Senha")
    inSenhaTxt.grid(row=2, column=5, padx=5, pady=2)

    senhaTxt = tkinter.Entry(step4, show="*")
    senhaTxt.grid(row=2, column=7, pady=2)

#Frame Botoes
    buttonCotar = tkinter.Button(buttonLf, text="Cotar", command = cotar, )
    buttonCotar.grid(row=5, column =8 , sticky = 'W',padx=5, pady=5, ipadx=5, ipady=5 )

    buttonAjuda = tkinter.Button(buttonLf, text="Ajuda", command = popUpHelp )
    buttonAjuda.grid(row=5, column =9 , sticky = 'W',padx=5, pady=5, ipadx=5, ipady=5 )

#Desenvolvido
    desenvolvidoLbl = tkinter.Label(sobreFrame, text="Versao 2.1")
    desenvolvidoLbl.grid(row=6,)


# Iniciacilazao
    if varRadioButton.get() == 1:
        controleDatum()

    form.resizable(width= True, height=True)


    form.mainloop()

