# 모든 파일 list를 가져오는 방법
import glob

path = "gugu*.txt"
total = glob.glob(path)  # 현재 경로에 존재하는 gugu로 시작하는 모든 파일 명 읽어옴
# 결과를 순서대로 가져오지 않음 / sort 필요

with open("gugu_all.txt", "w+") as handle:
    for filename in total:
        with open(filename, "r") as hand:
            for line in hand:
                handle.write(line)

# fw = open("gugu_all.txt",'w+')

# for filename in total:
#         with open(filename, "r") as hand:
#             for line in hand:
#                 fw.write(line)
# fw.close()
