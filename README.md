# smartThermometer
A smart, AI based system integrating Python, C++, OpenAI API, and Arduino for measuring temperature and providing AI-driven insights to the ideal temperature of the user-provided location in real-time. The Temperature is read through the sensor and the values are sent to the arduino which then prints the values to the serial monitor every 10 seconds. The 20 temperature values are retrieved from the serial monitor in python and stored in a list. The median is then calculated and stored. The user is promted for the location of the sensor and the location, as welll as the median temperature value are used in a prompt to ChatGPT to know if the temperature is ideal for the user-provided loaction. The response, of 50 words or less, to the prompt is displayed in the Python terminal.


Software Requirements:

Arduino IDE

Python 3.x

Required Python libraries: pyserial, statistics, OpenAI

Hardware Requirements:

Arduino Mega 2560

Temperature sensor

Jumper wires

USB cable

Computer
