PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE students (
	id INTEGER NOT NULL, 
	name VARCHAR, 
	address VARCHAR, 
	neighbour VARCHAR, 
	city VARCHAR, 
	state VARCHAR, 
	postal_code VARCHAR, 
	PRIMARY KEY (id)
);
INSERT INTO students VALUES(1,'Agatha da Costa','Via Cauã Rezende','Paraíso','da Mata','São Paulo','29093-532');
INSERT INTO students VALUES(2,'Benício das Neves','Rua de da Paz, 86','Capitão Eduardo','Pereira de Rodrigues','Rio de Janeiro','83392-182');
INSERT INTO students VALUES(3,'Júlia da Paz','Praia Moraes, 25','Conjunto Taquaril','Jesus de Goiás','Goiás','15319-202');
INSERT INTO students VALUES(4,'Dr. Pedro Lucas Peixoto','Esplanada Davi Luiz Freitas, 4','Virgínia','Pires de Minas','Distrito Federal','24123-321');
INSERT INTO students VALUES(5,'Sophia Araújo','Vila Beatriz Ramos, 125','Chácara Leonina','Lima','Minas Gerais','32024-590');
INSERT INTO students VALUES(6,'Esther Freitas','Pátio Fogaça, 52','Braúnas','da Rocha do Campo','Amapá','43302-598');
INSERT INTO students VALUES(7,'Camila Rocha','Fazenda Santos, 8','Serra','Correia das Flores','Santa Catarina','76917-907');
INSERT INTO students VALUES(8,'Ana Júlia Porto','Lagoa Sarah Moraes, 58','Monte São José','Lopes','Minas Gerais','82636-495');
INSERT INTO students VALUES(9,'Pietra Campos','Favela Natália Caldeira, 88','Xodo-Marize','Farias','Paraná','33447-453');
INSERT INTO students VALUES(10,'João Felipe Carvalho','Lago Davi Sales, 60','Renascença','Cunha','Mato Grosso do Sul','56446-679');
CREATE INDEX ix_students_id ON students (id);
COMMIT;
