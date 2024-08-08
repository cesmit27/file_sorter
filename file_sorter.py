import os, shutil

def sort(path):
    file_names = os.listdir(path)

    folder_names = ['csv files', 'image files', 'pdf files', 'Microsoft Office Files', 'text files']
    for i in range(0, len(folder_names)):
        if not os.path.exists(path + folder_names[i]):
            os.makedirs(path + folder_names[i])

    unsupported_files = []

    for file in file_names:
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            continue
        if ".csv" in file and not os.path.exists(path + "csv files/" + file):
            shutil.move(path + file, path + "csv files/" + file)
        elif ".png" in file or ".jpg" in file or ".JPG" in file or ".jpeg" in file and not os.path.exists(path + "image files/" + file):
            shutil.move(path + file, path + "image files/" + file)
        elif ".pdf" in file and not os.path.exists(path + "pdf files/" + file):
            shutil.move(path + file, path + "pdf files/" + file)
        elif ".docx" in file or ".doc" in file or ".pptx" in file or ".ppt" in file or ".xlsx" in file and not os.path.exists(path + "Microsoft Office Files/" + file):
            shutil.move(path + file, path + "Microsoft Office Files/" + file)
        elif ".txt" in file and not os.path.exists(path + "text files/" + file):
            shutil.move(path + file, path + "text files/" + file)
        else:
            unsupported_files.append(file)

    if len(unsupported_files) > 0:
        print("Warning: The following files are of unsupported types and were not moved:")
        for i, unsupported_file in enumerate(unsupported_files, start=1):
            print(f" {i}. {unsupported_file}")
        input("\n\nPress Enter to close...")


directory = "C:\\Example_Directory\\" #Add your directory here
sort(directory)
