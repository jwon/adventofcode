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
            while pointer < end_subpackets:
                result, end, version = parse_packet(packet[pointer:end_subpackets])
                print(f'subpacket result: {result}')
                version_sum += version
                pointer += end
            return 'DONE LEN SUBPACKETS', pointer, version_sum
        else:  # Number of subpackets
            end = pointer + 11
            num_subpackets = int(packet[pointer:end], 2)
            pointer = end
            print(f'Num subpackets: {num_subpackets}')
            for _ in range(num_subpackets):
                result, end, version = parse_packet(packet[pointer:])
                print(f'subpacket result: {result}')
                version_sum += version
                if end is not None:
                    pointer += end
            return 'DONE NUM SUBPACKETS', pointer, version_sum


with open('input.txt') as f:
    packet = ''.join(f'{int(char, 16):04b}' for char in f.readlines()[0].strip())
result, pointer, version_sum = parse_packet(packet)
print(f'result: {result}')
print(f'pointer: {pointer}')
print(f'version_sum: {version_sum}')
