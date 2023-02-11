import PySimpleGUI as sg


def convert(feet_input, Inches_input):
    Feet_meters = feet_input * 0.3048
    Inches_meters = Inches_input * 0.0254
    meters = Feet_meters + Inches_meters
    return meters



feet_label = sg.Text("Enter feet: ")
feet_input = sg.Input(key="feet")
Inches_label = sg.Text("Enter inches: ")
Inches_input = sg.Input(key="inches")

Conv_button = sg.Button("Convert")
output_label = sg.Text("", key="output")

window = sg.Window("Conversion to Meters", layout=[[feet_label, feet_input],
                                                   [Inches_label, Inches_input],
                                                   [Conv_button, output_label]])

while True:
    event, values = window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = convert(feet, inches)
    window["output"].update(value=f"{result} m", text_color="white")

window.close()