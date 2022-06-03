import QtQuick
import QtQuick.Controls
import Qt5Compat.GraphicalEffects
import QtCharts 2.3



Item {
          
            Rectangle {
                id: contentMonitor
                Text {
                    id: titleMonitor
                    color: "#666666"
                    text: qsTr("Monitoreo")
                    font.bold: true
                    font.pixelSize: 30
                    horizontalAlignment: Text.AlignLeft
                    verticalAlignment: Text.AlignTop
                    anchors.left: parent.left
                    anchors.top: parent.top
                    anchors.topMargin: 10
                    anchors.leftMargin: 30
                }
                Text {
                    id: descriptionMonitor
                    y: 74
                    color: "#666666"
                    text: "Verifique la adquisición de las señales y luego presione <i>\"Iniciar Estudio\"</i> para comenzar el registro."
                    anchors.left: titleMonitor.left
                    anchors.bottom: titleMonitor.top
                    font.pixelSize: 14
                    verticalAlignment: Text.AlignVCenter
                    anchors.leftMargin: 0
                    anchors.bottomMargin: -80
                }
                Text {
                    id: initRate
                    x: 30
                    color: "#666666"
                    text: qsTr("Ingrese <b>ritmo inicial</b>: ")
                    font.pixelSize: 16
                    anchors.top: descriptionMonitor.bottom
                    anchors.topMargin: 30
                    anchors.left: descriptionMonitor.left
                }
                TextInput {
                    id: inputInitRate
                    anchors.left: initRate.right
                    width: 2 * initRate.width
                    //height: 2 * initRate.height
                    color: "#666666"
                    text: qsTr("ej.: Normal")
                    anchors.verticalCenter: initRate.verticalCenter
                    font.pixelSize: 16
                    verticalAlignment: Text.AlignVCenter
                    font.italic: true
                    selectByMouse: true
                    cursorVisible: true
                    font.wordSpacing: 0.4
                    selectionColor: "#b4a6039b"
                    anchors.leftMargin: 10
                }
                FastBlur {
                    anchors.fill: signalsPlotArea
                    source: signalsPlotArea
                    transparentBorder: true
                    radius: 10
                }
                Rectangle {
                    id: signalsPlotArea
                    color: "#f9f9f9"
                    radius: 5
                    border.color: "#ae930089"
                    border.width: 4
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.top: initRate.bottom
                    anchors.rightMargin: 30
                    anchors.leftMargin: 30
                    anchors.topMargin: 32
                    anchors.bottom: parent.bottom
                    anchors.bottomMargin: 60
                    ChartView {
                        id: channel
                        legend.visible: false
                        anchors.left: parent.left
                        anchors.right: parent.right
                        // height: signalsPlotArea.height/3
                        backgroundColor: "transparent"
                        anchors.top: parent.top
                        anchors.bottom: parent.bottom
                        antialiasing: true
                        anchors.topMargin: 0
                        anchors.bottomMargin: parent.height - parent.height / 3 - 65
                        ValuesAxis {
                            id: axisX
                            visible: false
                            min: 0.0
                            max: 1600.0
                            // gridLineColor: 'red'
                        }

                        ValuesAxis {
                            id: axisY
                            min: 3.4
                            max: 4.1
                            // gridLineColor: 'red'
                            // shadesVisible: true
                        }
                    }
                    Connections {
                        target: plotter
                        function onSend(ser) {
                            plotter.get_series(channel.series(0))
                        }
                    }

                    Component.onCompleted: {
                        var series = channel.createSeries(
                                    ChartView.SeriesTypeLine, "Canal 1",
                                    axisX, axisY)
                    }
                    FastBlur {
                        anchors.fill: channel
                        source: channel
                        radius: 20
                    }
                }

                Button {
                    id: initStudio
                    text: qsTr("Iniciar Estudio")
                    height: 45
                    font.pixelSize: 14
                    anchors.right: signalsPlotArea.right
                    anchors.top: signalsPlotArea.bottom
                    anchors.topMargin: 2
                }
                Text {
                    id: plotFeet
                    color: "#666666"
                    text: qsTr(" Paciente: - ID: - Estudio: - Dispositivo: ")
                    anchors.verticalCenter: initStudio.verticalCenter
                    font.pixelSize: 14
                    font.italic: true
                    anchors.rightMargin: 10

                    anchors.right: initStudio.left
                }

                color: "#f6f6f6"
                anchors.fill: parent
            }
        }