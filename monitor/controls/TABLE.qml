TableView {
                   
                   anchors.fill: parent
                   anchors.topMargin: 8
                   anchors.rightMargin: 8
                   anchors.bottomMargin: 8
                   anchors.leftMargin: 8
                                  
                    
                    
        columnSpacing: 0.5
        rowSpacing: 0.5
        boundsBehavior: Flickable.StopAtBounds

        model: TableModel {
            // TableModelColumn { display: "Nombre" }
            // TableModelColumn { display: "Apellido" }
            // TableModelColumn { display: "DNI" }
            // TableModelColumn { display: "Fecha de Nacimiento" }
            // TableModelColumn { display: "Obra Social" }
            // TableModelColumn { display: "Número de Afiliado" }
            // TableModelColumn { display: "Número de Teléfono" }
            // TableModelColumn { display: "Domicilio" }
            // TableModelColumn { display: "N° Historia Clínica" }
            // TableModelColumn { display: "Institución" }
            // TableModelColumn { display: "Médico Solicitante" }
            // TableModelColumn { display: "Prescripciones" }
            // TableModelColumn { display: "Enfermedades preexistentes" }
            TableModelColumn { display: "Nombre" }
            TableModelColumn { display: "Apellido" }
            TableModelColumn { display: "DNI" }
            TableModelColumn { display: "Fecha" }
            TableModelColumn { display: "ObraSocial" }
            TableModelColumn { display: "NAfiliado" }
            TableModelColumn { display: "NTel" }
            TableModelColumn { display: "Domicilio" }
            TableModelColumn { display: "NHistoriaC" }
            TableModelColumn { display: "Inst" }
            TableModelColumn { display: "Solicitante" }
            TableModelColumn { display: "Prescripciones" }
            TableModelColumn { display: "Enfermedades" }
            // Each row is one type of fruit that can be ordered
            rows: [{},{},{},{}
//                 {
//                     Nombre: "1",
//                     Apellido: "2",
//                     DNI:"3",
//                     Fecha:"14",
//                     ObraSocial:"11",
//                     NAfiliado:"22",
//                     NTel:"33",
//                     Domicilio:"44",
// NHistoriaC:"11",
// Inst:"22",
// Solicitante:"33",
// Prescripciones:"55",
// Enfermedades:"66"
//                 }
            ]
        }
        delegate:  TextInput {
            text: model.display
            padding: 12
            selectByMouse: true

            onAccepted: model.display = text

            Rectangle {
                anchors.fill: parent
                color: "#efefef"
                // z: -1
            }
        }
    }
    }