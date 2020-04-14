from tkinter import Tk, Label, filedialog, Button, Text, Toplevel, END
from cryptofuncs import generatePublicKey, generatePrivateKey, sign, check
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import showwarning, showinfo
from hashlib import md5


class MainAppWindow(Tk):
    """ This class describes main window of app."""
    def __init__(self):
        Tk.__init__(self)

        self.title("Digital Signature Algorithm")
        self.geometry("600x400+660+340")
        self.resizable(False, False)
        self.configure(background='white')

        self.generateKeysLabelField()
        self.generateKeysButtonField()

        self.signLabelField()
        self.signButtonField()

        self.checkLabelField()
        self.checkButtonField()

    def generateKeysLabelField(self):
        generateKeysLabel = Label(self,
                                  text="Generate Key Pair for signing your items",
                                  font="Helvetica 12 bold",
                                  bg="white"
                                  )
        generateKeysLabel.place(x=145,
                                y=40,
                                width=310,
                                height=20
                                )

    def signLabelField(self):
        signLabel = Label(self,
                          text="Make signature for your items",
                          font="Helvetica 12 bold",
                          bg="white"
                          )
        signLabel.place(x=187,
                        y=150,
                        width=226,
                        height=20
                        )

    def checkLabelField(self):
        checkLabel = Label(self,
                           text="Check signature and integrity for item",
                           font="Helvetica 12 bold",
                           bg="white"
                           )
        checkLabel.place(x=157,
                         y=260,
                         width=286,
                         height=20
                         )

    def generateKeysButtonField(self):
        generateKeysButton = Button(self,
                                    text="Generate Keys",
                                    relief="groove",
                                    bg="#87cefa",
                                    command=self.openGeneratorWindow
                                    )
        generateKeysButton.place(x=175,
                                 y=80,
                                 width=250,
                                 height=50
                                 )

    def signButtonField(self):
        signButton = Button(self,
                            text="Sign",
                            relief="groove",
                            bg="#87cefa",
                            command=self.openSignWindow
                            )
        signButton.place(x=175,
                         y=190,
                         width=250,
                         height=50
                         )

    def checkButtonField(self):
        checkButton = Button(self, text="Check",
                             relief="groove",
                             bg="#87cefa",
                             command=self.openCheckWindow
                             )

        checkButton.place(x=175,
                          y=300,
                          width=250,
                          height=50
                          )

    def openGeneratorWindow(self):
        GeneratorWindow()

    def openSignWindow(self):
        SignWindow()

    def openCheckWindow(self):
        CheckWindow()


class ParentDSAWindow(Toplevel):
    """ This class has common settings for all types of classes except MainAppWindow. """
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("600x400+660+340")
        self.resizable(False, False)
        self.configure(background='white')


class FirstTypeWindow(ParentDSAWindow):
    """ This class is a template of class where you need to generate keys. """
    def __init__(self):
        ParentDSAWindow.__init__(self)
        self.geometry("600x295+660+393")
        self.focus_force()

    def firstTextField(self):
        """Field for the first part of public key"""
        firstText = Text(self,
                         relief="solid"
                         )
        firstText.place(x=70,
                        y=50,
                        width=460,
                        height=20
                        )
        return firstText

    def secondTextField(self):
        """Field for the second part of public key"""
        secondText = Text(self,
                          relief="solid"
                          )
        secondText.place(x=70,
                         y=90,
                         width=460,
                         height=40
                         )
        return secondText

    def thirdTextField(self):
        """Field for private key"""
        thirdText = Text(self,
                         relief="solid"
                         )
        thirdText.place(x=70,
                        y=150,
                        width=460,
                        height=40
                        )
        return thirdText

    def firstLabelField(self, text="First part Public Key"):
        """ Description of first text field.
            Default text = "First part Public Key"
        """
        firstLabel = Label(self,
                           text=text,
                           bg="white"
                           )
        firstLabel.place(x=70,
                         y=30,
                         width=110,
                         height=20
                         )

    def secondLabelField(self, text="Second part Public Key"):
        """ Description of the second text field
            Default text = "Second part Public Key"
        """
        secondLabel = Label(self,
                            text=text,
                            bg="white"
                            )
        secondLabel.place(x=70,
                          y=70,
                          width=124,
                          height=20
                          )

    def thirdLabelField(self, text="Private Key"):
        """ Description for the third text field
            Default text = "Private Key"
        """
        thirdLabel = Label(self,
                           text=text,
                           bg="white"
                           )
        thirdLabel.place(x=70,
                         y=130,
                         width=60,
                         height=20
                         )

    def firstButtonField(self, command, text="Generate key pair"):
        """ Button for generating key pair.
            Default text = "Generate key pair"
        """
        firstButton = Button(self,
                             text=text,
                             relief="groove",
                             bg="#87cefa",
                             command=command
                             )
        firstButton.place(x=175,
                          y=210,
                          width=250,
                          height=30
                          )

    def secondButtonField(self, command, text="Save private key"):
        """ Button for saving private key
            Default text = "Save private key"
        """
        secondButton = Button(self,
                              text=text,
                              relief="groove",
                              bg="#87cefa",
                              command=command
                              )
        secondButton.place(x=175,
                           y=245,
                           width=124,
                           height=30
                           )

    def thirdButtonField(self, command, text="Save public key"):
        """ Button for saving public key
            Default text = "Save public key"
        """
        thirdButton = Button(self,
                             text=text,
                             relief="groove",
                             bg="#87cefa",
                             command=command
                             )
        thirdButton.place(x=301,
                          y=245,
                          width=124,
                          height=30
                          )


