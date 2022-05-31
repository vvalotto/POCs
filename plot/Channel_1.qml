import QtQuick
import QtQuick.Window
import QtQuick.Controls.Material 2.12
import QtQuick.Controls
import QtQuick.Layouts 6.0
import Qt5Compat.GraphicalEffects
import QtCharts 2.3


    Item{
        id: itt
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
                            min: 3.0
                            max: 5.0
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