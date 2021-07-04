# levande
> Publish the health status of systems via MQTT

## Usage

### Configuration file

The configuration file is a simple JSON file. Each system has to be configured with a unique `id`, the `method` to obtain the health status with and further method specific properties. 

The following methods are available and require different properties:
- `HTTP` (GET request that expects a response code 200)
  - `url` (String): HTTP(S) URL that will be requested
- `Port` (Checks if specific TCP port is open)
  - `host` (String): Host name / IP
  - `port` (Number): Port
- `Ping` (Checks ping to host)
  - `host` (String): Host name / IP

Example configuration:
<pre>
{ 
    "systems": [ 
        { "id": "example", "method": "HTTP", "url": "https://example.org" },
        { "id": "badexample", "method": "HTTP", "url": "http://brokenwebsite.example.org" },
        { "id": "portexample", "method": "Port", "host": "example.org", "port": 80 },
        { "id": "pingexample", "method": "Ping", "host": "example.org" }
    ] 
}
</pre>
The configuration above would result in the following MQTT structure:
<pre>
> levande
  > lastUpdate = 2021-07-04 12:34:56.123456
  > example = UP
  > badexample = DOWN  
  > portexample = UP
  > pingexample = UP
</pre>

### Environment variables

The following environment variables can be set:
- MQTT_BROKER_HOST: host of MQTT broker (default: '127.0.0.1')
- MQTT_BROKER_PORT: port of MQTT broker (default: '1883')
- MQTT_CLIENT_ID: MQTT client id (default: random)
- MQTT_USERNAME: MQTT username (default: none)
- MQTT_PASSWORD: MQTT password (default: none)
- MQTT_TOPIC_PREFIX: topic prefix (default: 'levande/')
- SLEEP_TIME: frequency of health checks in secs (default: '30')
- LEVANDE_CONFIG_FILE: config file to define the systems to be checked (default: '/var/levande/config/levande.json')
- LEVANDE_STATUS_UP: status value for healthy web apps (default: 'UP')
- LEVANDE_STATUS_DOWN: status value for broken web apps (default: 'DOWN')
- VERIFY_SSL: true/false if SSL certs should be verified

### docker-compose example

<pre>
version: '3'

services:
  
  levande:
    image: patrickvogel/levande:latest
    restart: always
    volumes:
      - ./volumes/levande/config:/var/levande/config
    environment:
      TZ: "Europe/Berlin"
      MQTT_BROKER_HOST: "192.168.0.123"
      LEVANDE_STATUS_UP: "YAY"
      LEVANDE_STATUS_DOWN: "NAY"
      VERIFY_SSL: "false"
</pre>
