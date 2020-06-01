# Cargar bibliotecas
pacman::p_load("DataExplorer", #para el EDA
               "tidyverse",
               "plyr" ,        #para unir los csv
               "GGally",
               "ggplot2",
               "directlabels",
               "ggthemes"
)

# pongo el working directory como el folder donde está este archivo
setwd("~/GitHub/datos-vs-covid/marginacion-en-educacion/src/visualizaciones")

#cargo todos los archivos
files <- list.files(path = "~/GitHub/datos-vs-covid/marginacion-en-educacion/datos/crudos/planea", 
                    pattern = "*.csv", 
                    full.names = T)

data <- plyr::ldply(files, read.table,sep = ";",encoding = "UTF-8",fill=TRUE, header = TRUE)

# Me quedo con las columnas que voy a ocupar
data_mun <- data %>% 
  select(cct,nombre,latitud, longitud,localidad, entidad,nivel,control,planea_semaforo, planea_year,
         planea_rank_entidad, planea_evaluados)

data_mun %>% 
  dplyr::count(planea_year,entidad,localidad, planea_semaforo) #count() calls group_by() before and ungroup() after


#pruevba de grafica
library(RColorBrewer)
columnas = c( 12 ,
              15 ,
              18,
              21)

data %>% 
    filter(localidad=="Azcapotzalco",
            nivel == "Primaria",
           planea_semaforo ==1) %>% 
    top_n(5,desc(planea_rank_entidad)) %>% 
  ggparcoord(
             columns = columnas,
             groupColumn = "nombre",
             scale="globalminmax",
             order=columnas,
             alphaLines = 0.8,
             showPoints = TRUE
  ) +
directlabels::geom_dl(aes(label = nombre), 
        
        #method = list(dl.trans(x = x + .5), "last.points")
        method = list( "smart.grid",cex=.8) 
        #method = list( "last.points",cex=.8,rot=30,colour="#08415C",family="mono") 
        #method="top.points"
        #method=list("top.bumptwice",colour="#08415C",family="mono")
        #method = list(dl.trans(x = x + .2), "first.points")
)+
  scale_color_brewer(type = "qual",palette = "YlGnBu")+
  guides(color=FALSE)+
  xlab("")+
  ylab("Porcentaje")+
  labs(caption="@nerudista",
       title="Porcentaje de alumnos por categoría en Matematicas",
       subtitle= paste("Resultados PLANEA ", data$planea_year )
  )+
  theme_hc()
  
