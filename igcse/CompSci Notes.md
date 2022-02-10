# 3 Fetch Execute Cycle 

### Summary

1. PC has address of next instruction
2. PC copied to the MAR (via address bus)
3. Address in MAR is looked up and the contents are stored in the MDR
4. MDR copied to CIR
5. PC incremented by 1
6. The instruction is decoded and executed (by sending signals via the control bus)
7. Repeat



### Registers

They are high speed, expensive and limited storage within the CPU

| MAR  | Memory Address Register      | Holds the memory address of the next instruction to be accessed |
| ---- | ---------------------------- | ------------------------------------------------------------ |
| MDR  | Memory Data Register         | Holds instruction from memory                                |
| AC   | Accumulator                  | Holds intermediate arithmetic/logic results                  |
| PC   | Program Counter              | Holds memory address of the next instruction                 |
| CIR  | Current Instruction Register | Holds the current instruction                                |

### Buses

| Address Bus | Carries the **addresses** of data                            |
| ----------- | ------------------------------------------------------------ |
| Data Bus    | Carries data between processor and memory                    |
| Control Bus | Carries commands from the processor to coordinate and control other components |