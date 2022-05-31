import QtQuick
import QtQuick.Window
import QtCharts 2.3

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("Holter Laboratorios Bagó")
    property QtObject plotter

    ChartView {
        id: chart
        x: 300
        y: 150
        width: 600
        height: 300
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter

        ValuesAxis {
            id: axisX
            min: 0.0
            max: 800.0
            // gridLineColor: 'red'
        }

        DateTimeAxis {
            id: axis_X
            format: "mm:ss"
            titleText: "Time (mm:ss)"
            min: new Date(2022, 1, 1, 0, 0, 0, 0)
            max: new Date(2022, 1, 1, 0, 1, 0, 0)
            tickCount: 1
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
            plotter.get_series(chart.series(0))
        }
    }

    Component.onCompleted: {
        console.log("Se ha iniciado QML\n")
        var series = chart.createSeries(ChartView.SeriesTypeLine, "channel 1",
                                        axisX, axisY)
    }
}
