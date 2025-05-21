def appearance(intervals):
    lesson_start, lesson_end = intervals['lesson']
    pupil_time = intervals['pupil']
    tutor_time = intervals['tutor']

    def process_intervals(timestamps, lesson_start, lesson_end):
        intervals = []
        for i in range(0, len(timestamps), 2):
            start = max(timestamps[i], lesson_start)
            end = min(timestamps[i + 1], lesson_end)
            if start < end:
                intervals.append((start, end))
        if not intervals:
            return []
        intervals.sort()
        merged = [intervals[0]]
        for curr in intervals[1:]:
            last = merged[-1]
            if curr[0] <= last[1]:
                merged[-1] = (last[0], max(last[1], curr[1]))
            else:
                merged.append(curr)
        return merged

    pupil_merged = process_intervals(timestamps=pupil_time, lesson_start=lesson_start, lesson_end=lesson_end)
    tutor_merged = process_intervals(timestamps=tutor_time, lesson_start=lesson_start, lesson_end=lesson_end)

    total = 0
    i = j = 0
    while i < len(pupil_merged) and j < len(tutor_merged):
        pupil_start, pupil_end = pupil_merged[i]
        tutor_start, tutor_end = tutor_merged[j]

        start = max(pupil_start, tutor_start)
        end = min(pupil_end, tutor_end)
        if start < end:
            total += end - start

        if pupil_end < tutor_end:
            i += 1
        else:
            j += 1

    return total

tests = [
    {
        'intervals': {
            'lesson': [1594663200, 1594666800],
            'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
            'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
        },
        'answer': 3117
    },
    {
        'intervals': {
            'lesson': [1594702800, 1594706400],
            'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
            'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]
        },
        'answer': 3577
    },
    {
        'intervals': {
            'lesson': [1594692000, 1594695600],
            'pupil': [1594692033, 1594696347],
            'tutor': [1594692017, 1594692066, 1594692068, 1594696341]
        },
        'answer': 3565
    },
]

if __name__ == '__main__':
    all_passed = True
    for i, test in enumerate(tests):
        try:
            test_answer = appearance(test['intervals'])
            assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
            print(f"Test {i} passed")
        except AssertionError as e:
            print(e)
            all_passed = False

    if all_passed:
        print('OK')