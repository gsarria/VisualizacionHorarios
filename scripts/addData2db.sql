
BEGIN TRANSACTION;

/*----------*/
/* Carreras */
/*----------*/
insert into definicion values (40,'Ingeniería de Sistemas y Computación','2020-1',1008);
insert into definicion values (120001,'Diseño de Comunicación Visual','2020-1',1008);

/*------------*/
/* Profesores */
/*------------*/
insert into profesor values (0000000,'Sin Asignar',NULL);
insert into profesor values (0012941,'Gerardo M. Sarria M.','TC');
insert into profesor values (0058801,'Juan Carlos Martínez Arias','TC');
insert into profesor values (00020148119,'Carlos Alberto Ramírez Restrepo','TC');
insert into profesor values (0028575,'Camilo Rueda Calderon','TC');
insert into profesor values (0005320,'Maria Constanza Pabon Burbano','TC');
insert into profesor values (00010043377,'Gustavo Andrés Salazar Garzón','HC');
insert into profesor values (0028579,'Gloria Inés Alvarez Vargas','TC');
insert into profesor values (0000343,'Maribel Sacanamboy Franco','TC');
insert into profesor values (0006712,'Andrés Adolfo Navarro Newball','TC');
insert into profesor values (0022465,'Jose Eduardo Tofiño Peña','TC');
insert into profesor values (8936680,'José Leonardo Alfonso Gutierrez','HC');
insert into profesor values (00020269584,'Hernán Camilo Rocha Niño','TC');
insert into profesor values (00020274881,'Yoan José Pinzón Ardila','TC');
insert into profesor values (0003392,'Diego Luis Linares Ospina','TC');
insert into profesor values (0036840,'Juan Pablo García Cifuentes','TC');
insert into profesor values (00020130926,'Luis Gonzalo Noreña Agudelo','HC');
insert into profesor values (00020118133,'Luisa Fernanda Rincón Pérez','TC');
insert into profesor values (0002822,'Frank Darwin Valencia Posso','TC');
insert into profesor values (0011117,'Carlos Andrés Olarte Vega','TC');
insert into profesor values (0060184,'Andrés Felipe Barco Santa','HC');
insert into profesor values (8933568,'Lady Diana Rojas Naranjo','HC');
insert into profesor values (00020410101,'Hernán Darío Vargas Cardona','TC');
insert into profesor values (8939688,'Roger Alfonso Gómez Nieto','HC');
insert into profesor values (0183485,'Claudia Patricia Oviedo Santacruz','HC');
insert into profesor values (0015793,'Carlos Ernesto Ramirez Ovalle','HC');
insert into profesor values (0001348,'Luis Eduardo Fuertes Muñoz','HC');
insert into profesor values (00020052641,'Alexander Yela','HC');


/*-----------------------------------------------------------*/
/*-----------------------------------------------------------*/
/* Cursos y Horarios de Ingeniería de Sistemas y Computación */
/*-----------------------------------------------------------*/
/*-----------------------------------------------------------*/

/* PLAN NUEVO */
insert into curso values ('300ITA001','A','Introducción al Modelado de Sistemas',40,0012941,1008,1);
insert into horario values ('300ITA001','A',"Martes",14.0,16.0);
insert into horario values ('300ITA001','A',"Jueves",14.0,16.0);

insert into curso values ('300CIG039','A','Herramientas Computacionales',40,8936680,1008,1);
insert into horario values ('300CIG039','A',"Lunes",12.0,13.0);

insert into curso values ('300CIG039','B','Herramientas Computacionales',40,0183485,1008,1);
insert into horario values ('300CIG039','B',"Lunes",11.0,12.0);

insert into curso values ('300CIG040','A','Introducción a la Ingeniería de Sistemas y Computación',40,00020130926,1008,1);
insert into horario values ('300CIG040','A',"Martes",7.0,9.0);
insert into horario values ('300CIG040','A',"Jueves",7.0,9.0);

insert into curso values ('300CIP001','B','Introducción a la Programación',40,00010043377,1008,1);
insert into horario values ('300CIP001','B',"Lunes",9.0,12.0);
insert into horario values ('300CIP001','B',"Miércoles",9.0,11.0);

insert into curso values ('300CIP001','F','Introducción a la Programación',40,8936680,1008,1);
insert into horario values ('300CIP001','F',"Lunes",9.0,12.0);
insert into horario values ('300CIP001','F',"Miércoles",9.0,11.0);

insert into curso values ('300ITA002','A','Técnicas y Prácticas de Programación',40,00020118133,1008,2);
insert into horario values ('300ITA002','A',"Lunes",16.0,17.5);
insert into horario values ('300ITA002','A',"Martes",16.0,17.5);

insert into curso values ('300CIP009','A','Estructuras de Datos',40,00020274881,1008,2);
insert into horario values ('300CIP009','A',"Miércoles",9.0,11.0);
insert into horario values ('300CIP009','A',"Viernes",7.0,10.0);

