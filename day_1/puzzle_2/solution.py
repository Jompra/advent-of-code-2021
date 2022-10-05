
def main():
    with open('./day_1/puzzle_2/input.txt', 'r') as f:
        input_text = f.read()
    
    report_nums = input_text.split('\n')
    sliding_window_totals = []
    increases = 0

    for i in range(len(report_nums)):
        report_nums[i] = int(report_nums[i])

    for i in range(len(report_nums) - 2):
        sliding_window_totals.append(report_nums[i] + report_nums[i + 1] + report_nums[i + 2])
    
    for i in range(len(sliding_window_totals)):
        if int(sliding_window_totals[i]) > int(sliding_window_totals[i - 1]):
            increases += 1

    print(f'There are {increases} sums larger than the previous sum')
        

if __name__ == '__main__':
    main()