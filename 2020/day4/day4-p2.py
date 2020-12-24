import re


def validate_passport(passport):
    required_fields = [
            'byr',
            'iyr',
            'eyr',
            'hgt',
            'hcl',
            'ecl',
            'pid']
    passport_fields = passport.keys()
    for field in required_fields:
        if field not in passport_fields:
            print(f'INVALID: missing {field} in {passport}')
            return False

    birth_year = int(passport['byr'])
    if not (1920 <= birth_year <= 2002):
        print(f'INVALID: byr not within range: {birth_year}')
        return False
    issue_year = int(passport['iyr'])
    if not (2010 <= issue_year <= 2020):
        print(f'INVALID: iyr not within range: {issue_year}')
        return False
    expiration_year = int(passport['eyr'])
    if not (2020 <= expiration_year <= 2030):
        print(f'INVALID: eyr not within range: {expiration_year}')
        return False
    height = passport['hgt']
    if not (('cm' in height and (150 <= int(height.split('cm')[0]) <= 193)) or ('in' in height and (59 <= int(height.split('in')[0]) <= 76))):
        print(f'INVALID: hgt not within range: {height}')
        return False
    hair_color = passport['hcl']
    if re.match(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hair_color) is None:
        print(f'INVALID: hcl not a hex color: {hair_color}')
        return False
    eye_color = passport['ecl']
    if eye_color not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        print(f'INVALID: ecl not valid: {eye_color}')
        return False
    passport_id = passport['pid']
    if re.match(r'^\d{9}$', passport_id) is None:
        print(f'INVALID: pid not valid: {passport_id}')
        return False

    return True


if __name__ == '__main__':
    valid_passports_count = 0
    passport = {}
    with open('input.txt') as f:
        for line in f:
            if line == '\n':
                if validate_passport(passport):
                    valid_passports_count += 1
                passport = {}
            else:
                for kv in line.strip().split(' '):
                    k, v = kv.split(':')
                    passport[k] = v

    print(valid_passports_count)
