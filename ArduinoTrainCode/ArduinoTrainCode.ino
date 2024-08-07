int x;
String str;


void setup()
{

  Serial.begin(9600);
  
  pinMode(8, OUTPUT); // left - brown
  pinMode(9, OUTPUT); // right - orange
    
  pinMode(10, OUTPUT); // backward - white
  pinMode(11, OUTPUT); // forward - blue

  
}

void loop()
{
    if(Serial.available() > 0)
    {
        str = Serial.readStringUntil('\n');
        if (str.equals("l")) {
                 
          digitalWrite(8, HIGH);
          digitalWrite(9, LOW);
          digitalWrite(10, LOW);
          digitalWrite(11, LOW);
          delay(400);

          digitalWrite(8, LOW);
          digitalWrite(9, LOW);
          digitalWrite(10, LOW);
          digitalWrite(11, LOW);
        }
        if (str.equals("r")) {
          digitalWrite(9, LOW);
          digitalWrite(8, LOW);
          digitalWrite(10, HIGH);
          digitalWrite(11, LOW);  
          delay(400);

          digitalWrite(8, LOW);
          digitalWrite(9, LOW);
          digitalWrite(10, LOW);
          digitalWrite(11, LOW);                  
        }
        if (str.equals("b")) {
          digitalWrite(8, LOW);
          digitalWrite(9, HIGH);
          digitalWrite(10, LOW);
          digitalWrite(11, HIGH);
          delay(450);

          digitalWrite(8, LOW);
          digitalWrite(9, LOW);
          digitalWrite(10, LOW);
          digitalWrite(11, LOW);
          }
          
        if (str.equals("f")) {
          digitalWrite(8, HIGH);
          digitalWrite(9, LOW);
          digitalWrite(10, HIGH);
          digitalWrite(11, LOW);
          delay(450);

          digitalWrite(8, LOW);
          digitalWrite(9, LOW);
          digitalWrite(10, LOW);
          digitalWrite(11, LOW);
        }
        if (str.equals("s")) {
          digitalWrite(8, LOW);
        
          digitalWrite(9, LOW);
        
          digitalWrite(10, LOW);
        
          digitalWrite(11, LOW);
        }
    }
    }    
