#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
# Cargar bibliotecas
pacman::p_load("DataExplorer", #para el EDA
               "tidyverse",
               "plyr" ,       #para unir los csv
               "shiny",
               "RColorBrewer"
               
)

# pongo el working directory como el folder donde está este archivo
setwd("~/GitHub/datos-vs-covid/marginacion-en-educacion/src/visualizaciones")

#cargo todos los archivos
files <- list.files(path = "~/GitHub/datos-vs-covid/marginacion-en-educacion/datos/crudos/planea", 
                    pattern = "*.csv", 
                    full.names = T)

data <- plyr::ldply(files, read.table,sep = ";",encoding = "UTF-8",fill=TRUE, header = TRUE)

columnas_usar = c("nombre","localidad","entidad","nivel","planea_semaforo","planea_year",
                  "planea_rank_entidad","matematicas_insuficiente_escuela","matematicas_indispensable_escuela",
                  "matematicas_satisfactorio_escuela","matematicas_sobresalientes_escuela")

data_localidad <- data %>% 
  select(columnas_usar)

#elimina el objeto para liberar memoria
rm(data)

entidades <- data_localidad %>% 
   distinct(entidad) 
         
  
            
 
 
choices = setNames(entidades$entidad,entidades$entidad)
# Define UI for application that draws a histogram
ui <- fluidPage(
   
   # Application title
   #titlePanel("Mejores 10 Escuelas por Localidad"),
   
   # Sidebar with a slider input for number of bins 
   sidebarLayout(
      sidebarPanel(
        helpText("Grafica los resultados de las mejores 5 escuelas por localidad."),
        selectInput("entidad", h4("Selecciona una Entidad Federativa"), 
                    choices = choices),
        
         selectInput("localidad", h4("Selecciona una localidad"), 
                     choices = list("Seleccciona una localidad"= "selecciona")),
         selectInput("nivel", h4("Selecciona un nivel"), 
                      choices = list("Primaria" = "Primaria",
                                    "Secundaria" = "Secundaria"))
      ),
      # Show a plot of the generated distribution
      mainPanel(
        plotOutput("linePlot")
      )
     )
   )



# Define server logic required to draw a histogram
server <- function(input, output,session) {
  columnas = c( 8 ,9 ,10,11)
  
  observe({
    
    
  
    
   entidad_seleccionada <- input$entidad
   
  localidades_list <-  data_localidad %>% 
     filter(entidad == entidad_seleccionada) %>% 
     select(localidad) %>% 
    distinct(localidad) %>% 
    dplyr::arrange(localidad)
    
   
   
   # Can also set the label and select items
   updateSelectInput(session, "localidad",
                     choices = localidades_list,
                     selected = entidad_seleccionada
   )
   
   
  })
  
   output$linePlot <- renderPlot({
     
     localidad_seleccionada <- input$localidad
     
     # Can use character(0) to remove all choices
     if (is.null(localidad_seleccionada))
       localidad_seleccionada <- character(0)
     
     data_localidad %>% 
       filter(localidad==localidad_seleccionada,
              nivel == input$nivel,
              planea_semaforo ==1) %>% 
       top_n(5,desc(planea_rank_entidad)) %>% 
       ggparcoord(
         columns = columnas,
         groupColumn = "nombre",
         scale="globalminmax",
         order= columnas,
         alphaLines = 0.8,
         showPoints = TRUE
       ) +
       directlabels::geom_dl(aes(label = nombre), 
                             method = list( "smart.grid",cex=.8) 
       )+
       scale_color_brewer(type = "qual",palette = "Reds")+
       #scale_color_manual(values = )
       guides(color=FALSE)+
       xlab("")+
       ylab("Porcentaje")+
       labs(caption="@nerudista",
            title="Porcentaje de alumnos por categoría en Matematicas",
            subtitle= paste("Resultados PLANEA ", data_localidad$planea_year,
                            "para la Localidad: ",data_localidad$localidad )
       )+
       theme_hc()
     
   })
  
}

# Run the application 
shinyApp(ui = ui, server = server)

