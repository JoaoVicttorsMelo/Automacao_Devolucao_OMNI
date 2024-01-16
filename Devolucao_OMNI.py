import os
import subprocess
import time

# Lógica principal
while True:
    if (os.path.exists("C:\\Program Files (x86)\\Linx Sistemas\\LinxPOS\\UserPrograms")):
        choice = input('DESEJA **HABILITAR** A DEVOLUCAO OMNI? DIGITE: (sim/nao)\n')
        if choice.lower() == "sim" or choice.lower() == "s":
            # Encerrando processos
            subprocess.call(["taskkill", "/IM", "LPMLib.exe", "/F"], stderr=subprocess.DEVNULL,
                            stdout=subprocess.DEVNULL)
            subprocess.call(["taskkill", "/IM", "LPeMLib.exe", "/F"], stderr=subprocess.DEVNULL,
                            stdout=subprocess.DEVNULL)
            subprocess.call(["taskkill", "/IM", "LPLib.exe", "/F"], stderr=subprocess.DEVNULL,
                            stdout=subprocess.DEVNULL)
            subprocess.call(["taskkill", "/IM", "LPeLib.exe", "/F"], stderr=subprocess.DEVNULL,
                            stdout=subprocess.DEVNULL)

            os.rename("C:\\Program Files (x86)\\Linx Sistemas\\LinxPOS\\UserPrograms",
                      "C:\\Program Files (x86)\\Linx Sistemas\\LinxPOS\\UserPrograms.omni")

            break
        elif choice.lower() == "nao" or choice.lower() == "n":
            break
        else:
            print("Digite apenas sim ou nao")
    elif (os.path.exists("C:\\Program Files (x86)\\Linx Sistemas\\LinxPOS\\UserPrograms.omni")):
            choice = input('DESEJA **DESABILITAR** A **DEVOLUCAO** OMNI? DIGITE: (sim/nao)\n')
            if choice.lower() == "sim" or choice.lower() == "s":
                # Encerrando processos
                subprocess.call(["taskkill", "/IM", "LPMLib.exe", "/F"], stderr=subprocess.DEVNULL,
                                stdout=subprocess.DEVNULL)
                subprocess.call(["taskkill", "/IM", "LPeMLib.exe", "/F"], stderr=subprocess.DEVNULL,
                                stdout=subprocess.DEVNULL)
                subprocess.call(["taskkill", "/IM", "LPLib.exe", "/F"], stderr=subprocess.DEVNULL,
                                stdout=subprocess.DEVNULL)
                subprocess.call(["taskkill", "/IM", "LPeLib.exe", "/F"], stderr=subprocess.DEVNULL,
                                stdout=subprocess.DEVNULL)

                os.rename("C:\\Program Files (x86)\\Linx Sistemas\\LinxPOS\\UserPrograms.omni",
                          "C:\\Program Files (x86)\\Linx Sistemas\\LinxPOS\\UserPrograms")
                break
            elif choice.lower() == "nao" or choice.lower() == "n":
                break
            else:
                print("Digite apenas sim ou nao")
    elif (os.path.exists("C:\\Program Files (x86)\\Linx Sistemas\\LinxPOS-e\\UserPrograms")):
        choice = input('DESEJA **HABILITAR** A DEVOLUCAO OMNI? DIGITE: (sim/nao)\n')
        if choice.lower() == "sim" or choice.lower() == "s":
            # Encerrando processos
            subprocess.call(["taskkill", "/IM", "LPMLib.exe", "/F"], stderr=subprocess.DEVNULL,
                            stdout=subprocess.DEVNULL)
            subprocess.call(["taskkill", "/IM", "LPeMLib.exe", "/F"], stderr=subprocess.DEVNULL,
                            stdout=subprocess.DEVNULL)
            subprocess.call(["taskkill", "/IM", "LPLib.exe", "/F"], stderr=subprocess.DEVNULL,
                            stdout=subprocess.DEVNULL)
            subprocess.call(["taskkill", "/IM", "LPeLib.exe", "/F"], stderr=subprocess.DEVNULL,
                            stdout=subprocess.DEVNULL)
            os.rename("C:\\Program Files (x86)\\Linx Sistemas\\LinxPOS-e\\UserPrograms",
                      "C:\\Program Files (x86)\\Linx Sistemas\\LinxPOS-e\\UserPrograms.omni")
            break
        elif choice.lower() == "nao" or choice.lower() == "n":
            break
        else:
            print("Digite apenas sim ou nao")
    elif(os.path.exists("C:\\Program Files (x86)\\Linx Sistemas\\LinxPOS-e\\UserPrograms.omni")):
        choice = input('DESEJA **DESABILITAR** A DEVOLUCAO OMNI? DIGITE: (sim/nao)\n')
        if choice.lower() == "sim" or choice.lower() == "s":
            # Encerrando processos
            subprocess.call(["taskkill", "/IM", "LPMLib.exe", "/F"], stderr=subprocess.DEVNULL,
                            stdout=subprocess.DEVNULL)
            subprocess.call(["taskkill", "/IM", "LPeMLib.exe", "/F"], stderr=subprocess.DEVNULL,
                            stdout=subprocess.DEVNULL)
            subprocess.call(["taskkill", "/IM", "LPLib.exe", "/F"], stderr=subprocess.DEVNULL,
                            stdout=subprocess.DEVNULL)
            subprocess.call(["taskkill", "/IM", "LPeLib.exe", "/F"], stderr=subprocess.DEVNULL,
                            stdout=subprocess.DEVNULL)

            os.rename("C:\\Program Files (x86)\\Linx Sistemas\\LinxPOS-e\\UserPrograms.omni",
                      "C:\\Program Files (x86)\\Linx Sistemas\\LinxPOS-e\\UserPrograms")
            break
        elif choice.lower() == "nao" or choice.lower() == "n":
            break
        else:
            print("Digite apenas sim ou nao")

    else:
        print("A Userprograms esta fora do nosso padrão")
        time.sleep(4)
        break
