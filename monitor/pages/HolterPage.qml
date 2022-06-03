import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Item {
            
            Rectangle {
                Text {
                    id: titleHolter
                    color: "#666666"
                    text: qsTr("Holter")
                    font.bold: true
                    font.pixelSize: 30
                    verticalAlignment: Text.AlignTop
                    anchors.left: parent.left
                    anchors.top: parent.top
                    anchors.topMargin: 10
                    anchors.leftMargin: 30
                }
                color: "#f5f5f5"
                anchors.fill: parent
            }
        }