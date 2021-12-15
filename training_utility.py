import os

def gen_negative_txt_file():
    with open("-ve.txt", "w") as f:
        for filename in os.listdir("images/negatives"):
            f.write("images/negatives/" + filename + "\n")