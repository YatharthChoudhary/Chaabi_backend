def get_file_type(extension_type_list, file_list):
    file_type_dict = {}

    extension_type_dict = {}
    for pair in extension_type_list.split(";"):
        extension, file_type = pair.split(",")
        extension_type_dict[extension] = file_type

    for file_name in file_list:
        if "." in file_name:
            extension = file_name.split(".")[-1]
            if extension in extension_type_dict:
                file_type_dict[file_name] = extension_type_dict[extension]
            else:
                file_type_dict[file_name] = "unknown"
        else:
            file_type_dict[file_name] = "unknown"

    return file_type_dict

