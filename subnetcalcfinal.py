"""
Subnet Calculator
subnet mask in binary
broadcast address,
wildcard mask
number of usable host addresses
created by Jennifer Burns October 2021
"""
import ipaddress

validvalues = [0, 128, 192, 224, 240, 248, 252, 254, 255]

print("Welcome to the subnet calculator! \n")

while True:
    ip = input("Please enter an IP address or type 'q' to quit \n")
    octets = ip.split(".")
    # allow user to exit at any time
    if ip == "q":
        break
    # check if there are 4 octets, if not, ip is invalid
    elif len(octets) != 4:
        print("Invalid IP address, please try again")
    else:
        # if there are 4 octets
        # assign variable to each octet
        a = int(octets[0])
        b = int(octets[1])
        c = int(octets[2])
        d = int(octets[3])
        # ensure first octet isn't loopback or 224 or above (class D or E)
        # ensure no octet is less than 0 or more than 255
        if a <= 0 or a == 127 or a >= 224 or b > 255 or b < 0 or c > 255 or c < 0 or d > 255 or d < 0:
            print("Invalid IP address, please try again")
        else:

            print(" ")
            while True:
                sm = input("Please enter a subnet mask or type 'q' to quit \n")
                octets = sm.split(".")
                if sm == "q":
                    break
                # check if there are 4 octets, if not, sm is invalid
                elif len(octets) != 4:
                    print("Invalid subnet mask, please try again")
                else:
                    # if there are 4 octets
                    # assign variable to each octet
                    a = int(octets[0])
                    b = int(octets[1])
                    c = int(octets[2])
                    d = int(octets[3])

                    # ensure first octet is 255
                    # ensure no octet is less than 0 or greater than 255
                    if a != 255 or b not in validvalues or c not in validvalues or d not in validvalues:
                        print("Invalid subnet mask, please try again")
                    else:
                        print(" ")
                        print("You have entered the IP address " +
                              str(ip) + " and the subnet mask " + str(sm) + "\n")
                        net = ipaddress.ip_network(ip + "/" + sm, strict=False)
                        print("Network Address: " + str(net))
                        print(
                            'Subnet Mask in binary: {0:08b}.{1:08b}.{2:08b}.{3:08b}'.format(a, b, c, d))
                        print("Broadcast address: " +
                              str(net.broadcast_address))
                        print("Wildcard Mask: " + str(net.hostmask))
                        print("Number of usable host addresses: " +
                              str(net.num_addresses - 2))
                        break
            break
