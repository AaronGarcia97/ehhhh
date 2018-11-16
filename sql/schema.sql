-- Crea Base de Datos de TaxiUnico -
DROP DATABASE IF EXISTS TaxiUnico;
CREATE DATABASE TaxiUnico;
USE TaxiUnico;

DROP TABLE IF EXISTS Carro;
CREATE TABLE Carro(
	id_carro VARCHAR(10) NOT NULL UNIQUE,
  marca VARCHAR(20),
  modelo VARCHAR(20),
  anio VARCHAR(4),
  placas VARCHAR(9),

  PRIMARY KEY (id_carro)
	);

INSERT INTO Carro VALUES ('C111111111', 'Ford', 'Explorer', '2018', 'SGJ-91-1');
INSERT INTO Carro VALUES ('C222222222', 'Volkswagen', 'Jetta', '2016', 'NGR-11-3');
INSERT INTO Carro VALUES ('C333333333', 'Dodge', 'Ram', '2012', 'OTP-19-5');

DROP TABLE IF EXISTS Cliente;
CREATE TABLE Cliente(
	id_cliente VARCHAR(10) NOT NULL UNIQUE,
  username VARCHAR(20) NOT NULL UNIQUE,
  password VARCHAR(20) NOT NULL,
  firstName VARCHAR(10),
	lastName VARCHAR(10),
  sex CHAR(1),
	dateOfBirth DATE,
	email VARCHAR(60) NOT NULL UNIQUE,
	cellphone VARCHAR(10) NOT NULL UNIQUE,

  PRIMARY KEY (id_cliente)
	);

INSERT INTO Cliente VALUES ('U000000000', 'admin', 'admin', 'admin', 'admin', 'F', '1999-03-03', 'admin@hotmail.com', '2938174637');
INSERT INTO Cliente VALUES ('U111111111', 'GabaUser', 'GabasPasswd', 'Gabriela', 'Corona', 'F', '1999-03-03', 'daba@hotmail.com', '1293482918');
INSERT INTO Cliente VALUES ('U222222222', 'AnaUser', 'AnasPasswd', 'Ana', 'Corona', 'F', '1999-03-03', 'ana@hotmail.com', '8123475823');
INSERT INTO Cliente VALUES ('U333333333', 'AaronUser', 'AaronsPasswd', 'Aaron', 'Garcia', 'M', '1997-12-20', 'aaron@hotmail.com','8180833322');

DROP TABLE IF EXISTS Admin;
CREATE TABLE Admin(
	id_admin VARCHAR(10) NOT NULL UNIQUE,
  username VARCHAR(20) NOT NULL UNIQUE,
  password VARCHAR(20) NOT NULL,
  firstName VARCHAR(10),
	lastName VARCHAR(10),
  sex CHAR(1),
	dateOfBirth DATE,
	email VARCHAR(60) NOT NULL UNIQUE,
	cellphone VARCHAR(10) NOT NULL UNIQUE,

  PRIMARY KEY (id_admin)
	);

INSERT INTO Admin VALUES ('A111111111', 'AaronAdmin', 'AaronsPasswd', 'Aaron', 'Garcia', 'M', '1997-12-20', 'aaron@hotmail.com', '1039201849');
INSERT INTO Admin VALUES ('A222222222', 'DanielAdmin', 'DanielsPasswd', 'Daniel', 'Tijerina', 'M', '1997-10-12', 'daniel@hotmail.com', '5516372839');

DROP TABLE IF EXISTS MetodoDePago;
CREATE TABLE MetodoDePago(
	id_metodo VARCHAR(10) NOT NULL UNIQUE,
  numero VARCHAR(16) NOT NULL,
	titular VARCHAR(40),
	cvc VARCHAR (3),
	id_cliente VARCHAR(10) NOT NULL,

	FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente),
  PRIMARY KEY (id_admin)
	);

INSERT INTO MetodoDePago VALUES ('M111111111', '5579090032453293', 'Gabriela Corona', '098', 'U111111111');
INSERT INTO MetodoDePago VALUES ('M222222222', '0324293557509039', 'Aaron Garcia', '066', 'U222222222');

DROP TABLE IF EXISTS Taxista;
CREATE TABLE Taxista(
	id_taxista VARCHAR(10) NOT NULL UNIQUE,
  username VARCHAR(20) NOT NULL UNIQUE,
  password VARCHAR(20) NOT NULL,
  firstName VARCHAR(10),
	lastName VARCHAR(10),
  sex CHAR(1),
	dateOfBirth DATE,
	id_admin VARCHAR(10) NOT NULL,
	email VARCHAR(60) NOT NULL UNIQUE,
	cellphone VARCHAR(10) NOT NULL UNIQUE,
	id_carro VARCHAR(10) NOT NULL,

	FOREIGN KEY (id_admin) REFERENCES Admin(id_admin),
	FOREIGN KEY (id_carro) REFERENCES Carro(id_carro),
	PRIMARY KEY (id_taxista)
	);

INSERT INTO Taxista VALUES ('T111111111', 'GabaUser', 'GabasPasswd', 'Gabriela', 'Corona', 'F', '1999-03-03', 'A222222222', 'gaba@hotmail.com', '1920391726', 'C111111111');
INSERT INTO Taxista VALUES ('T222222222', 'AnaUser', 'AnasPasswd', 'Ana', 'Corona', 'F', '1999-03-03', 'A111111111', 'ana@hotmail.com', '1293929189', 'C222222222');

DROP TABLE IF EXISTS Viaje;
CREATE TABLE Viaje(
	id_viaje VARCHAR(10) NOT NULL UNIQUE,
  fechaYhora DATETIME NOT NULL,
  destino VARCHAR(20) NOT NULL,
	origen VARCHAR(20) NOT NULL,
	costoPorKilometro SMALLINT NOT NULL,
	id_cliente VARCHAR(10) NOT NULL,
	id_taxista VARCHAR(10) NOT NULL,

	FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente),
	FOREIGN KEY (id_taxista) REFERENCES Taxista(id_taxista),
	PRIMARY KEY (id_viaje)
	);

INSERT INTO Viaje VALUES ('V111111111', '2018-10-17 14:14:10', 'Valle Oriente', 'Garza Sada', 10, 'U111111111', 'T222222222');
INSERT INTO Viaje VALUES ('V222222222', '2018-10-17 15:14:10', 'Cumbres', 'Garza Sada', 11, 'U333333333', 'T111111111');


DROP TABLE IF EXISTS Encuesta;
CREATE TABLE Encuesta(
	id_encuesta VARCHAR(10) NOT NULL UNIQUE,
 	satisfaccion TINYINT,
	tiempo TINYINT,
	taxista TINYINT,
	comentarios VARCHAR(200),
	id_viaje VARCHAR(10) NOT NULL UNIQUE,

	FOREIGN KEY (id_viaje) REFERENCES Viaje(id_viaje),
	PRIMARY KEY (id_encuesta)
	);

INSERT INTO Encuesta VALUES ('E111111111', 5, 4, 3, 'No se, la neta, manejó muy rápido. ', 'V111111111');