insert into curso values ('300ITA003','A','Programación Funcional',40,0002822,1008,3);
insert into horario values ('300ITA003','A',"Lunes",11.0,13.0);
insert into horario values ('300ITA003','A',"Miércoles",11.0,13.0);
insert into horario values ('300ITA003','A',"Jueves",11.0,13.0);

insert into curso values ('300CIS017','A','Programación Orientada a Objetos',40,8936680,1008,3);
insert into horario values ('300CIS017','A',"Lunes",16.0,18.0);
insert into horario values ('300CIS017','A',"Miércoles",14.0,17.0);

insert into curso values ('300CIG043','A','Lógica Digital y Lenguaje de Máquina',40,0000343,1008,3);
insert into horario values ('300CIG043','A',"Miércoles",9.0,11.0);
insert into horario values ('300CIG043','A',"Viernes",11.0,12.5);
insert into horario values ('300CIG043','A',"Sábado",10.0,12.0);

insert into curso values ('300CIG002','A','Lógica para Ciencias de la Computación',40,0015793,1008,4);
insert into horario values ('300CIG002','A',"Martes",11.0,13.0);
insert into horario values ('300CIG002','A',"Jueves",11.0,13.0);

insert into curso values ('300CIG045','A','Diseño de Interfaces Humano-Computador',40,0006712,1008,4);
insert into horario values ('300CIG045','A',"Martes",16.0,19.0);
insert into horario values ('300CIG045','A',"Viernes",9.0,11.0);

insert into curso values ('300CIG044','A','Arquitectura de Computador',40,0000343,1008,4);
insert into horario values ('300CIG044','A',"Lunes",11.0,12.5);
insert into horario values ('300CIG044','A',"Martes",19.0,21.0);
insert into horario values ('300CIG044','A',"Miércoles",11.0,12.5);

insert into curso values ('300CIP011','A','Árboles y Grafos',40,0060184,1008,4);
insert into horario values ('300CIP011','A',"Martes",14.0,15.5);
insert into horario values ('300CIP011','A',"Miércoles",16.0,18.0);
insert into horario values ('300CIP011','A',"Jueves",14.0,15.5);

insert into curso values ('300CIG046','A','Computabilidad y Complejidad',40,0002822,1008,5);
insert into horario values ('300CIG046','A',"Lunes",9.0,11.0);
insert into horario values ('300CIG046','A',"Viernes",9.0,11.0);

insert into curso values ('300CIG008','A','Computación Gráfica',40,0006712,1008,5);
insert into horario values ('300CIG008','A',"Martes",9.0,11.0);
insert into horario values ('300CIG008','A',"Jueves",9.0,11.0);

insert into curso values ('300CIS024','A','Comunicación de Datos',40,0011117,1008,5);
insert into horario values ('300CIS024','A',"Lunes",16.0,18.0);
insert into horario values ('300CIS024','A',"Viernes",14.0,16.0);

insert into curso values ('300CIS022','A','Desarrollo Formal de Sistemas',40,0028575,1008,6);
insert into horario values ('300CIS022','A',"Martes",14.0,16.0);
insert into horario values ('300CIS022','A',"Jueves",14.0,16.0);

insert into curso values ('300CIG011','A','Sistemas Operativos',40,0060184,1008,6);
insert into horario values ('300CIG011','A',"Martes",7.0,9.0);
insert into horario values ('300CIG011','A',"Jueves",7.0,9.0);

insert into curso values ('300CID001','A','Gestión y Modelado de Datos',40,0005320,1008,6);
insert into horario values ('300CID001','A',"Miércoles",9.0,12.0);
insert into horario values ('300CID001','A',"Viernes",9.0,11.0);

insert into curso values ('300CIG004','A','Análisis y Diseño de Algoritmos',40,00020269584,1008,6);
insert into horario values ('300CIG004','A',"Martes",9.0,11.0);
insert into horario values ('300CIG004','A',"Jueves",9.0,11.0);

insert into curso values ('300IGG014','A','Gestión de Proyectos de Tecnología',40,8933568,1008,6);
insert into horario values ('300IGG014','A',"Lunes",18.0,21.0);

insert into curso values ('300CIP012','A','Computación Científica',40,00020410101,1008,7);
insert into horario values ('300CIP012','A',"Martes",14.0,16.0);
insert into horario values ('300CIP012','A',"Miércoles",17.0,18.0);

insert into curso values ('300CIP013','A','Programación Paralela',40,8939688,1008,7);
insert into horario values ('300CIP013','A',"Lunes",11.0,13.0);
insert into horario values ('300CIP013','A',"Miércoles",11.0,13.0);

insert into curso values ('300CIG041','A','Aprendizaje Automático y Análisis de Datos',40,0028579,1008,7);
insert into horario values ('300CIG041','A',"Martes",10.0,13.0);

