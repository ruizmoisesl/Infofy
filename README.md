# INFOFY

Este proyecto permite buscar información de artistas, álbumes y canciones utilizando la API de Spotify. La aplicación muestra detalles sobre los artistas, incluyendo géneros, seguidores y popularidad, además de listar sus canciones y álbumes más recientes.

## Características
- Búsqueda de artistas por nombre.
- Obtención de información detallada de cada artista.
- Listado de álbumes y canciones de los artistas consultados.
- Enlaces directos para escuchar en Spotify.

## Requisitos
- Python 3.x
- Flask
- Spotipy (librería para interactuar con la API de Spotify)
- Una cuenta de desarrollador en Spotify y credenciales de API

## Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/ruizmoisesl/Infofy
   cd Infofy
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Configura las credenciales de la API de Spotify en el archivo que se encuentra en `routes/spotify_credentials.py`:
   ```
   SPOTIPY_CLIENT_ID='tu_client_id'
   SPOTIPY_CLIENT_SECRET='tu_client_secret'
   SPOTIPY_REDIRECT_URI='tu_redirect_uri'
   ```

## Uso
Ejecuta la aplicación con:
```bash
flask run
```
Luego, accede a `http://localhost:5000` en tu navegador y busca artistas para obtener su información.

## Autor
Desarrollado por Moises Ruiz.

