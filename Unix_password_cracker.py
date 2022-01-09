import crypt
import argparse

def argument_parser():
    parser = argparse.ArgumentParser(description = "Crack hashed passwords by generating a rainbow table.")
    parser.add_argument("--repo", nargs= "?",default="./plaintext_repo.txt")
    parser.add_argument("--pass_file", nargs="?",default="./user_passwords.txt")
    var_args = vars(parser.parse_args())
    return var_args

def password_check(hashed_pass):
    salt = hashed_pass[:2]
    with open(plaintext_pwords) as repo:
        for word in repo.readlines():
            word = word.strip("\n")
            digest = crypt.crypt(word,salt)
            if digest == hashed_pass:
                print("[+] Found Password: {}\n".format(word))


def parse_file(username):
    with open(username) as pass_file:
        for line in pass_file.readlines():
            if ":" in line:
                username = line.split(":")[0]
                pass_digest = line.split(":")[1].strip(" ")
                print("[*] Cracking Password for : {}".format(username))
                password_check(pass_digest)


if __name__ == "__main__":
    user_args = argument_parser()
    plaintext_pwords = user_args["repo"]
    digests = user_args["pass_file"]
    parse_file(digests)
