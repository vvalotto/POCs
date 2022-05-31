import QtQuick
import QtQuick.Window
import QtQuick.Controls.Material 2.15

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    //modality: Qt.ApplicationModal
    title: qsTr("Hello World")

    // SET FLAGS
    flags: Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint | Qt.CustomizeWindowHint | Qt.MSWindowsFixedSizeDialogHint | Qt.WindowTitleHint

    Material.theme: Material.Dark
    Material.accent: Material.LightBlue
}
