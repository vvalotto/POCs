import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
Item {
            
            Rectangle {
                id: contentPacient
                Text {
                    id: titlePaciente
                    color: "#666666"
                    text: qsTr("Paciente")
                    anchors.left: parent.left
                    anchors.top: parent.top
                    anchors.topMargin: 10
                    anchors.leftMargin: 30
                    font.bold: true
                    font.pixelSize: 30
                    verticalAlignment: Text.AlignTop
                }

                color: "#f3f3f3"
                anchors.fill: parent
            }
        }