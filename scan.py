def scan_sensors():
    for channel in range (8):
        i2c.writeto(0x70, (pow(2,channel)).to_bytes(1,1))#0x70 is the address of the multiplexer. The rest creates the byte channel addresses
        print("Scan channel " + str(channel))
        i2c.scan()
        for device_address in i2c.scan():
            print(hex(device_address))
            if device_address != 0x70:
                occupied_channels.append(channel)
    print("Occupied channels ",occupied_channels)
    return occupied_channels
