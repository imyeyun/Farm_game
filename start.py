from classes.Farm_class import *
class Game:
    def Farm()=farm
    def start_game():
        main_loop()

    if __name__ == "__main__":
        print("-------Farm Game-------")
        isEnd = False
        while True:
            print("""
            1. 게임시작
            2. 불러오기
            3. 종료
            """)
            op=input("번호를 입력하세요:")
            if op=="1":
                print("농장으로 이동합니다.")
                start_game()

    def main_loop():
        go_to=0
        while True:
            if go_to=="0":
                print("농장에 오신걸 환영합니다.")
                print("""
                1. 밭으로
                2. 농작물 판매점으로
                3. 씨앗 가게로
                4. 메인 메뉴로
                5. 저장하기
                """)
                choose=input("번호를 입력하세요:")    
                if choose=="1":
                    print("밭으로 이동합니다.")
                    garden_proc()
                elif choose=="2":
                    print("농작물 판매점으로 이동합니다.")
                    crop_store_proc()

                elif choose=="3":
                    print("씨앗상점으로 이동합니다.")
                    seed_store_proc()
                elif choose=="4":
                    break
                elif choose=="5":
                    f = open("./data/save_data.txt", "w")
                    f.write("저장")
                    f.close()
                    break
                else:
                    print("메뉴를 다시 확인하세요.")

    def garden_proc():
        while True:
            print("밭에 도착하였습니다.")
            print("1.농작물심기\n2.농작물 확인\n3.수확하기\n4.수확하기")
            garden_op==int(input("메뉴를 선택하세요")) 
            if garden_op=="1":
                Farm.print_crop_list()


    def crop_store():
        print("농작물 판매점에 오신 것을 환영합니다.")
        print("""
        1.판매하기
        2. 뒤로가기
        """)
        crop_store_op==int(input("메뉴를 선택하세요")) 

    def seed_store():
        print("씨앗상점에 오신걸 환영합니다.")
        print("""
        1.구매하기
        2. 뒤로가기
        """)
        seed_store_op==int(input("메뉴를 선택하세요")) 

game=Game()                 
print(game)        
game.choose()
#