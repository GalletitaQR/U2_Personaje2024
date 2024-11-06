from machine import Pin, time_pulse_us, PWM
import time
from time import sleep

# Definicion de los pines DH-SR04 y LEDs
PIN_TRIG = 15
PIN_ECHO = 4
bOnf1 = Pin(21, Pin.IN, Pin.PULL_UP)
led_v = Pin(18, Pin.OUT)  # LED verde
led_r = Pin(22, Pin.OUT)  # LED rojo
trig = Pin(PIN_TRIG, Pin.OUT)
echo = Pin(PIN_ECHO, Pin.IN)

alarm_sequence = [
    (1000, 500), (1500, 500), 
    (1000, 500), (1500, 500),
]

# LED rojo
led_r.value(1)

# funcion al presionar que se ejcuta al presionar el botón
def toggle_led1(pin):
    led_v.value(0)  # LED verde abajo
    led_r.value(1)  # LED rojo
 arriba    buzzer.deinit()  

bOnf1.irq(trigger=Pin.IRQ_FALLING, handler=toggle_led1)

def measure_distance():
    # medición
    trig.value(1)
    time.sleep_us(10)  # Espera 10 microsegundos
    trig.value(0)

    duration = time_pulse_us(echo, 1)  # Mide la duración del pulso
    distance_cm = duration / 58.0  # Calcula la distancia en cm
    return distance_cm

while True:
    # Verifica si el LED rojo está encendido
    if led_r.value() == 1:
        distance_cm = measure_distance()  # Mide la distancia
        print("Distance in CM:", distance_cm)

        # Comprueba si la distancia si es menor a 16cm
        if distance_cm < 16:
            # Muy cerca, encender LED verde y apagar LED rojo
            led_v.value(1)
            led_r.value(0)

            # se vuelve a iniciar el buzzer
            buzzer = PWM(Pin(17), freq=440, duty=512)
            
            # Reproduce la melodía
            for note, duration in alarm_sequence:
                buzzer.freq(note)  # Cambia la frecuencia
                time.sleep_ms(duration)  # Espera la duración de la nota

            buzzer.deinit()  # Desactiva el buzzer al terminar la melodía

    time.sleep(1)  # Espera 1 segundo
