
BEGIN TRANSACTION;

/*----------*/
/* Carreras */
/*----------*/
insert into programa values (10,'Ingeniería Industrial');
insert into programa values (20,'Ingeniería Civil');
insert into programa values (30,'Ingeniería Electrónica');
insert into programa values (40,'Ingeniería de Sistemas y Computación');
insert into programa values (10001,'Matemáticas Aplicadas');
insert into programa values (10002,'Biología');
insert into programa values (10003,'Ingeniería Mecánica');
insert into programa values (10004,'Ingeniería Biomédica');
/*insert into programa values (120001,'Diseño de Comunicación Visual');*/

/*---------------------*/
/* Periodos Académicos */
/*---------------------*/
insert into periodo_academico values (1008,'2020-1');

/*---------------------*/
/* Programas X Periodo */
/*---------------------*/
insert into programa_periodo values (10,1008);
insert into programa_periodo values (20,1008);
insert into programa_periodo values (30,1008);
insert into programa_periodo values (40,1008);
insert into programa_periodo values (10001,1008);
insert into programa_periodo values (10002,1008);
insert into programa_periodo values (10003,1008);
insert into programa_periodo values (10004,1008);
/*insert into programa_periodo values (120001,1008);*/

/*------------*/
/* Profesores */
/*------------*/
/*
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

insert into profesor values (00020392,'Alioka Itare Quintero Ospino',NULL);
insert into profesor values (0056438,'Adriana Gastaldi Calero',NULL);
insert into profesor values (0071603,'Ángela María Sánchez Gómez',NULL);
insert into profesor values (00020072,'Juan Jose Ocampo Bejarano',NULL);
insert into profesor values (00020313,'Lorena Medina Beltran',NULL);
insert into profesor values (00020033,'Vanesa Franco Muñoz',NULL);
insert into profesor values (0060657,'Fernando Arboleda Aparicio',NULL);
insert into profesor values (3197501,'Elingth Simone Rosales Marquina',NULL);
insert into profesor values (00020354,'Sebero Emilio Ugarte Calleja',NULL);
insert into profesor values (0065122,'Carlos Andres Carrillo Escarraga',NULL);
insert into profesor values (0071531,'Paola Andrea Cano Molina',NULL);
insert into profesor values (0051758,'Juan Carlos Londoño R.',NULL);
insert into profesor values (0061415,'Carlos Andres Ortega Garcia',NULL);
insert into profesor values (0063998,'Diana Patricia Umaña Ruiz',NULL);
insert into profesor values (00020284,'Andrea Lucía Medina Gómez',NULL);
insert into profesor values (0069398,'Maria Paz Velez Gil',NULL);
insert into profesor values (0061548,'Diego Fernando Bolaños Diaz',NULL);
*/


/*------------------------------------------------*/
/*------------------------------------------------*/
/* Cursos de Ingeniería de Sistemas y Computación */
/*------------------------------------------------*/
/*------------------------------------------------*/