class GeneratorWindow(FirstTypeWindow):
    """ This class describes a window, where you can generate public and private keys. """
    def __init__(self):
        FirstTypeWindow.__init__(self)

        self.firstLabelField()
        self.firstPubKeyText = self.firstTextField()

        self.secondLabelField()
        self.secondPubKeyText = self.secondTextField()

        self.thirdLabelField()
        self.privateKeyText = self.thirdTextField()

        self.firstButtonField(self.showKeys)
        self.secondButtonField(self.writePrivKeyToFile)
        self.thirdButtonField(self.writePubKeyToFile)

    def showKeys(self):
        """ This method show generated keys in text fields. """
        self.firstPubKeyText.delete(1.0, END)
        self.secondPubKeyText.delete(1.0, END)
        self.privateKeyText.delete(1.0, END)

        publicKey = generatePublicKey()

        firstPartPubKey = publicKey[0]
        secondPartPubKey = publicKey[1]
        numberFuncEuler = publicKey[2]
        privateKey = generatePrivateKey(firstPartPubKey, numberFuncEuler)

        self.firstPubKeyText.insert(1.0, hex(firstPartPubKey)[2:])
        self.secondPubKeyText.insert(1.0, hex(secondPartPubKey)[2:])
        self.privateKeyText.insert(1.0, hex(privateKey)[2:])

    def writePubKeyToFile(self):

        firstPubKeyText = self.firstPubKeyText.get(1.0, END).rstrip()
        secondPubKeyText = self.secondPubKeyText.get(1.0, END).rstrip()

        if firstPubKeyText != '' and secondPubKeyText != '':
            dlg = asksaveasfilename(defaultextension=".txt",
                                    confirmoverwrite=False,
                                    filetypes=(("Text file", "*.txt"), ("All Files", "*.*")), parent=self)
            filename = dlg
            if filename != '':
                file = open(filename, "w")
                file.write("...PUBLIC KEY START...\n")
                file.write(firstPubKeyText + "\n")
                file.write(secondPubKeyText + "\n")
                file.write("...PUBLIC KEY END...")

                file.close()
        else:
            showwarning("Warning!", "Please, generate keys!", parent=self)

    def writePrivKeyToFile(self):

        secondPubKeyText = self.secondPubKeyText.get(1.0, END).rstrip()
        privateKeyText = self.privateKeyText.get(1.0, END).rstrip()

        if secondPubKeyText != '' and privateKeyText != '':
            dlg = asksaveasfilename(defaultextension=".txt",
                                    confirmoverwrite=False,
                                    filetypes=(("Text file", "*.txt"), ("All Files", "*.*")), parent=self)
            filename = dlg
            if filename != '':
                file = open(filename, "w")
                file.write("...PRIVATE KEY START...\n")
                file.write(secondPubKeyText + "\n")
                file.write(privateKeyText + "\n")
                file.write("...PRIVATE KEY END...")

                file.close()
        else:
            showwarning("Warning!", "Please, generate keys!", parent=self)


