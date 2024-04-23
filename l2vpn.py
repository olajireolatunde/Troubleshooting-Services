from netmiko import ConnectHandler
import getpass

List_of_Routers = {}
CID = input('please enter service ID for this service \n')
Number_of_Routers = int(input("How many routers: "))
user = input('please enter username:\n')
print("Please enter password:\n")
password = getpass.getpass()

for number in range(1, Number_of_Routers +1):
        Router = input("Enter Router IP:")
        List_of_Routers[Router] = [user,password]

for router in List_of_Routers:
        Devices = { "host": router,
                "username": List_of_Routers[router][0],
                "password": List_of_Routers[router][1],
                "device_type": "cisco_ios_telnet",
                "secret" : List_of_Routers[router][1]
            }
        Connect_To_Device = ConnectHandler(**Devices)

        Connect_To_Device.enable()
        print("Successfully connected to: ", router)

        Commands = "show int desc | inc" + ' ' + CID

        output = Connect_To_Device.send_command(Commands)

        with open("C:\\Users\\13401872\\Documents\\PYTHON\\Troubleshooting Services\\L2VPN\\ROUTER\\ " + CID + ".txt", "a")as file:
                file.write("\n")
                file.write(router + "#" + Commands)
                file.write("\n")
                file.write(output)
                file.close
        new_file = open('C:\\Users\\13401872\\Documents\\PYTHON\\Troubleshooting Services\\L2VPN\\ROUTER\\ ' + CID + '.txt', 'r')
        for line in new_file:
                if line.startswith('Te') or line.startswith('Gi'):
                    interface = line[0:16]
                    file.close
                    Connect_To_Device = ConnectHandler(**Devices)
                    Connect_To_Device.enable()
                    print("Successfully connected to: ", router)
                    New_Command = ["show run interface " + interface,"show l2vpn xconnect interface " + interface + ' detail']
                    for new_command in New_Command:
                        new_output = Connect_To_Device.send_command(new_command)
                        with open("C:\\Users\\13401872\\Documents\\PYTHON\\Troubleshooting Services\\L2VPN\\ROUTER\\ " + CID + ".txt", "a")as file:
                            file.write('\n')
                            file.write(router + "#" + new_command)
                            file.write("\n")
                            file.write(new_output)
                            file.close
                elif line.startswith("BE"):
                    interface = line[0:9]
                    file.close
                    Connect_To_Device = ConnectHandler(**Devices)
                    Connect_To_Device.enable()
                    print("Successfully connected to: ", router)
                    New_Command = ["show run interface " + interface,"show l2vpn xconnect interface " + interface + ' detail']
                    for new_command in New_Command:
                        new_output = Connect_To_Device.send_command(new_command)
                        with open("C:\\Users\\13401872\\Documents\\PYTHON\\Troubleshooting Services\\L2VPN\\ROUTER\\ " + CID + ".txt", "a")as file:
                            file.write('\n')
                            file.write(router + "#" + new_command)
                            file.write("\n")
                            file.write(new_output)
                            file.close


print("TROUBLESHOOTING COMPLETED, PLEASE CHECK FILE")
