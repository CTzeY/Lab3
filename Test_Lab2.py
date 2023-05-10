import Lab2 as Lab2

def test_calc_min_max_temperature():
    num_list = [2, 4, 6]
    result = Lab2.calc_min_max_temperature(num_list)
    assert (result == (2, 6))


def test_cal_average_temperature():
    num_list = [2, 4, 6]
    result = Lab2.cal_average_temperature(num_list)
    assert (result == 4)

def test_cal_median_temperature():
    num_list = [2, 4, 6]
    result = Lab2.cal_median_temperature(num_list)
    assert (result == 5)



