def wave(people):
    iteration = 0
    wave_list = []
    iteration_in_for = 0
    while(iteration < len(people)):
        new_word = ""
        for letter in people:
            if (letter == " "):
                iteration_in_for -= 1
            if(iteration_in_for == iteration):
                new_word += letter.upper()
            else:
                new_word += letter
            iteration_in_for += 1
        iteration_in_for = 0
        if(True != new_word.islower()):
            wave_list.append(new_word)
        new_word = ""
        iteration += 1
    return wave_list