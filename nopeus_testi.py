import time
start_time = time.time()


def str_testi():
    koti_str = "3"
    vieras_str = "1"

    if koti_str < vieras_str:
        tulos_yksiristikaksi = "2"
    elif koti_str > vieras_str:
        tulos_yksiristikaksi = "1"
    else:
        tulos_yksiristikaksi = "x"


def int_testi():
    koti_int = 3
    vieras_int = 1


    if koti_int < vieras_int:
        tulos_yksiristikaksi = "2"
    elif koti_int > vieras_int:
        tulos_yksiristikaksi = "1"
    else:
        tulos_yksiristikaksi = "x"


for _ in range(50000000):
    int_testi()


print("--- %s seconds ---" % (time.time() - start_time))

