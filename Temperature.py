from openai import OpenAI
import serial
import statistics

def read_arduino_data(port='/dev/cu.usbmodem101', baud_rate=9600, num_readings=20): #'/dev/cu.usbmodem101' is the port in the arduino IDE. May differ on devices and USB port used 
    readings = [] #list to store temperature readings
    try:
        with serial.Serial(port, baud_rate, timeout=1) as ser:
            print("Reading data from Arduino...")
            for _ in range(num_readings):
                line = ser.readline().decode('utf-8').strip()
                if line:
                    try:
                        readings.append(float(line))  # Convert to float if numerical data
                    except ValueError: #error handling for invalid data
                        print(f"Skipping invalid data: {line}")
    except serial.SerialException as e:
        print(f"Error: {e}")
    return readings

def find_median(readings):
    if readings:
        return statistics.median(readings)
    return None


sensor_readings = read_arduino_data('/dev/cu.usbmodem101', 9600, 20) #'/dev/cu.usbmodem101' is the port in the arduino IDE. May differ on devices and USB port used 
median_value = find_median(sensor_readings) # median value of 20 stored temperature readings to prevent outliers from afffecting results
print("Stored Readings:", sensor_readings) 
print("Median Temperature:", median_value, " degrees Celcius") 

location = input("Enter the location of the sensor reading: ") #user input
prompt = "in 50 words or less, reply to the following prompt: The temperature of " + location + " is " + str(median_value) + ". Is this temperature ideal for the location? " #ChatGPT prompt

client = OpenAI(
  api_key="XXXXXXXXXXX" #insert your API key here
)

completion = client.chat.completions.create(
  model="gpt-4o-mini", #ChatGPT model
  store=True,
  messages=[
    {"role": "user", "content": prompt}
  ]
)

print(completion.choices[0].message); #print ChatGPT response