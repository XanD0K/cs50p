import re

def main():
    ip = input("IPv4 Address: ").strip()
    print(validate(ip))


def validate(ip):
    if matches := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        for group in matches.groups():
            # Check for leading zeros
            if len(group) > 1 and group[0] == "0":
                return False
            # Check range number from 0 to 255           
            if not 0 <= int(group) <= 255:
                return False
        return True
    return False


if __name__ == "__main__":
    main()

# TODO: apply other Ip's constraints
# TODO: check for public/private Ip