class SecondTypeWindow(ParentDSAWindow):
    """ This class is a template of window, where you can sign and check you data. """
    def __init__(self):
        ParentDSAWindow.__init__(self)

        self.geometry("+665+345")

    def firstTextField(self):
        """Field for user's message"""
        firstText = Text(self, relief="solid")
        firstText.place(x=70,
                        y=30,
                        width=460,
                        height=60
                        )
        return firstText

    def secondTextField(self):
        """Field for path to user's file"""
        secondText = Text(self, relief="solid")
        secondText.place(x=70,
                         y=110,
                         width=360,
                         height=20
                         )
        return secondText

    def thirdTextField(self):
        """Field for the first key"""
        thirdText = Text(self, relief="solid")
        thirdText.place(x=70,
                        y=170,
                        width=360,
                        height=20
                        )
        return thirdText

    def fourthTextField(self):
        """Field for the second key"""
        fourthText = Text(self, relief="solid")
        fourthText.place(x=70,
                         y=210,
                         width=360,
                         height=40
                         )
        return fourthText

    def fifthTextField(self):
        """Field for signature"""
        fifthText = Text(self, relief="solid")
        fifthText.place(x=70,
                        y=290,
                        width=360,
                        height=40
                        )

        return fifthText

    def firstLabelField(self, text="Fill message field"):
        """ Description of the first field. For message text.
            Default text = "Fill message field"
        """
        firstLabel = Label(self,
                           text=text,
                           bg="white",
                           )
        firstLabel.place(x=70,
                         y=10,
                         width=94,
                         height=20
                         )

    def secondLabelField(self, text="Or choose a file file from your Desktop"):
        """ Description of the second field. For file path.
            Default text = "Or choose a file file from your Desktop"
        """
        secondLabel = Label(self,
                            text=text,
                            bg="white",
                            )
        secondLabel.place(x=70,
                          y=90,
                          width=206,
                          height=20
                          )

    def thirdLabelField(self, text="Part of public key"):
        """ Description of the third field. For public/private key.
            Default text = "Part of public key"
        """
        thirdLabel = Label(self,
                           text=text,
                           bg="white",
                           )
        thirdLabel.place(x=70,
                         y=150,
                         width=94,
                         height=20
                         )

    def fourthLabelField(self, text="Private key"):
        """ Description of the fourth field. For public/private key.
            Default text = "Private key"
        """
        fourthLabel = Label(self,
                            text=text,
                            bg="white",
                            )
        fourthLabel.place(x=70,
                          y=190,
                          width=60,
                          height=20
                          )

    def fifthLabelField(self, text="Load\nan existing\nprivate key\n"):
        """ Description for the second button. Button loads existing keys from a file.
            Default text = "Load\nan existing\nprivate key\n"
        """
        fifthLabel = Label(self,
                           text=text,
                           bg="white",
                           relief="groove"
                           )
        fifthLabel.place(x=436,
                         y=170,
                         width=98,
                         height=70
                         )

    def sixthLabelField(self, text="Signature"):
        """ Description of the fifth field. For signature.
            Default text = "Signature"
        """
        sixthLabel = Label(self,
                           text=text,
                           bg="white",
                           )
        sixthLabel.place(x=70,
                         y=270,
                         width=60,
                         height=20
                         )

    def seventhLabelField(self, text="Save to file\n"):
        """ Description of the thrid button. Button saves signature to a file
            Default text = "Save to file\n"
        """
        seventhLabel = Label(self,
                             text=text,
                             bg="white",
                             relief='groove',
                             )
        seventhLabel.place(x=436,
                           y=290,
                           width=98,
                           height=30
                           )

    def firstButtonField(self, command, text="Choose"):
        """ Button for get path of file from your Desktop
            Default text = "Choose"
        """
        firstButton = Button(self,
                             text=text,
                             command=command,
                             relief="groove",
                             bg="#87cefa"
                             )
        firstButton.place(x=440,
                          y=110,
                          width=90,
                          height=20)

    def secondButtonField(self, command, text="Load"):
        """ Button for loading existing key from file.
            Default text = "Load"
        """
        secondButton = Button(self,
                              text=text,
                              relief="groove",
                              bg="#87cefa",
                              command=command
                              )
        secondButton.place(x=440,
                           y=230,
                           width=90,
                           height=20
                           )

    def thirdButtonField(self, command, text="Save"):
        """ Button for saving signature to a file
            Default text = "Save"
        """

        thirdButton = Button(self,
                             text=text,
                             relief="groove",
                             bg="#87cefa",
                             command=command
                             )
        thirdButton.place(x=440,
                          y=310,
                          width=90,
                          height=20
                          )

    def fourthButtonField(self, command, text="Sign"):
        """ Button for signing some item or document.
            Default text = "Sign"
        """
        fourthButton = Button(self,
                              text=text,
                              relief="groove",
                              bg="#87cefa",
                              command=command
                              )
        fourthButton.place(x=225,
                           y=350,
                           width=150,
                           height=30)


