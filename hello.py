import tkinter
from tkinter import filedialog
from tkinter import messagebox

def sel():
    selection = "You selected the option " + str(var.get())
    print(selection)

def abrirArquivo():
    openfilename = filedialog.askopenfilename(title = "Escolha o arquivo .inp",filetypes = ((".inp","*.inp"),("all files","*.*")))
    inFileTxt.insert(0,openfilename)

def salvarArquivo():
    saveFilename = filedialog.asksaveasfilename(title = 'Salvar Como',filetypes = ((".inp","*.inp"),("all files","*.*")), initialfile= 'Novo.inp',defaultextension = '.inp' )
    outFileTxt.insert(0,saveFilename)

def cotar():
    print('Cotando...')

def popUpHelp():
    messagebox.showinfo(title= 'Ajuda', message= ">> Selecione o Arquivo .inp que será cotado."
                                         "\n\n>> Escolha onde salvar que o arquivo cotado"
                                         "\n\n>> Informe o intervalo dos nós que serão cotados"
                                         "\n\n>> Obtenha numero e zona das coordenadas no Google Earth"
                                         "\n\n>> Descubra o Datum utilizado no cadastro"
                                         "\n\n>> Adicione a chave do google. Cada chave cota 2500 nós por dia"
                                         "\n\n>> Se necessário autenticar o proxy. Informe matricula e senha. "
                                         "\n\n>> Para mais informações consulte a documentação")

if __name__ == '__main__':
    form = tkinter.Tk()

    getFld = tkinter.IntVar()

    form.wm_title('Cota Automatica')

#Definicao dos Frames
    stepOne = tkinter.LabelFrame(form, text=" 1.Informações do Arquivo .inp: ")
    stepOne.grid(row=0, columnspan=7, sticky='WE', \
                 padx=5, pady=5, ipadx=5, ipady=5)

    stepTwo = tkinter.LabelFrame(form, text=" 2. Informações sobre as coordenadas UTM: ")
    stepTwo.grid(row=2, columnspan=7, sticky='WE', \
                 padx=5, pady=5, ipadx=5, ipady=5)

    stepThree = tkinter.LabelFrame(form, text=" 3. Datum: ")
    stepThree.grid(row=3, columnspan=7, sticky='WE', \
                   padx=5, pady=5, ipadx=5, ipady=5)

    step4 = tkinter.LabelFrame(form, text=" 4. Login e Senha: ")
    step4.grid(row= 4, columnspan=7, sticky='WE', \
                   padx=5, pady=5, ipadx=5, ipady=5)

    buttonLf = tkinter.LabelFrame(form, bd= 0)
    buttonLf.grid(row=5, columnspan=7, \
                 padx=5, pady=5)

    sobreFrame = tkinter.LabelFrame(form, bd= 0)
    sobreFrame.grid(row=6, columnspan=7, \
                 padx=5, pady=5)


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

    outFileBtn = tkinter.Button(stepOne, text="Abrir ...", command = salvarArquivo)
    outFileBtn.grid(row=1, column=8, sticky='W', padx=5, pady=2)

    noInicialLb = tkinter.Label(stepOne, text="Nó inicial:")
    noInicialLb.grid(row=2, column=0, sticky='E', padx=5, pady=2)

    noInicialEntry = tkinter.Entry(stepOne)
    noInicialEntry.grid(row=2, column=1, sticky='E', pady=2)

    noFinalLb = tkinter.Label(stepOne, text="Nó Final:")
    noFinalLb.grid(row=2, column=5, padx=5, pady=2)

    noFinalEntry = tkinter.Entry(stepOne)
    noFinalEntry.grid(row=2, column=7, pady=2)

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


#Frame 3
    datumLb = tkinter.Label(stepThree, text="Datum utilizado no Cadastro:")
    datumLb.grid(row=6, column=0, padx=2, pady=2)
    var = tkinter.IntVar()
    R1 = tkinter.Radiobutton(stepThree, text="Sirgas 2000 ", variable=var, value=1,
                  command=sel)
    R1.grid(row=6, column=1, padx=5, pady=2, sticky='W')
    R2 = tkinter.Radiobutton(stepThree, text="SAD 69", variable=var, value=2,
                  command=sel)
    R2.grid(row=6, column=2, padx=5, pady=2, sticky='W')

    altitudeLb = tkinter.Label(stepThree, text="Altitude média da região:")
    altitudeLb.grid(row=7, column=0, padx=2, pady=2, sticky = 'W')

    altitudeEntry = tkinter.Entry(stepThree)
    altitudeEntry.grid(row=7, column=1, padx = 2, pady=2, sticky = 'W')

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

    senhaTxt = tkinter.Entry(step4)
    senhaTxt.grid(row=2, column=7, pady=2)

#Frame Botoes
    buttonCotar = tkinter.Button(buttonLf, text="Cotar", command = cotar, )
    buttonCotar.grid(row=5, column =8 , sticky = 'W',padx=5, pady=5, ipadx=5, ipady=5 )

    buttonAjuda = tkinter.Button(buttonLf, text="Ajuda", command = popUpHelp )
    buttonAjuda.grid(row=5, column =9 , sticky = 'W',padx=5, pady=5, ipadx=5, ipady=5 )

#Desenvolvido
    desenvolvidoLbl = tkinter.Label(sobreFrame, text="Versao 1 \n Desenvolvido por Danilo Platiny")
    desenvolvidoLbl.grid(row=6,)

    form.resizable(width= False, height=False)
    form.mainloop()

