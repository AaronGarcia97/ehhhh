SELECT * FROM Admin;
SELECT * FROM Carro;
SELECT * FROM Cliente;
SELECT * FROM Encuesta;
SELECT * FROM Taxista;
SELECT * FROM Viaje;

-- Iniciar Sesion --
-- Validar que existe el Usuario --
SELECT id_cliente FROM Cliente WHERE username = "AaronUser";

-- Validar que password ingresada es la misma --
SELECT password FROM Cliente WHERE username = "AaronUser";

-- Administrador CRUD (Cliente, Taxista, etc) --
-- Crear cliente --
INSERT INTO Cliente VALUES ('U333333333', 'AaronUser2', 'AaronsPasswd2', 'Aaron2', 'Garcia2', 'M', '1997-12-20 12:16:10');


-- Leer info --
SELECT * FROM Cliente;
SELECT * FROM Taxista;

-- Update algo --
UPDATE Cliente SET firstName = "newFirstNa" WHERE id_cliente = "U222222222";

-- Modificar Costo por Kilometro de Viaje --
UPDATE Viaje SET costoPorKilometro = 15 WHERE id_viaje = "V111111111";

-- Asignar servicio de Taxi a Cliente --
INSERT INTO Viaje VALUES ('V333333333', '2018-11-17 14:14:10', 'Cumbres2', 'Garza Sada2', 11, 'U333333333', 'T111111111', 'C111111111');

-- Consultar servicios solicitados por cliente --
SELECT * FROM Viaje WHERE id_cliente = "U333333333";

-- Consultar servicios por taxista --
SELECT * FROM Viaje WHERE id_taxista = "T111111111";
