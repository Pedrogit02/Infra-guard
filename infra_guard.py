import subprocess

def verificar_firewall():
   resultado = subprocess.run(["sudo" ,"ufw" , "status"] , capture_output=True)
   resultado.stdout
   texto = resultado.stdout.decode()
   partes = texto.split("\n")
   for parte in partes:
    if len (partes) > 0:

        if "ativo" in parte:
            return True

        elif "inativo" in parte:
           return False


def verificar_ssh():
    resultado_ssh = subprocess.run(["systemctl" , "status" , "ssh"] ,
                                   capture_output=True)
    resultado_ssh.stdout
    texto_ssh = resultado_ssh.stdout.decode()
    partes_ssh = texto_ssh.split("\n")
    for parte in partes_ssh:

        if len(parte) > 0:
            resultado = parte.split()

        if resultado[1] == "active":
            print("SSH: ATIVO")
            return True
            
        else:
            print("SSH: INATIVO ")
            return False
            
def sair():
    print("X" * 25)
    print("        SAINDO...       ")
    print("X" * 25 )
    
def main():
     while True:

        print ("=" *40 )
        print ("        INFRA GUARD  V1.0        ")
        print("=" * 40)

        print(" 1 - Verificar SSH  ")
        print(" 2 - Verificar Firewall  ")
        print(" 0 - Sair     ")
 
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
          verificar_ssh()
           
        elif opcao == 2:
            verificar_firewall()
            estado = verificar_firewall()
            if estado:
                print("Firewall: ATIVO ")

            else:
                print("Firewall: INATIVO")

        elif opcao == 0:
            sair()
            break
        
main()