insert into curso values ('300CIG032','A','Animación y Simulación',40,0006712,1008,7);
insert into horario values ('300CIG032','A',"Miércoles",7.0,10.0);

insert into curso values ('300CIS019','A','Procesos y Diseño de Software',40,00010043377,1008,7);
insert into horario values ('300CIS019','A',"Lunes",7.0,9.0);
insert into horario values ('300CIS019','A',"Miércoles",7.0,9.0);

insert into curso values ('300IGG012','A','Seminario de Investigación',40,00010043377,1008,7);
insert into horario values ('300IGG012','A',"Martes",16.0,17.0);

insert into curso values ('300FRG044','A','Aspectos Éticos, Sociales y Profesionales de la Computación',40,00010043377,1008,7);
insert into horario values ('300FRG044','A',"Jueves",7.0,10.0);

/* Cursos aun no abiertos */
insert into curso values ('300CIG049','A','Introducción a la Seguridad Informática',40,0000000,1008,8);
insert into horario values ('300CIG049','A',"Dia",0.0,0.0);
insert into curso values ('300CID004','A','Procesamiento de Grandes Volúmenes de Datos',40,0000000,1008,8);
insert into horario values ('300CID004','A',"Dia",0.0,0.0);
insert into curso values ('300CIG047','A','Sistemas de Interacción',40,0000000,1008,8);
insert into horario values ('300CIG047','A',"Dia",0.0,0.0);
insert into curso values ('300CIS023','A','Sistemas Inteligentes',40,0000000,1008,8);
insert into horario values ('300CIS023','A',"Dia",0.0,0.0);
insert into curso values ('300CIS020','A','Construcción de Software y Pruebas',40,0000000,1008,8);
insert into horario values ('300CIS020','A',"Dia",0.0,0.0);
insert into curso values ('300IGG013','A','Preparación de Proyectos de Investigación e Innovación',40,0000000,1008,8);
insert into horario values ('300IGG013','A',"Dia",0.0,0.0);
insert into curso values ('300CIG038','A','Proyecto Social',40,0000000,1008,8);
insert into horario values ('300CIG038','A',"Dia",0.0,0.0);
insert into curso values ('300CIG048','A','Internet de las Cosas y Computación en la Nube',40,0000000,1008,9);
insert into horario values ('300CIG048','A',"Dia",0.0,0.0);
insert into curso values ('300CIG042','A','Desarrollo de Videojuegos',40,0000000,1008,9);
insert into horario values ('300CIG042','A',"Dia",0.0,0.0);
insert into curso values ('300CIS021','A','Tecnologías Emergentes',40,0000000,1008,9);
insert into horario values ('300CIS021','A',"Dia",0.0,0.0);
insert into curso values ('300IGG004','A','Trabajo de Grado',40,0000000,1008,9);
insert into horario values ('300IGG004','A',"Dia",0.0,0.0);
insert into curso values ('300CIG037','A','Práctica Profesional',40,0000000,1008,10);
insert into horario values ('300CIG037','A',"Dia",0.0,0.0);

/* PLAN VIEJO */
insert into curso values ('300IGG002','A','Fundamentos de Investigación',40,0003392,1008,8);
insert into horario values ('300IGG002','A',"Martes",9.0,11.0);
insert into horario values ('300IGG002','A',"Jueves",9.0,11.0);

insert into curso values ('300CIG009','A','Inteligencia Artificial',40,0028579,1008,8);
insert into horario values ('300CIG009','A',"Lunes",16.0,18.0);
insert into horario values ('300CIG009','A',"Miércoles",16.0,18.0);

insert into curso values ('300CIG033','A','Introducción al Desarrollo de Videojuegos',40,0006712,1008,9);
insert into horario values ('300CIG033','A',"Viernes",14.0,17.0);

insert into curso values ('300CIG031','A','Computación Móvil y Agentes Móviles',40,8936680,1008,9);
insert into horario values ('300CIG031','A',"Martes",11.0,13.0);
insert into horario values ('300CIG031','A',"Jueves",11.0,13.0);

insert into curso values ('300CIS001','A','Desarrollo de Software a Gran Escala',40,0001348,1008,7);
insert into horario values ('300CIS001','A',"Miércoles",18.0,21.0);

insert into curso values ('300CID002','A','Implementación de Bases Datos',40,00020052641,1008,7);
insert into horario values ('300CID002','A',"Jueves",18.0,21.0);


/*-----------------------------------------------------------*/
/*-----------------------------------------------------------*/
/* Cursos y Horarios de Diseño de Comunicación Visual        */
/*-----------------------------------------------------------*/
/*-----------------------------------------------------------*/

/* PLAN NUEVO */
insert into curso values ('300CMG040','A','Historia de la Comunicación Visual',120001,0000000,1008,1);
insert into horario values ('300CMG040','A',"Viernes",7.0,10.0);


COMMIT;
