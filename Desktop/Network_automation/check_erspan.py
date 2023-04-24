from netmiko import ConnectHandler
from pass_encoding_decoding import decoded_password
# Define the device information
device = {
    'device_type': 'cisco_nxos',
    'ip': '192.168.20.240',  # Replace with the IP address of your Nexus switch
    'username': 'net-user',  # Replace with your username
    'password': decoded_password,  # Replace with your password
}

# Connect to the Nexus switch
connection = ConnectHandler(**device)
connection.enable()

erspan_session_id = 1  # Replace with the ERSPAN session ID you want to configure
config_commands = [
    'monitor session ' + str(erspan_session_id) + ' type erspan-source',
    'shut down',
    'no shut'
]

# Define the command to retrieve version and OS information
command = 'show monitor session 1' 
command1 = 'end'
# Establish an SSH connection to the switch
connection = ConnectHandler(**device)
connection.enable()

# Send the command to retrieve the information
output = connection.send_command(command)

# Parse the output to extract the version and OS information
lines = output.splitlines()
state1 = ''
for line in lines:
    if 'state' in line:
        state1 = line.split(':')[-1].strip() 
        if state1 == 'up':
            output = connection.send_command(command1)
            print(output)
        elif state1 != 'up':
            output = connection.send_config_set(config_commands)
         

print(connection.send_command(command))

# Disconnect from the Nexus switch
connection.disconnect()

