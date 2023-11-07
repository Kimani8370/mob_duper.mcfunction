# File generated (specified as "Output file name" when running
# the program) will have to run along with a "scoreboard players
# add frames cred_step 1", meaning you must have a controlling
# function looking like:
#
# ----------------------------------------------------
# ...
# scoreboard players add frames cred_step 1
# function my_generated_credits.mcfunction
# ...
# ----------------------------------------------------
#
# You can also add some sound effects on the controlling function,
# so it would be like a typewriter. Also, the text color is green
# by default, feel free to edit this file in lines 35, 38 and 40 to
# adapt the commands to your needs.

file_out = input("Output file name: ")
file_in = input("Input text file: ")
delay = int(input("Delay when text fully shown (in ticks): "))
lw = int(input("Line width: "))

f_out = open(file_out,"w")
f_in = open(file_in,"r")

score = 0
for line in f_in.readlines():
    line = line[:-1]
    chars_line = len(line)
    for i in range(lw+1+chars_line):
        score += 1
        line_pre = "_"*(lw-i)
        line_post = "_"*(i-chars_line)
        if (lw-i) == 0:
            write_str = "execute if score frames cred_step matches " + str(score) + ".." + str(score+delay-1) + " run title @a actionbar {\"text\":\"" + line_pre + line[0:i] + line_post + "\",\"color\":\"green\"}\n"
            score += delay-1
        elif (lw-i) > 0:
            write_str = "execute if score frames cred_step matches " + str(score) + " run title @a actionbar {\"text\":\"" + line_pre + line[0:i] + line_post + "\",\"color\":\"green\"}\n"
        else:
            write_str = "execute if score frames cred_step matches " + str(score) + " run title @a actionbar {\"text\":\"" + line_pre + line[i-71:] + line_post + "\",\"color\":\"green\"}\n"
        f_out.write(write_str)
        #print(write_str)

f_out.close()
f_in.close()