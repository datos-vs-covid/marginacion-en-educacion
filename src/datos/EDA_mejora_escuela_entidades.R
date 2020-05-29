
# Cargar bibliotecas
pacman::p_load("DataExplorer", #para el EDA
               "tidyverse",
               "plyr"         #para unir los csv
               )

setwd("~/GitHub/datos-vs-covid/marginacion-en-educacion")

#Cargar archivos

files <- list.files(path = "~/GitHub/datos-vs-covid/marginacion-en-educacion/datos/crudos/planea", 
                    pattern = "*.csv", 
                    full.names = T)

tbl <- plyr::ldply(files, read.table,sep = ";",fill=TRUE, header = TRUE)

# crea gráfica con todos los campos del dataset
plot_str(tbl)

#
introduce(tbl)

# rows    columns discrete_columns continuous_columns all_missing_columns total_missing_values
# 139181      44                8                 30                   6               902461
# complete_rows total_observations memory_usage
#            0            6123964     61411704

plot_intro(tbl)

plot_missing(tbl)

profile_missing(tbl)

data <- DataExplorer::drop_columns(tbl,c("promedio_general","promedio_matematicas",
                                         "promedio_espaniol","rank","rank_nacional",
                                         "poco_confiables"))

plot_missing(data)

#To visualize frequency distributions for all discrete features:
  
  plot_bar(data)
