#include <WiFi.h>;

const char* ssid = "Casa"; //definicao da rede
const char* password =  "121212121"; //definicao da senha

int botao = 2; //definicao do led para piscar quando pressionado o botao

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");
 
  pinMode(BOTAO,INPUT);
 
 
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
 
  Serial.println("\nConnected to the WiFi network");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
}
 
void loop() {
  if ((WiFi.status() == WL_CONNECTED)) //Check the current connection status
  {
    Serial.println("You can try to ping me");
    if (
    
    delay(5000);
  }
  else
  {
    Serial.println("Connection lost");
  }
}
