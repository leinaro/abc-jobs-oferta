# Componente sesión, Arquitecturas agiles, Experimento Seguridad.
​
Se encargará de crear un nuevo proyecto solo si el usuario está autorizado para realizar la operación​

## Configuracion de Docker
1. Crear la network para los dos microservicios del experimento (correr solo una vez)

    ```bash
    docker network create abc-network-seguridad
    ```
2. Construir la imagen de docker 
    ```bash
     docker build -t oferta .
    ```
3. Crear y iniciar el container (correr solo una vez)
    ```bash
    docker run --network=abc-network-seguridad --name oferta -p 5002:5002 oferta
    ```
4. Iniciar el container de nuevo:
    ```bash
    docker start oferta
    ```