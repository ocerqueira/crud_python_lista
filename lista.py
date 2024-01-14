import mysql.connector

class BancoDeDados:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hobbies"
        )
        self.cursor = self.conexao.cursor()

    def fechar_conexao(self):
        if self.conexao.is_connected():
            self.cursor.close()
            self.conexao.close()
            print("Conexão Fechada!")

    def criar_usuario(self, nome_completo, email, usuario, senha):
        self.cursor.execute("INSERT INTO usuarios (nome_completo, email, usuario, senha) VALUES (%s, %s, %s, %s)", (nome_completo, email, usuario, senha))
        self.conexao.commit()
        print("Cadastro realizado com sucesso!")

    def listar_usuarios(self):
        self.cursor.execute("SELECT * FROM usuarios")
        usuarios = self.cursor.fetchall()
        print("Lista de Usuários: ")
        for usuario in usuarios:
            print(f"ID: {usuario[0]}, Nome: {usuario[1]}, Email: {usuario[2]}, Usuário: {usuario[3]}, Senha: {usuario[4]}")
        return usuarios

    def atualizar_usuarios(self, id_usuario, novo_nome, nova_senha, novo_email, novo_status):
        self.cursor.execute("UPDATE usuarios SET nome_completo = %s, senha = %s, email = %s, status = %s WHERE id = %s",(novo_nome, nova_senha, novo_email, novo_status, id_usuario))
        self.conexao.commit()
        print(f"Usuario {id_usuario} atualizado")
    def excluir_usuario(self, id_usuario):
        self.cursor.execute("DELETE FROM usuarios WHERE id = %s", (id_usuario,))
        self.conexao.commit()
        print(f"Usuario {id_usuario} Excluido")

    def cadastrar_genero(self, nome):
        self.cursor.execute("INSERT INTO generos (nome) VALUES (%s)", (nome,))
        self.conexao.commit()
        print("Genero cadastrado com sucesso!")

    def atualizar_genero(self, id_genero, nome):
        self.cursor.execute("UPDATE generos SET nome = %s WHERE id = (%s)", (nome, id_genero))
        self.conexao.commit()
        print("Genero cadastrado com sucesso!")

    def cadastrar_catalogo(self, titulo, descricao, lancamento, categoria, episodios=None, temporadas=None, resenha=None, avaliacao=None, genero=None, ):
        self.cursor.execute("INSERT INTO catalogo (titulo, descricao, data_lancamento, episodios, temporadas, resenha, avalicao, genero_id, categorias) "
                            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",(titulo, descricao, lancamento, episodios, temporadas, resenha, avaliacao, genero, categoria))
        self.conexao.commit()
        print("Cadastrado com sucesso")

    def listar_catalogo (self):
        self.cursor.execute("SELECT * FROM catalogo")
        catalogo = self.cursor.fetchall()
        print("CATALOGO")
        for titulo in catalogo:
            print(titulo)
            return catalogo




banco = BancoDeDados()

#banco.cadastrar_genero("Comedia")

#banco.criar_usuario("Lucas Cerqueira Dos Santos", "lucas@email.com", "luke", "123456")
#banco.criar_usuario("Thiago Cerqueira Dos Santos", "thiago@email.com", "thiago", "123456")
#banco.criar_usuario("Pedro Oliveira Dos Santos", "pedro@email.com", "pedro", "123456")


#banco.cadastrar_catalogo("The Office", "Sitcom americano de escritório", "2004/01/01", "SERIE")

#banco.listar_usuarios()

#banco.listar_catalogo()

banco.fechar_conexao()