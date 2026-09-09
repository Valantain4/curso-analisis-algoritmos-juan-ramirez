# Laboratorio 02 - Configuración del entorno

Para crear el entorno virtual ejecuté `python -m venv venv` desde la raíz del repositorio.
En Windows lo activé usando `.\venv\Scripts\Activate.ps1`.
Con el entorno activo instalé matplotlib usando `pip install matplotlib`.
Las dependencias del proyecto se guardaron ejecutando `pip freeze > requirements.txt`.
La carpeta `venv/` fue agregada al archivo `.gitignore` para evitar subirla a GitHub.
Para reconstruir el entorno se debe crear y activar un nuevo `venv`.
Finalmente, las dependencias se instalan con `pip install -r requirements.txt`.