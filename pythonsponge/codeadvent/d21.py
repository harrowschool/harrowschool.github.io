###########################
# GLOBAL VARIABLES
###########################

regs = [0] * 10  # 10 registers
pc = 0  # program counter

###########################
# SUBPROGRAMS
###########################


def evalOperand(operand, pRegisters):
    if operand.startswith('#'):
        return int(operand[1:])
    else:
        return pRegisters[int(operand)]

###########################
# MAIN PROGRAM
###########################


# data setup - use example data for testing
data = '''\
LD 1 #5
OUT 1
SUB 1 #1
LD 1 0
CMP 1 #0
JN #2
JA #-5
HLT'''

# uncomment these three lines to use the real challenge data instead when ready
# file = open("d21.txt", "r")
# data = [list(line.strip()) for line in file.readlines()]
# file.close()  

# setup
instructions = data.splitlines()

# main loop
while True:

    parts = instructions[pc].split(' ')
    cmd, args = parts[0], parts[1:]

    # incremement the program counter ready for next loop
    pc += 1

    if cmd == 'HLT':
        # end of program
        break
    elif cmd == 'OUT':
        # output the required register
        print(evalOperand(args[0], regs))
    elif cmd == 'LD':
        # load the second operand into the specified register
        regs[int(args[0])] = evalOperand(args[1], regs)
    elif cmd == 'ADD':
        # add the two operands and store the result in the accumulator
        regs[0] = evalOperand(
            args[0], regs) + evalOperand(args[1], regs)
    elif cmd == 'SUB':
        # subtract the two operands and store the result in the accumulator
        regs[0] = __________ - __________
    elif cmd == 'MUL':
        # multiply the two operands and store the result in the accumulator
        regs[0] = __________ * __________
    elif cmd == 'DIV':
        # integer divide the two operands and store the result in the accumulator
        regs[0] = __________ // __________
    elif cmd == 'MOD':
        # find the remainder when dividing the two operands and store the result in the accumulator
        # ==> COMPLETE THIS NEXT LINE
        regs[0] = ___________________________________
    elif cmd == 'CMP':
        # compare the two operands and store in the accumulator either -1, 0 or 1
        # depending on whether the first operand is less than, equal to or greater than the second operand
        if evalOperand(args[0], regs) < evalOperand(args[1], regs):
            regs[0] = -1
        elif evalOperand(args[0], regs) > evalOperand(args[1], regs):
            regs[0] = 1
        else:
            # ==> COMPLETE THIS NEXT LINE
            regs[0] = __
    elif cmd in ['JN', 'JP', 'JZ', 'JA']:
        # jump to the specified offset if the jump condition is met
        offset = evalOperand(args[0], regs)
        # ==> COMPLETE THE TWO UNFINISHED CONDITIONS
        if (cmd == 'JN' and regs[0] < 0) or \
           (__________ and __________) or \
           (__________ and __________) or \ 
           cmd == 'JA':
            pc -= 1  # undo the pc increment from the top of the loop
            # ==> COMPLETE THIS NEXT LINE
            pc += ______
    else:
        raise Exception("Unknown instruction: " + cmd)
