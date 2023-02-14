Analisis
Se defini'on los requisitos para realizar este programa, de las cuales son los siguientes:
-Usar funciones 
-Usar try-except
-Intentar realizar una interfaz amigable
-Tratar de no realizar complejidad en el codigo
-No usar clases

DISENO

Primero se definio que hara cada funciones de las cuales al principio solo se pensaba usar 3 funciones.
1.- Funcion_guardar_palabra1: Esta funci'on se defini'on con el proposito de guardar un caracter que el usuario digitalice y compararlo con todo los caracteres de la palabra a adivinar, en caso no encuentre ninguno igual entonces perder algunos intentos. 
2.-Funcion_guardar_palabra: Esta funcion realiza las siguientes acciones: abre el archivo words.json, luego elige una palabra al azar y finalmente no guarda como una lista y esa palabra se compara con las dem'as funciones.
3.-Funcion_dibujar: Se penso hacer una funcion para graficar el avance del usuario y pueda visualizar sus errores.
4.-Funcion_jugar: Esta funcion es la base del juego, en donde tiene 3opciones, tiene manejo de errores y asu vez llama a las dem'as funciones para ejecutar el juego.

PROGRAMACION

La primera accion fue el interfaz de usuario, donde seguidamente se programo la funcion para elegir una palabra de la base de datos, y despues se programo la funcion_guardar_palabra1. 
Luego se tuvo dificultades al unir todas las funciones en una sola funcion, pero uso una sintaxis anterior hecho por el quien escribe y se uso chatGPT para la actualizaci'on de la palabra, ya que se tenia inconveniente con la actualizacion del avance del usuario.