class SignWindow(SecondTypeWindow):
    """ This class describes window, where you can sign your data. """
    def __init__(self):
        SecondTypeWindow.__init__(self)

        self.title("Signature")

        self.firstLabelField()
        self.mesText = self.firstTextField()

        self.secondLabelField()
        self.pathFileText = self.secondTextField()
        self.firstButtonField(self.choosePathToFile)

        self.thirdLabelField()
        self.pubKeySecondPartText = self.thirdTextField()

        self.fourthLabelField()
        self.privateKeyText = self.fourthTextField()

        self.fifthLabelField()
        self.secondButtonField(self.loadExistingPrivKey)

        self.sixthLabelField()
        self.signatureText = self.fifthTextField()

        self.seventhLabelField()
        self.thirdButtonField(self.saveSignature)

        self.fourthButtonField(self.signItem)

    def choosePathToFile(self):
        filename = filedialog.askopenfilename(parent=self)
        self.pathFileText.delete(1.0, END)
        self.pathFileText.insert(1.0, filename)

    def loadExistingPrivKey(self):
        filename = filedialog.askopenfilename(parent=self)
        if filename != '':
            file = open(filename)

            rows = file.readlines()

            if rows[0].rstrip() == "...PRIVATE KEY START..." \
                    and rows[-1].rstrip() == "...PRIVATE KEY END..." \
                    and len(rows) == 4:

                secondPartPubKey = rows[1].rstrip()
                privateKey = rows[2].rstrip()

                self.pubKeySecondPartText.delete(1.0, END)
                self.privateKeyText.delete(1.0, END)

                self.pubKeySecondPartText.insert(1.0, secondPartPubKey)
                self.privateKeyText.insert(1.0, privateKey)
            else:
                showwarning("Warning!", "File with private key is invalid!", parent=self)

    def signItem(self):

        mesText = self.mesText.get(1.0, END).rstrip()
        pathFileText = self.pathFileText.get(1.0, END).rstrip()
        privateKeyText = self.privateKeyText.get(1.0, END).rstrip()
        pubKeyFirstText = self.pubKeySecondPartText.get(1.0, END).rstrip()

        if mesText == '' and pathFileText == '':
            showwarning("Warning!", "Please, fill message field or path of file field!", parent=self)

        elif mesText != '' and pathFileText != '':
            showwarning("Warning!", "You can fill only one field. Message or path to file!", parent=self)

        elif privateKeyText == '' or pubKeyFirstText == '':
            showwarning("Warning!", "Please, fill all fields for keys.", parent=self)

        elif mesText != '' and pathFileText == '':
            message = self.mesText.get(1.0, END).rstrip()
            hashMes = md5(message.encode('utf-8')).hexdigest()

            signature = sign(hashMes, self.privateKeyText.get(1.0, END).rstrip(),
                             self.pubKeySecondPartText.get(1.0, END).rstrip())
            self.signatureText.insert(1.0, hex(signature)[2:])

            showinfo("Info", "Your message was signed!", parent=self)

        elif mesText == '' and pathFileText != '':
            pathToFile = self.pathFileText.get(1.0, END).rstrip()

            try:
                file = open(pathToFile, 'rb').read()

                fileHash = md5(file).hexdigest()

                signature = sign(fileHash, privateKeyText, pubKeyFirstText)
                self.signatureText.insert(1.0, hex(signature)[2:])

                showinfo("Info", "Your file was signed!", parent=self)
            except FileNotFoundError:
                showwarning("Warning!", "File, which you want to sign, is not existing!", parent=self)

    def saveSignature(self):

        signatureText = self.signatureText.get(1.0, END).rstrip()

        if signatureText != '':
            dlg = asksaveasfilename(defaultextension=".txt",
                                    confirmoverwrite=False,
                                    filetypes=(("Text file", "*.txt"), ("All Files", "*.*")),
                                    parent=self)
            filename = dlg
            if filename != '':
                file = open(filename, "w")

                file.write("...SIGNATURE START...\n")
                file.write(signatureText + "\n")
                file.write("...SIGNATURE END...")

                file.close()

                showinfo("Info", "Your signature was saved to the file!", parent=self)
        else:
            showwarning("Warning!", "Please, sign your item before saving a signatures!", parent=self)


