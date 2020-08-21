import fakeGen

for i in range(10):
    nick=fakeGen.nick()
    print("\033[32mNICK GENERADO:\033[0m \033[35m"+nick+"\033[0m")