cl = {
    "Algorithm": "204",
    "DataAnalysis": "207",
    "ArtificialIntelligence": "302",
    "CyberSecurity": "B101",
    "Network": "303",
    "Startup": "501",
    "TestStrategy": "105",
}

n = int(input())

input_list = list()
for i in range(n):
    input_list.append(input())

for e in input_list:
    print(cl[e])
