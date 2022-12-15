const int pinLED = 8;

void setup() {
  Serial.begin(9600);
  pinMode(pinLED, OUTPUT);

}

void loop() {
  if (Serial.available() > 0){
    char serialData = Serial.read();

    if(serialData == '1'){
      digitalWrite(pinLED, 1);
    } else if(serialData == '0'){
      digitalWrite(pinLED, 0);
    }

  }

}
