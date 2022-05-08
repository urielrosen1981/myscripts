print('"Shuffle, Shuffle, Shuffle", say it together!\n Change colors and directions,\n Don\'t back down and stop the player! \n \tDo you want to play Taki? \n \tPress y\\n')

a_file = open("/Users/uriel/python/ssh_hosts.txt", "r")

lines = a_file.read().split('\n')
print(lines)

fileobj=open("/Users/uriel/python/ssh_hosts.txt", "r")
it=iter(fileobj)
lines=[]
while True:
    try:
        line=next(it)
        line=line.strip()
        lines.append(line)
    except StopIteration:
        break
print(lines)