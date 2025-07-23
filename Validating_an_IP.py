def is_valid_ipv4_address(ip_address):
    
    
    parts = ip_address.split('.')
    
    if len(parts) != 4:
        return False
    
    for i, part in enumerate(parts):
        try:
            num = int(part)
            if num < 0 or num > 255:
                return False
            # Check if the last number contains a 0
            if i == 3 and '0' in part:
                return False
        except ValueError:
            return False
    
    return True

#-------------------------------------------------------

ip_address = input('Enter an IP address: ')
if is_valid_ipv4_address(ip_address):
    print('Valid IPv4 address')
else:
    print('Invalid IPv4 address')
