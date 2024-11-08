# U2_Personaje2024

## Nombre del personaje
ProtoSiervo


## Creadores
Gael Quintana Romero y Lizeth Ramírez Ramírez


## Ejercicio integral de la unidad
### 6. Semáforo de Tráfico con Sensor de Distancia
El ejercicio reune los conocimientos de los principios de IoT, tal como el uso de sensores
como HC-S04 así como el uso de corriente positiva y negativa como fuente de alimentación.
Es un prototipo de un semáforo de tráfico que detecta si un objeto está cerca para cambiar de 
rojo a verde. Un botón reinicia el semáforo. Por otro lado, el buzzer emite una señal de alerta
si el objeto pasa la distancia limite.

Archivo que contiene el video: 
https://drive.google.com/file/d/1VOVmmOS49c8NmKiCzEVS97Xe_oyZTm-m/view?usp=sharing



## Ejercicios en clase en el uso de sensores, actuadores y ESP32

Carpeta con todos los videos:
https://drive.google.com/drive/folders/1SQ6eO0eT6lH7jQHxqoob0HJlQLpPBqCM?usp=sharing

### Ejercicio número 1
En esta actividad se puso a prueba un buzzer para reproducir melodías a partir de pitidos.

### Ejercicio número 2
En esta actividad se puso a prueba un DHT11 mejor conocido como sensor de humedad y
temperatura, así como un servo. El servo se moverá a partir de cierta temperatura 
registrada por el sensor DHT11. 

### Ejercicio número 3
En esta actividad se prenden leds al ser activados por un botón, permanecen prendidos hasta que
se vuelve a pulsar el botón. Esto simula las luces de una vivenda.

### Ejercicio número 4
En esta actividad se realizó la simulación de un semáforo, en conjunto de un sensor de 
movimiento y unos leds, esté los activará. Si el sensor detecta movimiento en un distancia
no tan lejana, prenderá el led amarillo, en caso de que este muy cerca, prenderá el led rojo,
dependiendo si la distancia sea muy lejana, este permanecerá verde.

### Ejercicio número 5
En esta actividad se hizo la simulación de una gasolinera, la cual al ser controlado por
un potenciometro mostrará un porcentaje junto con una pequeña animación en la pantalla oled. 

### Ejercicio número 6
En esta matriz de leds se programó de tal manera que muestre un nombre, funciona apagando y
prendiendo leds a una determinada velocidad, dando la ilusión  de que se recorre la pantalla.

### Ejercicio número 7
En este ejercicio se utilizó un sensor de movimiento y una matriz de leds. De tal modo que,
cuando el sensor de movimiento detecta un sutil movimiento, este reflejará la distancia en
la matriz de leds.

### Ejercicio número 8
En este MAX7219 de leds se programó de tal manera que muestre un nombre, funciona apagando y
prendiendo leds a una determinada velocidad, dando la ilusión  de que se recorre la pantalla.

### Ejercicio número 9
En esta actividad se hizo la reflexión del porcentaje del potenciometro en la MAX7219 de led.

### Ejercicio número 10
En esta actividad se hizo la configuración y la implementación del motor a pasos.

### Ejercicio número 11
En está actividad, dependiendo la dirección del joystick se prende el led rgb en diferentes
colores.

## Avance en el proyecto navideño
Enlace del video:
https://drive.google.com/file/d/1iv4O0mBlPXgTzPWA1Iy4z9cU0Vjv1heN/view?usp=sharing

Los avances logrados hasta el momento es la obtención de todos los componentes a utilizar,
esto nos permite que en el futuro la modelación sea de una manera más rápida. El prototipo
ya es capaz de realizar las operaciones que se planearon de manera exitosa, el HC-S04 
obtiene una distancia, si está cerca hace que se mueva la cabeza del venado y su cola, 
tambien hace que se habra un regalo que dentro tendrá un led. Los botones ejecutan canciones
por medio del buzzer, y las luces adornan al muñeco y sus alrededores.

## Imágen de la captura de pantalla de los examenes de cisco Python
### Modulo 1
![image](https://github.com/user-attachments/assets/6b499716-29ce-4406-a46d-a03e98a18ea9)
### Modulo 2
![image](https://github.com/user-attachments/assets/92f614d6-4feb-432a-9141-fc882e26a642)
### Modulo 3
![image](https://github.com/user-attachments/assets/f1f97dc2-0ff0-4d31-b68b-56019a48ac77)
### Modulo 4
![image](https://github.com/user-attachments/assets/6e040c56-86b3-4710-aa81-44f0d3feb51b)
### Exámen final
![image](https://github.com/user-attachments/assets/e46c9944-c755-41aa-a53b-0da5030941d1)

### Capturas de pantalla que demuestren el avance
https://drive.google.com/drive/folders/1FE3LbaDT8tEFuZBK-r209vajVLnCWx9r?usp=sharing

##### ¿Cómo aplicaría los conocimientos adquiridos en Python al proyecto?
Para aplicar los principios básicos de Python en el proyecto del muñeco navideño, un ciervo, utilizaré las técnicas que he aprendido en el curso para darle funcionalidad y mejorar su interactividad.

Por ejemplo, la estructura de control en Python será clave para definir comportamientos básicos del ciervo, como cambiar de expresión o realizar ciertos movimientos al detectar una entrada específica del usuario, como un toque o una señal sonora. Utilizando funciones, puedo organizar y reutilizar las diferentes acciones del muñeco, lo que facilita la programación de comportamientos variados y le da más vida al personaje. 

Además, los conceptos de manipulación de datos serán útiles para manejar las interacciones que el ciervo tenga en tiempo real. Si el muñeco registra cambios en su ambiente, como la variación de luces o sonidos, podré procesar estos datos y generar respuestas en el ciervo, dándole una apariencia más “inteligente” y adaptativa. 

También aprovecharé la gestión de errores en Python para asegurar que el ciervo funcione sin problemas, manejando posibles fallos en sensores o interacciones de manera que no interrumpan la experiencia del usuario. Los conceptos de bucles y condicionales permiten crear secuencias animadas para el ciervo, haciendo que sus movimientos y expresiones se activen en un orden natural y acorde con el ambiente festivo. 

En conjunto, estos principios básicos de Python serán fundamentales para hacer del muñeco navideño una pieza interactiva y entretenida, que responda de manera dinámica a su entorno y a la interacción del usuario.

##  Coevaluación
Mi compañera de trabajo, Lizeth Ramírez Ramírez, estudia la carrera de Desarrollo de Software, al igual que yo. Juntos estamos desarrollando un prototipo el cual se trata de un muñeco de un ciervo, equipado
con sensores que le darán movimiento. A continuación mostraré observaciónes con respecto a su trabajo en equipo así como aportaciones.
- Esta atenta a las necesidades del equipo, ya que pregunta y da su opinión acerca de las diferentes funcionalidades del proyecto.
- Esta dispuesta a brindar de su tiempo cuando se presenta alguna necesidad del proyecto.
- Aplica su conocimiento sobre el lenguaje de programación haciendo uso de códigos para programar diferentes tipos de sensores y componentes eléctricos.
- Demuestra control de estrés y ansiedad. 
- Apoya a su compañero cuando se le demuestra alguna dificultad.
- Puede hacer más uso de voz al cuestionar desiciones que se están planeando.

En conclusión, le daré a mi compañera una nota de excelencia, 10/10.
