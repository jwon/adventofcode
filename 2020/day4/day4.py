required_fields = set([
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid'])

if __name__ == '__main__':
    valid_passports_count = 0
    seen_fields = set()
    with open('input.txt') as f:
        for line in f:
            if line == '\n':
                print(f'seen: {seen_fields}')
                if 'cid' in seen_fields:
                    seen_fields.remove('cid')
                if seen_fields == required_fields:
                    print('VALID')
                    valid_passports_count += 1
                seen_fields = set()
            else:
                for kv in line.strip().split(' '):
                    k, v = kv.split(':')
                    seen_fields.add(k)

    print(valid_passports_count)
