import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Item {
            
            Rectangle {
                Text {
                    id: titleEstudio
                    color: "#666666"
                    text: qsTr("Estudio")
                    font.bold: true
                    font.pixelSize: 30
                    verticalAlignment: Text.AlignTop
                    anchors.left: parent.left
                    anchors.top: parent.top
                    anchors.topMargin: 10
                    anchors.leftMargin: 30
                }
                color: "#f4f4f4"
                anchors.fill: parent
            }
        }