def warn_the_sheep(queue):
    sheep_number = 0
    result = ""
    if queue[-1] == "wolf":
        result = "Pls go away and stop eating my sheep"
        return result
    else:
        for i in range(len(queue)-1, -1, -1):
            if queue[i] == "wolf":
                sheep_number = len(queue) - i - 1
                result = "Oi! Sheep number " + str(sheep_number) + "! You are about to be eaten by a wolf!"                
        return result

print(warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf'] ))