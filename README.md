# RPi-temperature-logger
A data logging project involving the Raspberry Pi 3 and DHT22 sensor. By making use of the NGinx web server, uWSGI and Flask, a web application stack is developed to display temperatures in real time.
To do: Automatically create graphs to analyze temperature/humidity pattern using past records.

You need to set up and install components for the web application stack to get started: 
1. NGinx (web server) 
2. uWSGI (application server)
3. Python virtual environment
4. Flask 

Hardware setup
Make the following connections using jumper wires:
1. 3.3V pin of the DHT22 to pin 1 of the Raspberry Pi (3.3V)
2. Data pin of the DHT22 to pin 13 of the Raspberry Pi (GPIO27)
3. Ground pin of the DHT22 to pin 39 of the Raspberry Pi (GND) 
Have a look at the setup.jpg file for a graphical view
