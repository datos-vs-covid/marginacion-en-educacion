# Repositorio template 

Bienvenido a la iniciativa Datos vs COVID

Si quieres trabajar en algun proyecto relacionado al COVID-19, por favor sigue estas indicaciones:

- Crea un repositorio para tu proyecto a partir de este  template. (https://github.com/datos-vs-covid/template). Sólo da click en el botón verde que dice "Use this template" y ¡listo!.
- El repositorio tiene por default la siguiente estructura:

```.
├── AUTORES.md
├── LICENSE
├── README.md
├── datos
│   ├── crudos          <- Datos originales, ***inmutables***.
│   ├── interinos       <- Datos intermedios que han sido transformados.
│   └── procesados      <- Datos finales, listos para tus modelos/visualizaciones.
├── docs                <- Documentación. Por ejemplo, artículos científicos, periodísticos, etc. (ignorado por git)
├── notebooks           <- Jupyter/Rmarkdown notebooks
├── reportes            <- Para cualquier reporte/informe del proyecto y/o el manusctrito final.
│   └── figuras         <- Figuras para el manuscrito o informes.
└── src                 <- Código fuente para este proyecto.
    ├── datos           <- Scripts y programas para procesar datos.
    ├── externos        <- Cualquier código fuente externo, por ejemplo, extraer otros proyectos de git o bibliotecas externas
    ├── herramientas    <- Cualquier script de ayuda entra aquí.
    ├── modelos         <- Código fuente para tu propio modelo.
    └── visualizaciones <- Scripts para la visualización de sus resultados, por ejemplo, matplotlib, ggplot2, bokeh, altair.
```

Si no utilizas algún folder, por favor no lo borres. Lo anterior nos va a ayudar a que podamos crear un inventario de datos que podamos compartir con la comunidad. Si necesitas crear más folders, siéntete libre de hacerlo.

Este template usa [Git LSF](https://git-lfs.github.com/) para hacer más ligero el trackeo de archivos de datos, imagenes y videos. Las extensiones que se guardan como LSF son:

- .csv
- .tsv
- .sav
- .mp3, mp4
- .mov

Si deseas agregar otro tipo de archivo, sólo agregalo en en el archivo `.gitattributes`

¡Gracias por participar!