class CheckWindow(SecondTypeWindow):
    """ This class describes window, where you can check your signature. """
    def __init__(self):
        SecondTypeWindow.__init__(self)

        self.title("Check signature")
        self.grab_set()

        self.firstLabelField()
        self.mesText = self.firstTextField()

        self.secondLabelField()
        self.pathFileText = self.secondTextField()
        self.firstButtonField(self.choosePathToFile)

        self.thirdLabelField("First part of public key")
        self.pubKeyFirstText = self.thirdTextField()

        self.fourthLabelField("Second part of public key")
        self.pubkeySecondText = self.fourthTextField()

        self.fifthLabelField("Load\nan existing\npublic key\n")
        self.secondButtonField(self.loadExistingPubKey)

        self.sixthLabelField()
        self.signatureText = self.fifthTextField()

        self.seventhLabelField("Load from file\n")
        self.thirdButtonField(self.loadSignature, "Load")

        self.fourthButtonField(self.checkItem, "Check")

    def thirdLabelField(self, text):

        thirdLabel = Label(self,
                           text=text,
                           bg="white",
                           )
        thirdLabel.place(x=70,
                         y=150,
                         width=120,
                         height=20
                         )

    def fourthLabelField(self, text):
        fourthLabel = Label(self,
                            text=text,
                            bg="white",
                            )
        fourthLabel.place(x=70,
                          y=190,
                          width=136,
                          height=20
                          )

    def choosePathToFile(self):
        SignWindow.choosePathToFile(self)

    def loadExistingPubKey(self):

        filename = filedialog.askopenfilename(parent=self)

        if filename != '':
            file = open(filename)

            rows = file.readlines()
            file.close()

            if rows[0].rstrip() == "...PUBLIC KEY START..." \
                    and rows[-1].rstrip() == "...PUBLIC KEY END..." \
                    and len(rows) == 4:
                firstPartPubKey = rows[1].rstrip()
                secondPartPubKey = rows[2].rstrip()

                self.pubKeyFirstText.delete(1.0, END)
                self.pubkeySecondText.delete(1.0, END)

                self.pubKeyFirstText.insert(1.0, firstPartPubKey)
                self.pubkeySecondText.insert(1.0, secondPartPubKey)
            else:
                showwarning("Warning!", "File with public key is invalid!", parent=self)

    def loadSignature(self):

        filename = filedialog.askopenfilename(parent=self)

        if filename != '':
            file = open(filename)

            rows = file.readlines()

            if rows[0].rstrip() == "...SIGNATURE START..." and rows[-1].rstrip() == "...SIGNATURE END..." and len(
                    rows) == 3:
                signature = rows[1].rstrip()

                self.signatureText.delete(1.0, END)
                self.signatureText.insert(1.0, signature)
            else:
                showwarning("Warning", "File with your signature is invalid!", parent=self)

    def checkItem(self):

        mesText = self.mesText.get(1.0, END).rstrip()
        pathFileText = self.pathFileText.get(1.0, END).rstrip()
        pubKeyFirstText = self.pubKeyFirstText.get(1.0, END).rstrip()
        pubkeySecondText = self.pubkeySecondText.get(1.0, END).rstrip()
        signatureText = self.signatureText.get(1.0, END).rstrip()

        if mesText == '' and pathFileText == '':
            showwarning("Warning!", "Please, fill message field or path of file field!", parent=self)

        elif mesText != '' and pathFileText != '':
            showwarning("Warning!", "You can fill only one field. Message or path to file!", parent=self)

        elif pubKeyFirstText == '' or pubkeySecondText == '':
            showwarning("Warning!", "Please, fill all fields for a key.", parent=self)

        elif signatureText == '':
            showwarning("Warning!", "Please, fill field for a signature.", parent=self)

        elif mesText != '' and pathFileText == '':

            hashMes = md5(mesText.encode('utf-8')).hexdigest()
            hashInt = int(hashMes, 16)

            calculatedHash = check(signatureText, pubKeyFirstText, pubkeySecondText)

            if calculatedHash == hashInt:
                showinfo("Info", "Signature is valid!", parent=self)
            else:
                showinfo("Info", "Signature is not valid!", parent=self)

        elif mesText == '' and pathFileText != '':

            try:
                file = open(pathFileText, 'rb').read()

                fileHash = md5(file).hexdigest()
                fileHashInt = int(fileHash, 16)

                calculatedHash = check(signatureText, pubKeyFirstText, pubkeySecondText)

                if calculatedHash == fileHashInt:
                    showinfo("Info", "Signature is valid!", parent=self)
                else:
                    showinfo("Info", "Signature is not valid!", parent=self)
            except FileNotFoundError:
                showwarning("Warning!", "File, which you want to check, is not existing!", parent=self)
