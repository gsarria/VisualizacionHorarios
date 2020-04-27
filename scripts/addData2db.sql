
BEGIN TRANSACTION;

/*----------*/
/* Carreras */
/*----------*/
insert into definicion values (40,'Ingeniería de Sistemas y Computación','2020-1',1008);

/*------------*/
/* Profesores */
/*------------*/
insert into profesor values (1,'Gerardo M. Sarria M.','TC');
insert into profesor values (2,'Juan Carlos Martinez','TC');
insert into profesor values (3,'Carlos Ramirez','TC');
insert into profesor values (4,'Camilo Rueda','TC');
insert into profesor values (5,'Maria Constanza Pabon','TC');
insert into profesor values (6,'Gustavo Salazar','HC');
insert into profesor values (7,'Gloria I. Alvarez','TC');
insert into profesor values (8,'Maribel Sacanamboy','TC');
insert into profesor values (9,'Andrés Navarro','TC');
insert into profesor values (10,'Jose Eduardo Tofiño','TC');
insert into profesor values (11,'Leonardo Alfonso','HC');
insert into profesor values (12,'Camilo Rocha','TC');
insert into profesor values (13,'Yoan Pinzón','TC');
insert into profesor values (14,'Diego Linares','TC');
insert into profesor values (15,'Juan Pablo García','TC');
insert into profesor values (16,'Gonzalo Noreña','HC');
insert into profesor values (17,'Luisa Rincón','TC');
insert into profesor values (18,'Frank Valencia','TC');
insert into profesor values (19,'Carlos Andrés Olarte','TC');
insert into profesor values (20,'Andrés Barco','HC');
insert into profesor values (21,'Lady Rojas','HC');
insert into profesor values (22,'John Copete','HC');
insert into profesor values (23,'Hernán Vargas','TC');
insert into profesor values (24,'Roger Gómez','HC');

insert into profesor values (200,'Sin Asignar',NULL);

/*-------------------*/
/* Cursos y Horarios */
/*-------------------*/

/* PLAN NUEVO */
insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300ITA001','A','Introducción al Modelado de Sistemas',40,1,1008,1);
insert into horario values (1,"Martes",14.0,16.0);
insert into horario values (1,"Jueves",14.0,16.0);

insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIG039','A','Herramientas Computacionales',40,200,1008,1);
insert into horario values (2,"Lunes",12.0,13.0);

insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIG039','B','Herramientas Computacionales',40,200,1008,1);
insert into horario values (3,"Lunes",11.0,12.0);

insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIG040','A','Introducción a la Ingeniería de Sistemas y Computación',40,16,1008,1);
insert into horario values (4,"Martes",7.0,9.0);
insert into horario values (4,"Jueves",7.0,9.0);

insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIP001','B','Introducción a la Programación',40,200,1008,1);
insert into horario values (5,"Lunes",9.0,12.0);
insert into horario values (5,"Miércoles",9.0,11.0);

insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIP001','F','Introducción a la Programación',40,11,1008,1);
insert into horario values (6,"Lunes",9.0,12.0);
insert into horario values (6,"Miércoles",9.0,11.0);

insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300ITA002','A','Técnicas y Prácticas de Programación',40,17,1008,2);
insert into horario values (7,"Lunes",16.0,17.5);
insert into horario values (7,"Martes",16.0,17.5);

insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIP009','A','Estructuras de Datos',40,13,1008,2);
insert into horario values (8,"Miércoles",9.0,11.0);
insert into horario values (8,"Viernes",7.0,10.0);

insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300ITA003','A','Programación Funcional',40,18,1008,3);
insert into horario values (9,"Lunes",11.0,13.0);
insert into horario values (9,"Miércoles",11.0,13.0);
insert into horario values (9,"Jueves",11.0,13.0);

insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIS017','A','Programación Orientada a Objetos',40,11,1008,3);
insert into horario values (10,"Lunes",16.0,18.0);
insert into horario values (10,"Miércoles",14.0,17.0);

insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIG043','A','Lógica Digital y Lenguaje de Máquina',40,200,1008,3);
insert into horario values (11,"Miércoles",9.0,11.0);
insert into horario values (11,"Viernes",11.0,12.5);
insert into horario values (11,"Sábado",10.0,12.0);

insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIG002','A','Lógica para Ciencias de la Computación',40,10,1008,4);
insert into horario values (12,"Martes",11.0,13.0);
insert into horario values (12,"Jueves",11.0,13.0);

insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIG045','A','Diseño de Interfaces Humano-Computador',40,9,1008,4);
insert into horario values (13,"Martes",16.0,19.0);
insert into horario values (13,"Viernes",9.0,11.0);

insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIG044','A','Arquitectura de Computador',40,8,1008,4);
insert into horario values (14,"Lunes",11.0,12.5);
insert into horario values (14,"Martes",19.0,21.0);
insert into horario values (14,"Miércoles",11.0,12.5);

insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIP011','A','Árboles y Grafos',40,12,1008,4);
insert into horario values (15,"Martes",14.0,15.5);
insert into horario values (15,"Miércoles",16.0,18.0);
insert into horario values (15,"Jueves",14.0,15.5);

insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIG046','A','Computabilidad y Complejidad',40,18,1008,5);
insert into horario values (16,"Lunes",9.0,11.0);
insert into horario values (16,"Viernes",9.0,11.0);

insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIG008','A','Computación Gráfica',40,9,1008,5);
insert into horario values (17,"Martes",9.0,11.0);
insert into horario values (17,"Jueves",9.0,11.0);

insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIS024','A','Comunicación de Datos',40,19,1008,5);
insert into horario values (18,"Lunes",16.0,18.0);
insert into horario values (18,"Viernes",14.0,16.0);

insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIS022','A','Desarrollo Formal de Sistemas',40,4,1008,6);
insert into horario values (19,"Martes",14.0,16.0);
insert into horario values (19,"Jueves",14.0,16.0);

insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIG011','A','Sistemas Operativos',40,20,1008,6);
insert into horario values (20,"Martes",7.0,9.0);
insert into horario values (20,"Jueves",7.0,9.0);

insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CID001','A','Gestión y Modelado de Datos',40,5,1008,6);
insert into horario values (21,"Miércoles",9.0,12.0);
insert into horario values (21,"Viernes",9.0,11.0);

insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIG004','A','Análisis y diseño de algoritmos',40,12,1008,6);
insert into horario values (22,"Martes",9.0,11.0);
insert into horario values (22,"Jueves",9.0,11.0);

insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300IGG014','A','Gestión de Proyectos de Tecnología',40,21,1008,6);
insert into horario values (23,"Lunes",18.0,21.0);

insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIP012','A','Computación Científica',40,23,1008,7);
insert into horario values (24,"Martes",14.0,16.0);
insert into horario values (24,"Miércoles",17.0,18.0);

insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIP013','A','Programación Paralela',40,24,1008,7);
insert into horario values (25,"Lunes",11.0,13.0);
insert into horario values (25,"Miércoles",11.0,13.0);

insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIG041','A','Aprendizaje Automático y Análisis de Datos',40,7,1008,7);
insert into horario values (26,"Martes",10.0,13.0);

insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIG032','A','Animación y Simulación',40,9,1008,7);
insert into horario values (27,"Miércoles",7.0,10.0);

insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIS019','A','Procesos y Diseño de Software',40,2,1008,7);
insert into horario values (28,"Lunes",7.0,9.0);
insert into horario values (28,"Miércoles",7.0,9.0);

insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300IGG012','A','Seminario de Investigación',40,6,1008,7);
insert into horario values (29,"Martes",16.0,17.0);

insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300FRG044','A','Aspectos Éticos, Sociales y Profesionales de la Computación',40,6,1008,7);
insert into horario values (30,"Jueves",7.0,10.0);

/* Cursos aun no abiertos */
insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIG049','A','Introducción a la Seguridad Informática',40,22,1008,8);
insert into horario values (31,"Dia",0.0,0.0);
insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CID004','A','Procesamiento de Grandes Volúmenes de Datos',40,7,1008,8);
insert into horario values (32,"Dia",0.0,0.0);
insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIG047','A','Sistemas de Interacción',40,1,1008,8);
insert into horario values (33,"Dia",0.0,0.0);
insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIS023','A','Sistemas Inteligentes',40,7,1008,8);
insert into horario values (34,"Dia",0.0,0.0);
insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIS020','A','Construcción de Software y Pruebas',40,15,1008,8);
insert into horario values (35,"Dia",0.0,0.0);
insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300IGG013','A','Preparación de Proyectos de Investigación e Innovación',40,14,1008,8);
insert into horario values (36,"Dia",0.0,0.0);
insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIG038','A','Proyecto Social',40,9,1008,8);
insert into horario values (37,"Dia",0.0,0.0);
insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIG048','A','Internet de las Cosas y Computación en la Nube',40,200,1008,9);
insert into horario values (38,"Dia",0.0,0.0);
insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIG042','A','Desarrollo de Videojuegos',40,9,1008,9);
insert into horario values (39,"Dia",0.0,0.0);
insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIS021','A','Tecnologías Emergentes',40,200,1008,9);
insert into horario values (40,"Dia",0.0,0.0);
insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300IGG004','A','Trabajo de Grado',40,200,1008,9);
insert into horario values (41,"Dia",0.0,0.0);
insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIG037','A','Práctica Profesional',40,200,1008,10);
insert into horario values (42,"Dia",0.0,0.0);

/* PLAN VIEJO */
insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300IGG002','A','Fundamentos de Investigación',40,14,1008,8);
insert into horario values (43,"Martes",9.0,11.0);
insert into horario values (43,"Jueves",9.0,11.0);

insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIG009','A','Inteligencia Artificial',40,7,1008,8);
insert into horario values (44,"Lunes",16.0,18.0);
insert into horario values (44,"Miércoles",16.0,18.0);

insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIG033','A','Introducción al Desarrollo de Videojuegos',40,9,1008,9);
insert into horario values (45,"Viernes",14.0,17.0);

insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIG031','A','Computación Móvil y Agentes Móviles',40,11,1008,9);
insert into horario values (46,"Martes",11.0,13.0);
insert into horario values (46,"Jueves",11.0,13.0);

insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CIS001','A','Desarrollo de Software a Gran Escala',40,200,1008,7);
insert into horario values (47,"Miércoles",18.0,21.0);

insert into curso (codigo,grupo,nombre,id_carrera,id_profesor,codigo_periodo,semestre) values ('300CID002','A','Implementación de Bases Datos',40,200,1008,7);
insert into horario values (48,"Jueves",18.0,21.0);

COMMIT;
