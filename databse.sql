create database `hobbies`;
use hobbies;

create table `usuarios` (
	id int not null primary key auto_increment,
    nome_completo varchar(50) not null,
    email varchar(200),
    usuario varchar(50) not null unique,
    senha varchar(255) not null,
    status ENUM('ATIVO', 'INATIVO') default 'ATIVO',
    data_cadastro timestamp default current_timestamp
);


create table `generos` (
id int not null primary key auto_increment,
    nome varchar(100) not null,
    descricao text,
    data_cadastro timestamp default current_timestamp);
    

create table `catalogo` (
	id int not null auto_increment primary key,
    titulo varchar(50),
    descricao varchar(200) not null,
    data_lancamento date not null,
    episodios int,
    temporadas int,
    resenha text,
    avalicao int,
	genero_id int,
    categorias ENUM ('SERIE', 'FILME', 'ANIME', 'DOCUMENTARIO') NOT NULL,
    status ENUM ('ASSISTINDO', 'ASSISTIDO', 'ABANDONADO', 'PAUSADO', 'PENDENTE') default 'PENDENTE',
    ult_episodio int,
    ult_temporada int,
    foreign key (genero_id) references generos(id)
);