import getpass

def autenticar():
    # Dicionário com usuários e senhas (na vida real, seria um banco de dados)
    usuarios = {
        "usuario1": "senha1",
        "usuario2": "senha2"
    }

    nome_usuario = input("Nome de usuário: ")
    senha= getpass.getpass
    senha = input("Senha: ")  # `getpass` oculta a senha na tela

    if nome_usuario in usuarios and usuarios[nome_usuario] == senha:
        print("Login bem-sucedido!")
        return True
    else:
        print("Login falhou.")
        return False

# Exemplo de uso
autenticar()