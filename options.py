import argparse,subprocess,os
parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("--a", default=1, type=int, help="This is the 'a' variable")
parser.add_argument("--education", 
                    choices=["highschool", "college", "university", "other"],
                    required=True, type=str, help="Your name")

args = parser.parse_args()

ed = args.education

if ed == "college" or ed == "university":
    cmd = 'uptime'
    os.system(cmd)
    #result.stdout
elif ed == "highschool":
  print("Finished Highschool")
else:
    print("Does not have degree")