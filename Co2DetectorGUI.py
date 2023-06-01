import serial
import PySimpleGUI as sg

ser = serial.Serial('COM3', 115200)
# Set up serial port COM3 and baud rate 115200

lable1 = sg.Text("CO2 value:", font=('Helvetica', 20))
lable2 = sg.Text("", font=('Helvetica', 20),size=(20,1))
lable3 = sg.Text("", font=('Helvetica', 20),size=(20,1))
button1 = sg.Button("Exit", key='button1')

layout = [[lable1, lable2], [lable3, button1]]

window1 = sg.Window('CO2 value', layout, font=('Helvetica', 20))

try:
    while True:
        event, values = window1.read(timeout=10)
        if event == 'button1':
            ser.close()
            break
        co2 = ser.readline().strip().decode()
        #Read the CO2 value from the serial port
        co2 = int(co2)

        lable2.update(str(co2))

        print(f"Current CO2 value: {co2}")

        print("ctrl + c to exit")

        if co2 > 2000:
            # To test the monitoring effect, you can lower the value to 2000
            warnStr = "CO2 value exceeds 2000, please take action!"
            print("CO2 value exceeds 2000, please take action!")
            lable3.update(warnStr)
        else:
            lable3.update('CO2 normal')
        window1.refresh()

except KeyboardInterrupt:
    ser.close()  # Close the serial port
    print('Goodbye!')

window1.close()