/* PLAN NUEVO */
/*
insert into curso values ('300ITA001','Introducción al Modelado de Sistemas',40,1);
insert into curso values ('300CIG039','Herramientas Computacionales',40,1);
insert into curso values ('300CIG040','Introducción a la Ingeniería de Sistemas y Computación',40,1);
insert into curso values ('300CIP001','Introducción a la Programación',40,1);
insert into curso values ('300MAG002','Cálculo Diferencial',40,1);
insert into curso values ('300EPG002','Expresión Oral y Escrita',40,1);
insert into curso values ('300CSP003','Constitución Política y Democracia Colombia',40,1);
insert into curso values ('300EIH001','Humanidades I',40,1);
insert into curso values ('300EIO039','Experiencia Formativa Vida Universitaria',40,1);
insert into curso values ('300ITA002','Técnicas y Prácticas de Programación',40,2);
insert into curso values ('300CIP009','Estructuras de Datos',40,2);
insert into curso values ('300MAG007','Cálculo Integral',40,2);
insert into curso values ('300MAG006','Álgebra Lineal',40,2);
insert into curso values ('300TEG001','Teología I',40,2);
insert into curso values ('300EIH002','Humanidades II',40,2);
insert into curso values ('300ITA003','Programación Funcional',40,3);
insert into curso values ('300CIS017','Programación Orientada a Objetos',40,3);
insert into curso values ('300CIG043','Lógica Digital y Lenguaje de Máquina',40,3);
insert into curso values ('300MAG008','Cálculo Multivariable',40,3);
insert into curso values ('300MAG009','Ecuaciones Diferenciales',40,3);
insert into curso values ('300TEG002','Teología II',40,3);
insert into curso values ('300CIG002','Lógica para Ciencias de la Computación',40,4);
insert into curso values ('300CIG045','Diseño de Interfaces Humano-Computador',40,4);
insert into curso values ('300CIG044','Arquitectura de Computador',40,4);
insert into curso values ('300CIP011','Árboles y Grafos',40,4);
insert into curso values ('300FIF003','Cinemática y Dinámica',40,4);
insert into curso values ('300CIG046','Computabilidad y Complejidad',40,5);
insert into curso values ('300CIG008','Computación Gráfica',40,5);
insert into curso values ('300CIS024','Comunicación de Datos',40,5);
insert into curso values ('300FSC001','Física Términa y Ondulatoria',40,5);
insert into curso values ('300FSC002','Electricidad y Magnetismo',40,5);
insert into curso values ('300MAE005','Probabilidad y Estadística',40,5);
insert into curso values ('300CIS022','Desarrollo Formal de Sistemas',40,6);
insert into curso values ('300CIG011','Sistemas Operativos',40,6);
insert into curso values ('300CID001','Gestión y Modelado de Datos',40,6);
insert into curso values ('300CIG004','Análisis y Diseño de Algoritmos',40,6);
insert into curso values ('300IGG014','Gestión de Proyectos de Tecnología',40,6);
insert into curso values ('300CIP012','Computación Científica',40,7);
insert into curso values ('300CIP013','Programación Paralela',40,7);
insert into curso values ('300CIG041','Aprendizaje Automático y Análisis de Datos',40,7);
insert into curso values ('300CIG032','Animación y Simulación',40,7);
insert into curso values ('300CIS019','Procesos y Diseño de Software',40,7);
insert into curso values ('300IGG012','Seminario de Investigación',40,7);
insert into curso values ('300FRG044','Aspectos Éticos, Sociales y Profesionales de la Computación',40,7);
*/
/* Cursos aun no abiertos */
/*
insert into curso values ('300CIG049','Introducción a la Seguridad Informática',40,8);
insert into curso values ('300CID004','Procesamiento de Grandes Volúmenes de Datos',40,8);
insert into curso values ('300CIG047','Sistemas de Interacción',40,8);
insert into curso values ('300CIS023','Sistemas Inteligentes',40,8);
insert into curso values ('300CIS020','Construcción de Software y Pruebas',40,8);
insert into curso values ('300IGG013','Preparación de Proyectos de Investigación e Innovación',40,8);
insert into curso values ('300CIG038','Proyecto Social',40,8);
insert into curso values ('300CIG048','Internet de las Cosas y Computación en la Nube',40,9);
insert into curso values ('300CIG042','Desarrollo de Videojuegos',40,9);
insert into curso values ('300CIS021','Tecnologías Emergentes',40,9);
insert into curso values ('300IGG004','Trabajo de Grado',40,9);
insert into curso values ('300FRG001','Ética',40,9);
insert into curso values ('300CIG037','Práctica Profesional',40,10);
insert into curso values ('300IGI003','Ingeniería Económica',40,10);
*/
/* PLAN VIEJO */
/*
insert into curso values ('300IGG002','Fundamentos de Investigación',40,8);
insert into curso values ('300CIG009','Inteligencia Artificial',40,8);
insert into curso values ('300CIG033','Introducción al Desarrollo de Videojuegos',40,9);
insert into curso values ('300CIG031','Computación Móvil y Agentes Móviles',40,9);
insert into curso values ('300CIS001','Desarrollo de Software a Gran Escala',40,7);
insert into curso values ('300CID002','Implementación de Bases Datos',40,7);
*/

/*------------------------------------------------*/
/*------------------------------------------------*/
/* Cursos de Diseño de Comunicación Visual        */
/*------------------------------------------------*/
/*------------------------------------------------*/
/*
insert into curso values ('300CMM015','Imagen Dibujo y Texto Digital',120001,1);
insert into curso values ('300ARA001','Dibujo I',120001,1);
insert into curso values ('300CMG040','Historia de la Comunicación Visual',120001,1);
insert into curso values ('300CMO010','Diseño 2D',120001,1);
insert into curso values ('300ARA005','Teoría del Color',120001,1);
insert into curso values ('300CMM017','La Imagen para Comunicación Visual',120001,2);
insert into curso values ('300ARA011','Dibujo para Diseño Gráfico',120001,2);
insert into curso values ('300CMM016','Estudios de la Imagen',120001,2);
insert into curso values ('300ARG006','Arte Clásico y Diseño',120001,2);
insert into curso values ('300CMO011','Diseño 3D',120001,2);
insert into curso values ('300CMO012','Tipografía I: Principios',120001,2);
*/

COMMIT;
