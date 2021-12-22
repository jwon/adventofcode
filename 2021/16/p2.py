from math import prod


def parse_packet(packet):
    print(packet)
    pointer = 3
    version = int(packet[:pointer], 2)
    end = pointer + 3
    type_id = int(packet[pointer:end], 2)
    pointer = end
    print(f'Version: {version} Type ID: {type_id}')

    if type_id == 4:  # Literal value
        step = 5
        result = ''
        for i in range(pointer, len(packet), step):
            group = packet[i:i+step]
            result += group[1:]
            if group[0] == '0':
                return int(result, 2), i+step, version
    else:  # Operator packet
        length_type_id = packet[pointer]
        print(f'Length Type ID: {length_type_id}')
        pointer += 1
        version_sum = version
        if length_type_id == '0':  # Length subpackets
            end = pointer + 15
            length_subpackets = int(packet[pointer:end], 2)
            pointer = end
            print(f'Length of subpackets: {length_subpackets}')
            end_subpackets = pointer + length_subpackets
            subpacket_results = []
            while pointer < end_subpackets:
                result, end, version = parse_packet(packet[pointer:end_subpackets])
                print(f'subpacket result: {result}')
                subpacket_results.append(result)
                version_sum += version
                pointer += end
            return calculate_value_of_subpackets(type_id, subpacket_results), pointer, version_sum
        else:  # Number of subpackets
            end = pointer + 11
            num_subpackets = int(packet[pointer:end], 2)
            pointer = end
            print(f'Num subpackets: {num_subpackets}')
            subpacket_results = []
            for _ in range(num_subpackets):
                result, end, version = parse_packet(packet[pointer:])
                print(f'subpacket result: {result}')
                subpacket_results.append(result)
                version_sum += version
                if end is not None:
                    pointer += end
            return calculate_value_of_subpackets(type_id, subpacket_results), pointer, version_sum


def calculate_value_of_subpackets(type_id, subpackets):
    if type_id == 0:
        return sum(subpackets)
    elif type_id == 1:
        return prod(subpackets)
    elif type_id == 2:
        return min(subpackets)
    elif type_id == 3:
        return max(subpackets)
    elif type_id == 5:
        return 1 if subpackets[0] > subpackets[1] else 0
    elif type_id == 6:
        return 1 if subpackets[0] < subpackets[1] else 0
    elif type_id == 7:
        return 1 if subpackets[0] == subpackets[1] else 0


with open('input.txt') as f:
    packet = ''.join(f'{int(char, 16):04b}' for char in f.readlines()[0].strip())
result, pointer, version_sum = parse_packet(packet)
print(f'result: {result}')
print(f'pointer: {pointer}')
print(f'version_sum: {version_sum}')
