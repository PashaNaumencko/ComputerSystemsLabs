def base64_encode(read_file_path, write_file_path):
    with open(read_file_path, "rb") as stream_for_read:
        data = stream_for_read.read()
        start_data_length = len(data)
        number_to_char_list = [char for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"]
        base64_list = []
        while len(data) % 3 != 0:
            data += bytes([0])
        for i in range(0, len(data), 3):
            base64_list += [data[i] >> 2]
            base64_list += [(data[i] & 3) << 4 | data[i + 1] >> 4]
            base64_list += [(data[i + 1] & 15) << 2 | data[i + 2] >> 6]
            base64_list += [data[i + 2] & 63]
        base64_string =  "".join([number_to_char_list[number] for number in base64_list])
        last_char_index = 3 - (start_data_length % 3)
        if last_char_index:
            base64_string = base64_string[:-last_char_index] + "=" * last_char_index
        with open(write_file_path, "w") as stream_for_write:
            stream_for_write.write(base64_string)