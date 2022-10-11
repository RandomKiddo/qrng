# QRNG

A quantum random number generator based on IBM's quantum computer simulation and Qiskit

___

### Quantum Random Number Generator

Based on the amount of bits provided, a random number is generated based on a circuit of a quantum and classical register. Then an HGate is applied to the circuit and measured. Then, in one shot, the circuit pings each qubit and returns a value of `0` or `1`, and then a binary string is strung for each qubit. Then the number is converted into decimal, and the result is provided. 

Circuit and result for a 16-bit random number:
![](16bit.png)

<br>

Circuit and result for a 4-bit random number:
![](4bit.png)

<br>

Circuit and result for a 4-bit random number in range [0,10] (bits selected automatically):
![](in.png)

<br>
___

[Back to Top](#qrng)

<sub>This page was last edited on 10.11.2022</sub>