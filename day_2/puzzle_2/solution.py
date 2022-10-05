def main():
    with open('./day_2/puzzle_1/input.txt', 'r') as f:
        input_text = f.read()
        instructions = input_text.split('\n')

    depth = 0
    h_pos = 0
    aim = 0

    for instruction in instructions:
        split_instruction = instruction.split(' ')
        if split_instruction[0] == 'forward':
            h_pos += int(split_instruction[1])
            depth += aim * int(split_instruction[1])
        
        if split_instruction[0] == 'down':
            aim += int(split_instruction[1])
        
        if split_instruction[0] == 'up':
            aim -= int(split_instruction[1])
    
    print(f'The Depth of the submarine is {depth}')
    print(f'The horizontal position of the submarine is {h_pos}')
    print(f'the final position of the submarine is {depth * h_pos}')


        

if __name__ == '__main__':
    main()