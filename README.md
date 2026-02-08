# IoT Thermal Fan Control Evolution
## IoT Thermal Control Evolution Project Setup

### Phase 1: Arduino Prototype (Arduino Uno R3)
- [ ] Create Arduino sketch for temperature sensor reading
- [ ] Implement PWM fan control in Arduino
- [ ] Add serial communication for monitoring
- [ ] Create circuit diagram/documentation

### Phase 2: AVR C Conversion
- [ ] Port Arduino code to raw AVR C
- [ ] Implement ADC for temperature sensor
- [ ] Implement Timer/PWM for fan control
- [ ] Setup UART communication

### Phase 3: STM32F401RE Port
- [ ] Port AVR C code to STM32 HAL
- [ ] Configure ADC for STM32
- [ ] Configure Timer/PWM for STM32
- [ ] Setup UART communication for STM32

### Phase 4: Web Application
- [ ] Create web server backend (Node.js/Python)
- [ ] Implement real-time data communication (WebSocket)
- [ ] Build web UI for monitoring temperature
- [ ] Add fan control interface

### Documentation
- [ ] Update README with project description
- [ ] Add build/setup instructions
- [ ] Document hardware requirements

<!-- START COPILOT CODING AGENT SUFFIX -->



<!-- START COPILOT ORIGINAL PROMPT -->



<details>

<summary>Original prompt</summary>

> Well my project is gonna be an IoT app that controls a fan through a web app, with real time monitoring of the temperature. I plan on making my prototype with Arduino libraries, converting it to raw avr C then finally convert the project from an arduino uno r3 to another micro controller: stm32f401re
> 
> 


</details>



<!-- START COPILOT CODING AGENT TIPS -->
---

💡 You can make Copilot smarter by setting up custom instructions, customizing its development environment and configuring Model Context Protocol (MCP) servers. Learn more [Copilot coding agent tips](https://gh.io/copilot-coding-agent-tips) in the docs.
