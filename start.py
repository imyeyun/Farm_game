from Farm_class import *
from Asset_class import *
from Seed_class import *
farm=Farm("")
asset=Asset()
seed=Seed()
class Game:
    def first(self):
        while True:
            print("-------Farm Game-------")
            print("""
            1. 게임시작
            2. 불러오기
            3. 종료
            """)
            op=input("번호를 입력하세요:")
            if op=="1":
                print("농장에 오신걸 환영합니다.농장에서 10000원을 벌어봅시다.현재 자산은 %d원 입니다."%asset.money)
                game.start_game()
            elif op=="2":
                pass

            elif op=="3":
                print("프로그램을 종료합니다.")
                break

            else :
                print("잘못된 번호입니다.")     
    def garden_proc():
        while True:
            print("밭에 도착하였습니다.")
            print("1.농작물심기\n2.농작물 확인\n3.수확하기\n4.돌아가기")
            garden_op=int(input("메뉴를 선택하세요")) 
            if garden_op=="1":
                farm.print_crop_list()

            elif garden_op=="2":
                pass

            elif garden_op=="3":  
                pass 

            elif garden_op=="4": 
                break   


    def crop_store():
        while True:
            print("농작물 판매점에 오신 것을 환영합니다.")
            print("""
            1.판매하기
            2. 뒤로가기
            """)
            crop_store_op=int(input("메뉴를 선택하세요")) 
            if crop_store_op=="1":
                pass
    def seed_store():
        while True:
            print("씨앗상점에 오신걸 환영합니다.")
            print("""
            1.구매하기
            2. 뒤로가기
            """)
            if seed_store_op=="1":
                farm.seed_store_menu
                seed_store_op = int(input("메뉴를 선택해주세요: "))

                if seed_store_op == 1:
                    seed.print_sell_list()
                    
                    item_num = int(input("구매하실 아이템을 선택하세요: "))

                    item = seed.sell_list[item_num-1]
                    if asset.money - item.price < 0:
                        print("소지금이 부족합니다.")
                    else:

                        asset.money -= item.price
                        print("%s 아이템을 구매했습니다." % item.name)
                    
                    print("확인")


            elif seed_store_op=="2":
                break
    def start_game(self):
        go_to=0
        while True:
            if go_to=="0":
                print("""
                1. 밭으로
                2. 농작물 판매점으로
                3. 씨앗 가게로
                4. 메인 메뉴로
                """)
                choose=input("번호를 입력하세요:")    
                if choose=="1":
                    print("밭으로 이동합니다.")
                    game.garden_proc()
                elif choose=="2":
                    print("농작물 판매점으로 이동합니다.")
                    game.crop_store()

                elif choose=="3":
                    print("씨앗상점으로 이동합니다.")
                    game.seed_store()
                elif choose=="4":
                    break
                else:
                    print("메뉴를 다시 확인하세요.")                        

game=Game()                 
game.first()
print(game)