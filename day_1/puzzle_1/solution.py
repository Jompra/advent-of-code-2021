
def main():
    increases = 0

    with open('./day_1/puzzle_1/input.txt', 'r') as f:
        input_text = f.read()
    
    report_nums = input_text.split('\n')

    for i in range(len(report_nums)):

        if int(report_nums[i]) > int(report_nums[i - 1]):
            increases += 1

    print(f'There are {increases} measurements that are larger than the previous measurement')
        

if __name__ == '__main__':
    main()