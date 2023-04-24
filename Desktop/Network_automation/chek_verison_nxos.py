from netmiko import ConnectHandler
from pass_encoding_decoding import decoded_password
# Specify the file path
ip_device = 'ip.txt'  # Replace with your actual file path

#Open the file in read mode
with open(ip_device, 'r') as file:
    # Read the contents of the file
    total_ip = 0
    for line in file:
        temp = line.strip()
        device = {
            'device_type': 'cisco_nxos',
            'ip': temp,
            'username': 'net-user',
            'password': decoded_password,
            'port': 22,  # Default SSH port for Cisco Nexus
        }

        # Define the command to retrieve version and OS information
        command = 'show version'

        # Establish an SSH connection to the switch
        connection = ConnectHandler(**device)

        # Send the command to retrieve the information
        output = connection.send_command(command)

        # Parse the output to extract the version and OS information
        lines = output.splitlines()
        os_version = ''
        software = ''
        for line in lines:
            if 'NXOS:' in line:
                os_version = line.split(':')[-1].strip()
                print(f'Switch OS version: {os_version}' + ' ' +  device['ip'])
            elif 'system:' in line:
                software = line.split(':')[-1].strip()
                print(f'Switch OS version: {software}'+ ' ' + device['ip'])

        # Print the retrieved information
        # Close the SSH connection
        connection.disconnect()

# #Define the switch's connection parameters
# device = {
#     'device_type': 'cisco_nxos',
#     'ip': '192.168.20.100',
#     'username': 'net-user',
#     'password': 'decoded_password',
#     'port': 22,  # Default SSH port for Cisco Nexus
# }

# #Define the command to retrieve version and OS information
# command = 'show version'

# #Establish an SSH connection to the switch
# connection = ConnectHandler(**device)

# #Send the command to retrieve the information
# output = connection.send_command(command)

# #Parse the output to extract the version and OS information
# lines = output.splitlines()
# os_version = ''
# software = ''
# for line in lines:
#     if 'NXOS:' in line:
#         os_version = line.split(':')[-1].strip()
#     if 'system:' in line:
#         software = line.split()[1]

# #Print the retrieved information
# print(f'Switch OS version: {os_version}')
# print(f'Switch software: {software}')

# #print(output)

# #Close the SSH connection
# connection.disconnect()

