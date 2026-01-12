#include <WiFi.h>
#include <WiFiUdp.h>

const char* ssid = "WIFI_SSID";
const char* password = "WIFI_PASSWORD";

WiFiUDP Udp;
unsigned int localPort = 8888;

// Motor driver pins (L298N / L293D)
int L1 = 18;
int L2 = 19;
int R1 = 21;
int R2 = 22;

void setup() {
  Serial.begin(115200);

  pinMode(L1, OUTPUT);
  pinMode(L2, OUTPUT);
  pinMode(R1, OUTPUT);
  pinMode(R2, OUTPUT);

  Serial.println("Connecting to WiFi...");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConnected to WiFi!");
  Serial.print("ESP32 IP: ");
  Serial.println(WiFi.localIP());

  Udp.begin(localPort);
  Serial.println("UDP listening...");
}

void loop() {
  int packetSize = Udp.parsePacket();
  if (packetSize) {
    char cmd[50];
    int len = Udp.read(cmd, 49);
    if (len > 0) cmd[len] = '\0';
    String command = String(cmd);
    command.trim();

    Serial.println("Received: " + command);

    if (command == "FORWARD") forward();
    else if (command == "BACKWARD") backward();
    else if (command == "LEFT") left();
    else if (command == "RIGHT") right();
    else stopCar();
  }
}

void forward() {
  Serial.println("→ Forward");
  digitalWrite(L1, HIGH);
  digitalWrite(L2, LOW);
  digitalWrite(R1, HIGH);
  digitalWrite(R2, LOW);
}

void backward() {
  Serial.println("← Backward");
  digitalWrite(L1, LOW);
  digitalWrite(L2, HIGH);
  digitalWrite(R1, LOW);
  digitalWrite(R2, HIGH);
}

void left() {
  Serial.println("↺ Left");
  digitalWrite(L1, LOW);
  digitalWrite(L2, HIGH);
  digitalWrite(R1, HIGH);
  digitalWrite(R2, LOW);
}

void right() {
  Serial.println("↻ Right");
  digitalWrite(L1, HIGH);
  digitalWrite(L2, LOW);
  digitalWrite(R1, LOW);
  digitalWrite(R2, HIGH);
}

void stopCar() {
  Serial.println("■ Stop");
  digitalWrite(L1, LOW);
  digitalWrite(L2, LOW);
  digitalWrite(R1, LOW);
  digitalWrite(R2, LOW);
}

