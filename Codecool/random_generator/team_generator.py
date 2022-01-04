import random

def read_name_file(name_list_file):
    with open(name_list_file) as f:
        return f.readlines()


def team_size_input(namelist) :
    while True:
        try:
            size = int(input(f"Ideal team size (2 - { len(namelist) }): "))
            if size < 2 or size > len(namelist):
                print(f"Please, user a number betwen 2 and {len(namelist)}.")
            else:
                return size
        except ValueError:
            print("Please, user numbers!")
        




def gen_and_print_small_groups(names_list, team_size): 
    team_number = len(names_list) // team_size
    teams_list = []
    names_list_copy = names_list[:]
    for n in range(team_number):
        teams_list.append(random.choices(names_list, team_size))


if __name__ == "__main__":
    print(read_name_file("names_list.txt"))