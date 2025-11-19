import os

cur_dir = os.path.dirname(os.path.abspath(__file__))

# get all dirs under this 

sub_dirs = [d for d in os.listdir(cur_dir) if os.path.isdir(os.path.join(cur_dir, d))]

for d in sub_dirs:
    # full_path = os.path.join(cur_dir, d)

    #     for file in os.listdir(full_path):
    #         if file.endswith("output.txt"):
    #             # read the file
    #             file_path = os.path.join(full_path, file)
    #             with open(file_path, "r", encoding="utf-8") as f:
    #                 content = f.read()

    #             # there maybe having the following format in the file
    #             # ```
    #             # content important ...
    #             # content important ...
    #             # ```
    #             # we need to remove the ``` part
    #             if content.startswith("```") and content.endswith("```"):
    #                 # remove the first and last ```
    #                 content = "\n".join(content.split("\n")[1:-1])
    #                 # write back to the file
    #                 with open(file_path, "w", encoding="utf-8") as f:
    #                     f.write(content)

    # get sub dirs under d
    sub_dirs_2 = [sd for sd in os.listdir(os.path.join(cur_dir, d)) if os.path.isdir(os.path.join(cur_dir, d, sd))]
    for sd in sub_dirs_2:
        full_path_2 = os.path.join(cur_dir, d, sd)
        for file in os.listdir(full_path_2):
            if file.endswith("output.txt"):
                # read the file
                file_path = os.path.join(full_path_2, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # there maybe having the following format in the file
                # need to find the last two ``` and extract the content inside and then remove all other content`
                # some above content (optional)
                # ```
                # content important ...
                # content important ...
                # ```
                # we need to remove the ``` part

                if content.count("```") >= 2:
                    parts = content.split("```")
                    content = "\n".join(parts[-2].split("\n")[1:-1])
                    # write back to the file
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(content)