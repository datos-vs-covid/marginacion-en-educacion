
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

tbl <- plyr::ldply(files, read.table,sep = ";",encoding = "UTF-8",fill=TRUE, header = TRUE)

# crea gráfica con todos los campos del dataset
plot_str(tbl)

#
introduce(tbl)

# rows    columns discrete_columns continuous_columns all_missing_columns total_missing_values
# 139181      44                8                 30                   6               902461
# complete_rows total_observations memory_usage
#            0            6123964     61411704

# grafico inicial
plot_intro(tbl)

# valores faltantes
plot_missing(tbl)

# valores faltantes en tabla
profile_missing(tbl)

# quitar columnas que están vacias en el 100% de registros
data <- DataExplorer::drop_columns(tbl,c("promedio_general","promedio_matematicas",
                                         "promedio_espaniol","rank","rank_nacional",
                                         "poco_confiables"))



# validar que ya no hay columnas con valores faltantes asl 100%
plot_missing(data)

# Crear reporte EDA
# esto va  generar un html con las gráficas
create_report(data)

# quiero revisar la distribución de matematicas_insuficiente_nacional

data %>%
  #filter(planea_semaforo < 5) %>% 
  select(planea_year, planea_semaforo,matematicas_insuficiente_nacional) %>% 
  group_by(planea_year,planea_semaforo,matematicas_insuficiente_nacional) %>% 
  summarise_all(count)


# Después de revisar el reporte voy a generar un nuevo csv
# voy a seguir con el análisis de municipios

write.csv(data,
          "~/GitHub/datos-vs-covid/marginacion-en-educacion/datos/interinos/planea/planea_full_entidades.csv")
  