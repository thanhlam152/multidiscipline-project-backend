const int capture_D = 4;
const int capture_A = A0;

int val_analog;

void setup() {
  // put your setup code here, to run once:
  pinMode(capture_D, INPUT);
  pinMode(capture_A, INPUT);
  Serial.begin(9600);
}

void loop() {

  // put your main code here, to run repeatedly:
  if(digitalRead(capture_D) == LOW) 
  {
    Serial.println("Digital value: wet"); 
    delay(10); 
  }
  else
  {
    Serial.println("Digital value: dry");
    delay(10); 
  }
  val_analog=analogRead(capture_A); 
  Serial.print("Analog value: ");
  Serial.println(val_analog); 
  delay(30000);
}
