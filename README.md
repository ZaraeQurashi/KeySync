# KeySync — Custom MIDI Controller

A custom-built MIDI controller inspired by Undertale, featuring seven heart-shaped capacitive touch keys, two mechanical pushbuttons, and a rotary encoder.

KeySync combines custom PCB design, programming, and game inspired aesthetics to create a unique musical  device. The heart-shaped touch pads are inspired by the 7 SOULS from the game UNDERTALE, giving the controller a recognizable design while serving as its main musical input.

<img width="396" height="418" alt="image" src="https://github.com/user-attachments/assets/349983c1-e04f-49aa-9521-d57348450333" />


---

## Table of Contents

- [Project Overview](#project-overview)
- [Hardware](#hardware)
- [PCB Design](#pcb-design)
- [Controls and Key Mapping](#controls-and-key-mapping)
- [Firmware](#firmware)
  
---


## Project Overview

KeySync started as an idea for a custom MIDI controller that would combine my interests in electronics, programming, and video games. Instead of using a standard keyboard layout, I wanted to design something with a distinct appearance that reflected the games that inspired it.

The project involved designing the circuit in KiCad, arranging components on a custom PCB, creating heart-shaped copper electrodes for the touch keys, routing the board, developing the firmware, and documenting the parts required to build it.

One of the main goals was to make the controller visually interesting while still keeping the controls practical. The seven touch keys provide the main musical input, the mechanical pushbuttons add two extra notes, and the rotary encoder provides a convenient way to control system volume.

### Project Details

| Category | Details |
|---|---|
| Project name | KeySync |
| Project type | Custom MIDI controller |
| Microcontroller | Seeed Studio XIAO ESP32-S3 |
| PCB design software | KiCad |
| Firmware language | Python |
| Firmware environment | CircuitPython |
| Keyboard framework | KMK |
| Main inputs | 7 capacitive touch pads |
| Additional inputs | 2 mechanical pushbuttons |
| Encoder | 1 rotary encoder |
| Design inspiration | UNDERTALE |


## Hardware

KeySync is built around the Seeed Studio XIAO ESP32-S3 microcontroller. The board acts as the controller for the inputs and runs the firmware that determines how the device responds to them.

The hardware consists of three main input groups.

### 1. Capacitive Touch Keys

The seven heart-shaped electrodes are the main controls on KeySync. They are designed to detect touch and correspond to individual notes in a C-major scale.

Unlike a mechanical switch, a capacitive touch key doesn't require a physical contact to close a circuit. Instead, the sensing system detects a change in capacitance when a finger approaches or touches the electrode.

<img width="470" height="284" alt="image" src="https://github.com/user-attachments/assets/d752bc4e-3b55-4c2d-ad83-705d44679a83" />


### 2. Mechanical Pushbuttons

KeySync also includes two low-profile mechanical pushbuttons. These provide additional physical inputs that can be used alongside the touch keys. 

The firmware assigns each button a separate drum note, allowing them to trigger additional sounds or percussion samples in compatible MIDI software. The buttons use GPIO inputs configured with pull-ups, with the inputs changing state when the buttons connect their respective pins to ground.

<img width="350" height="200" alt="image" src="https://github.com/user-attachments/assets/a316d7fd-2385-4af0-abef-f1ad75c18c48" />


### 3. Rotary Encoder

The rotary encoder provides a control that can be turned in either direction. In the current firmware configuration, it is intended to adjust the computer's system volume.

<img width="150" height="170" alt="image" src="https://github.com/user-attachments/assets/5af9144e-3306-41da-b398-14af75fc230e" />

---

## PCB Design

The PCB was designed in KiCad. After completing the schematic, I moved on to arranging the components, creating the board outline, designing the custom heart-shaped electrodes, and routing the electrical connections.

### Schematic and Component Placement

The schematic defined the electrical connections between the microcontroller and the various inputs. Once the schematic was ready, I transferred the components into the PCB layout and began arranging them to fit the board.

During this stage, I encountered footprint sizing issues and had to adjust an oversized footprint to fit the available space. I also revised some schematic connections and custom footprint pad numbers to make sure the PCB layout matched the intended electrical connections.

This reinforced the importance of checking the physical dimensions of components and the electrical mapping of their pads.

<img width="500" height="400" alt="image" src="https://github.com/user-attachments/assets/233f5fed-5439-491b-89de-4259ab9ecb95" />



### Routing

After settling on the component placement, I routed the PCB using both copper layers.

- **F.Cu — Front copper:** Used for routing the capacitive touch key connections.
- **B.Cu — Back copper:** Used for routing the mechanical switch connections.

Using both layers helped organize the traces and make better use of the available board space.

## Controls and Key Mapping

The firmware is configured to map the seven touch keys to a C-major scale, the two mechanical buttons to drum notes, and the rotary encoder to system volume control.

### Capacitive Touch Keys

| Touch key | MIDI note number | Intended note |
|---|---:|---|
| Heart 1 | 60 | C4 |
| Heart 2 | 62 | D4 |
| Heart 3 | 64 | E4 |
| Heart 4 | 65 | F4 |
| Heart 5 | 67 | G4 |
| Heart 6 | 69 | A4 |
| Heart 7 | 71 | B4 |


### Mechanical Pushbuttons

| Button | MIDI note number | Intended use |
|---|---:|---|
| Button 1 | 36 | Drum/percussion trigger |
| Button 2 | 38 | Drum/percussion trigger |

### Rotary Encoder

| Control | Function |
|---|---|
| Rotary encoder | Increase or decrease computer system volume |
| Communication method | Media-key commands in the current firmware design |

<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/20ee327a-0d12-4e51-a01d-7f2ac76a2792" />



---

## Firmware

The firmware is written in Python using CircuitPython and KMK. It handles input scanning, maps the controls to their intended functions, and provides the logic needed for the controller to respond to touches, button presses, and encoder movements.

### Firmware Structure

The code is organized around several main responsibilities:

**Touch sensing:** Reads the state of the seven capacitive touch inputs and detects changes between touched and untouched states.

**Button scanning:** Reads the two mechanical pushbuttons and determines when they are pressed or released.

**Key mapping:** Associates each touch key and pushbutton with its assigned MIDI note.

**Encoder controls:** Reads the rotary encoder and triggers the appropriate system volume command.

<img width="413" height="344" alt="image" src="https://github.com/user-attachments/assets/5ba86b8f-7ecf-4a5e-85ee-4a6ffabe0004" />


### GPIO Pin Mapping

The following GPIO assignments are from the current firmware configuration.

| Control | GPIO pin |
|---|---|
| Capacitive touch key 1 | GPIO3 |
| Capacitive touch key 2 | GPIO4 |
| Capacitive touch key 3 | GPIO5 |
| Capacitive touch key 4 | GPIO6 |
| Capacitive touch key 5 | GPIO7 |
| Capacitive touch key 6 | GPIO8 |
| Capacitive touch key 7 | GPIO9 |
| Mechanical pushbutton 1 | GPIO43 |
| Mechanical pushbutton 2 | GPIO44 |
| Rotary encoder signal A | GPIO1 |
| Rotary encoder signal B | GPIO2 |

### MIDI Behaviour

The seven touch keys are intended to send MIDI note events corresponding to the C-major scale. Touching a key triggers a Note On event, while releasing it triggers a matching Note Off event.

The two mechanical pushbuttons are assigned to notes 36 and 38 for percussion.

---

## Challenges and Lessons Learned

Developing KeySync involved more than creating a circuit board. Some of the most important work happened while adapting the firmware and making sure the software matched the hardware.

### PCB Design Challenges

Creating the PCB required me to design custom heart-shaped electrodes, fit the components within the board outline, fix an oversized footprint, and revise pad numbers and connections. Routing the switches and touch keys across two copper layers also required careful planning.

These challenges taught me to check both the physical and electrical sides of a design. A footprint can look correct on screen but still be unsuitable for the actual component, and an attractive layout is not useful if the pads do not connect to the intended signals.

<img width="254" height="243" alt="image" src="https://github.com/user-attachments/assets/3cbb13bb-78e8-4827-9e64-04769b5e8284" />


### Firmware Compatibility

I initially explored an Arduino-based firmware approach and encountered compatibility problems involving USB MIDI classes, MIDI event types, and capacitive touch functions. I eventually moved to CircuitPython and KMK, which meant adapting the implementation instead of simply transferring the earlier code.

This taught me that code written for one development environment does not automatically work in another. Microcontroller features, library APIs, and USB support can differ significantly between boards and programming environments.

---

## Final Summary

KeySync brought together my interests in electronics, programming and gaming into one custom MIDI controller inspired by UNDERTALE. From designing the PCB and seven heart-shaped capacitive touch keys in KiCad to developing the CircuitPython/KMK firmware, creating the BOM, and documenting everything on GitHub, I gained hands-on experience with both hardware and software. Although troubleshooting firmware compatibility was challenging, it taught me to approach problems systematically and consider how every part of a project works together. Overall, KeySync helped me better understand the process of turning an idea into a custom electronic device.

<img width="492" height="361" alt="image" src="https://github.com/user-attachments/assets/fbe6e974-0b6a-4398-bcfb-69ec2154f24f" />
