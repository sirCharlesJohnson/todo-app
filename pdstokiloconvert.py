from pds_kilo_converter import convert
import FreeSimpleGUI as sg



label1 = sg.Text("Enter Pounds:")
input_box1 = sg.InputText(key="Pounds")

convert_button = sg.Button("Convert")
output_label = sg.Text("", key="output")


window = sg.Window('Pounds to Kilograms Converter',
                   layout=[[label1, input_box1], [convert_button, output_label]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    Pounds = float(values["Pounds"])
    result = convert(Pounds)
    window["output"].update(value=f"{result} kilograms", text_color="red")

window()

