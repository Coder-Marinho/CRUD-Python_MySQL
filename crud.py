import mysql.connector

# Conecta ao banco
conn = mysql.connector.connect(
    host=" localhost",       # ou IP do servidor remoto
    user="desenvolvedores",
    password="pai de muitos",
    database="gamification_db"
)

cursor = conn.cursor()


#MAIN MENU
def initialMenu():
    escolha = 0
    print("Bem-vindo ao sistema de gerenciamento de usuários!")
    print("1 - Criar usuário")
    print("2 - Listar usuários")
    print("3 - Atualizar usuário")
    print("4 - Deletar usuário")
    print("5 - Sair")
    escolha = input("Escolha uma opção: ")
    match escolha:
        case '1':
            criar_usuario()
        case '2':
            listar_usuarios()
        case '3':
            atualizar_usuario()
        case '4':
            deletar_usuario();
        case '5':
            print("Obrigado por usar o sistema!")
            cursor.close()
            conn.close()


# CREATE
def criar_usuario():
    nome, email = dados()
    sql = "INSERT INTO users (nome, email) VALUES (%s, %s)"
    cursor.execute(sql, (nome, email))
    conn.commit()
    print("Usuário criado com sucesso!")
    initialMenu()

# READ
def listar_usuarios():
    cursor.execute("SELECT * FROM users")
    for (id, nome, email) in cursor.fetchall():
        print(f"{id}: {nome} - {email}")

# UPDATE
def atualizar_usuario(id, novo_nome):
    sql = "UPDATE usuarios SET nome = %s WHERE id = %s"
    cursor.execute(sql, (novo_nome, id))
    conn.commit()
    print("Usuário atualizado!")

# DELETE
def deletar_usuario(id):
    sql = "DELETE FROM usuarios WHERE id = %s"
    cursor.execute(sql, (id,))
    conn.commit()
    print("Usuário deletado!")


# Exemplo de uso:
#criar_usuario("Túlio", "tulio@email.com")
#listar_usuarios()
#atualizar_usuario(1, "Túlio Marinho")
#deletar_usuario(1)

def dados():
    nome = input("Insira o nome")
    email = input("Insira o email")
    return nome, email
    

initialMenu()

