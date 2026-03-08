from converter14 import convert
import FreeSimpleGUI as sg



label1 = sg.Text("Enter feet:")
input_box1 = sg.InputText(key="feet")
label2 = sg.Text("Enter inches:")
input_box2 = sg.InputText(key="inches")
convert_button = sg.Button("Convert")
output_label = sg.Text("", key="output")


window = sg.Window('Feet and Inches to Meters Convertor',
                   layout=[[label1, input_box1], [label2, input_box2], [convert_button, output_label]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = convert(feet, inches)
    window["output"].update(value=f"{result} m", text_color="red")

window()

